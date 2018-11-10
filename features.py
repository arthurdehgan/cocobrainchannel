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
from pyeeg import hurst
import warnings
import os

warnings.filterwarnings("ignore")


from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client


if len(sys.argv) > 1:
    SUB = sys.argv[1]
    SPORT = int(sys.argv[2])
else:
    print("Need SUB and SPORT as arguments for the script")
    print("Default values are: SUB=S001, SPORT=5000")
    SUB = "S001"
    SPORT = 5000

CPORT = SPORT + 10
PATH = "data/"
raw_data = []
DATASTEP = 220
FILENAME = PATH + SUB + "_raw_pred.mat"
SAMP_FEAT_RATE = 2
WINDOW_SIZE = 10
count = 0
raw_data = None


def compute_feature(data):
    features = []
    for values in data.T:
        features.append(hurst(values))
    return features


def rhandler(unused_addr, args, ch1, ch2, ch3, ch4):
    global raw_data, count, DATASTEP
    raw_data = (
        np.asarray([ch1, ch2, ch3, ch4]).reshape((1, 4))
        if raw_data is None
        else np.concatenate(
            (raw_data, np.asarray([ch1, ch2, ch3, ch4]).reshape(1, -1)), axis=0
        )
    )
    count += 1
    if count >= SAMP_FEAT_RATE * DATASTEP:
        print(compute_feature(raw_data[-WINDOW_SIZE * DATASTEP :]))
        count = 0


if __name__ == "__main__":
    client = udp_client.SimpleUDPClient(CIPADDR, CPORT)

    baseline = []
    L = np.array([]).reshape(0, 4)
    R = np.array([]).reshape(0, 4)
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/muse/eeg", rhandler, R)

    server = osc_server.ThreadingOSCUDPServer((SIPADDR, SPORT), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
