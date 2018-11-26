"""Small example OSC server

This program listens to several addresses, and prints some information about
received packets.
"""
import sys
import numpy as np
import sys
from params import SIPADDR, CIPADDR
from sklearn.externals import joblib
from pyeeg import hurst
import warnings
import os


from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client

with warnings.catch_warnings():
    warnings.simplefilter("ignore")


if len(sys.argv) > 1:
    SUB = sys.argv[1]
    SPORT = int(sys.argv[2])
else:
    print("Need SUB and SPORT as arguments for the script")
    print("Default values are: SUB=S001, SPORT=5000")
    SUB = "S001"
    SPORT = 5000

CPORT = SPORT + 10
DATASTEP = 220
SAMP_FEAT_RATE = 5
WINDOW_SIZE = 10
COMPUTING = False
raw_data = None
count = 0


def feature_extraction(data):
    features = []
    for values in data.T:
        features.append(hurst(values))
    return features


def data_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    global raw_data, count, DATASTEP, COMPUTING
    raw_data = (
        np.asarray([ch1, ch2, ch3, ch4]).reshape((1, 4))
        if raw_data is None
        else np.concatenate(
            (raw_data, np.asarray([ch1, ch2, ch3, ch4]).reshape(1, -1)), axis=0
        )
    )
    count += 1
    if count >= SAMP_FEAT_RATE * DATASTEP and not COMPUTING:
        print("Computing features...")
        COMPUTING = True
        features = feature_extraction(raw_data[-WINDOW_SIZE * DATASTEP :])
        client.send_message("/hurst", features)
        COMPUTING = False
        print("Done")
        count = 0


if __name__ == "__main__":
    client = udp_client.SimpleUDPClient(CIPADDR, CPORT)

    R = np.array([], dtype=np.float32).reshape(0, 4)
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/muse/eeg", data_handler, R)

    server = osc_server.ThreadingOSCUDPServer((SIPADDR, SPORT), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
