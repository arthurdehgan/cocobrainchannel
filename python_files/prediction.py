"""Small example OSC server

This program listens to several addresses, and prints some information about
received packets.
"""
import sys
import numpy as np
from scipy.io import savemat
import sys
from params import SIPADDR, CIPADDR
from sklearn.externals import joblib
import warnings
import os
warnings.filterwarnings("ignore")


from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client


first = True
SUB = sys.argv[1]
PATH = 'data/'
raw_data = []
DATALEN = 1100
DATASTEP = 220
SPORT = int(sys.argv[2])
CPORT = SPORT + 10
FILENAME = PATH + SUB + '_raw_pred.mat'

classif = {}
pred = [[] * len(classif)]
for file in os.listdir(PATH):
    if SUB in file and file.endswith('.pkl'):
        suf = "".join(file.split('_')[1:3])
        classif[suf] = joblib.load(PATH + file)


def rhandler(unused_addr, args, ch1, ch2, ch3, ch4):
    global raw_data, DATALEN, DATASETP, FILENAME
    raw_data.append([ch1, ch2, ch3, ch4])
    if len(raw_data) >= DATALEN:
        DATALEN = len(raw_data) + DATASTEP
        savemat(FILENAME, {'data': raw_data})


def handler(unused_addr, args, ch1,ch2,ch3,ch4):
    global pred, first
    data = np.array([ch1, ch2, ch3, ch4]).reshape(1, -1)
    if len(pred[0]) < 3:
        for i, key in enumerate(classif):
            pred[i].append(classif[key].predict(data))
    if len(pred[0]) >= 3:
        for i, key in enumerate(classif):
            prediction = int(round(np.mean(pred[i])))
            sys.stdout.write('\r' + str(prediction))
            sys.stdout.flush()
            client.send_message("/predict/" + key, prediction)
            if first:
                client.send_message("/predict/start", 1)
                first = False
            pred[i] = pred[i][1:]

if __name__ == "__main__":
  client = udp_client.SimpleUDPClient(CIPADDR, CPORT)

  baseline = []
  L = np.array([]).reshape(0,4)
  R = np.array([]).reshape(0,4)
  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/muse/elements/gamma_absolute", handler, L)
  dispatcher.map("/muse/eeg", rhandler, R)

  server = osc_server.ThreadingOSCUDPServer(
      (SIPADDR, SPORT), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()
