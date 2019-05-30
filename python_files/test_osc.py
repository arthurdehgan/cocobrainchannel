"""Small example OSC server

This program listens to several addresses, and prints some information about
received packets.
"""
import sys
import numpy as np
from scipy.io import savemat
import sys
from sklearn.externals import joblib
import warnings
import os
warnings.filterwarnings("ignore")


from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client


first = True
PATH = 'data/'
raw_data = []
DATALEN = 1100
DATASTEP = 220
SPORT = 5001
CPORT = SPORT + 10
SIPADDR = '127.0.0.1'

def rhandler(unused_addr, args, delta, theta, alpha, beta, gamma):
    print(delta, theta, alpha, beta, gamma)


if __name__ == "__main__":

  R = np.array([]).reshape(0,5)
  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/muse/elements/", rhandler, R)

  server = osc_server.ThreadingOSCUDPServer(
      (SIPADDR, SPORT), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()
