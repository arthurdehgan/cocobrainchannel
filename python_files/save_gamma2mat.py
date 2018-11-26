"""Small example OSC server

This program listens to several addresses, and prints some information about
received packets.
"""
import sys
import math
from time import time
import numpy as np
from scipy.io import savemat
import sys
import os
import warnings
from params import SIPADDR

from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client
warnings.filterwarnings("ignore")


data, raw = [], []
DATALEN = 20
DATASTEP = 5
RAWDATALEN = 800
RAWDATASTEP = 220
SPORT = sys.argv[2]
SPORT = int(SPORT)
SUB = sys.argv[1]
PATH = 'data/'
TYPE = sys.argv[3]
if len(sys.argv) > 4:
    LENGTH = int(sys.argv[4])
else:
    LENGTH = 100000
THRESH = LENGTH * 10
if not PATH.endswith('/'):
    PATH += '/'
if not os.path.exists(PATH):
     os.makedirs(PATH)
FILENAME = PATH + SUB + '_' + TYPE
RAWFILENAME = PATH + SUB + '_raw_' + TYPE


def rhandler(unused_addr, args, ch1,ch2,ch3,ch4):
    global raw, RAWDATALEN, RAWFILENAME, RAWDATASTEP, THRESH
    raw.append([ch1,ch2,ch3,ch4])
    if len(raw) >= RAWDATALEN:
        RAWDATALEN = len(data) + RAWDATASTEP
        savemat(RAWFILENAME, {'raw': raw})


def handler(unused_addr, args, ch1,ch2,ch3,ch4):
    global data, DATALEN, FILENAME, DATASTEP, raw
    data.append([ch1,ch2,ch3,ch4])
    sys.stdout.write('\r' + str(len(data)) + '/' + str(THRESH))
    sys.stdout.flush()
    if len(data) >= DATALEN:
        DATALEN = len(data) + DATASTEP
        savemat(FILENAME, {'gamma': data})
    if len(data) >= THRESH and len(raw) >= LENGTH * 200:
        os._exit(0)


if __name__ == "__main__":
  client = udp_client.SimpleUDPClient('127.0.0.1', 5005)

  baseline = []
  L = np.array([]).reshape(0,4)
  R = np.array([]).reshape(0,4)
  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/muse/elements/gamma_absolute", handler, L)
  dispatcher.map("/muse/eeg", rhandler, R)

  server = osc_server.ThreadingOSCUDPServer(
      (SIPADDR, SPORT), dispatcher)
  print("Serving on {}".format(server.server_address))
  print('Gathering data...')
  tstart = time()
  server.serve_forever()
