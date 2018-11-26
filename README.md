# cocobrainchannel

## Introduction

CocoBrainChannel is a project that allows real-time musical exploration of mental states. To achieve this, we use brain-computer interfaces and mobile EEG.

## Instructions

#### Get python ready

Requires python 3.5+

Create the python environment with the script "install_muse_ml.sh"

./install_muse_ml.sh

Or install the packages manually and run "test_env.py" to check if everything is working fine.
list of packages:
- sklearn
- python-osc
- numpy
- scipy
- xgboost

#### Set some parameters

You will need to set the ip addresses in "params.py" with SIPADDR the broadcast address of your network and CIPADDR the IP of the machine  to which you send the OSC data (eg. machine learning predictions)
If you run everything on single machine, set both to "127.0.0.1"

#### Start the experience on someone

Start the "calibration.sh" script with the required arguments :
- Subject number (for file name if data is saved)
- Port to listen to to gather OSC data
- Duration of the calibration in seconds

exemple:
./calibration.sh S0001 5003 10

Follow the instructions...
Have Fun!

## Credits

CocoLab (UdeM, Montreal, Quebec, CA).  
Bellemare-Pepin Antoine,  
Dehgan Arthur,  
Harel Yann,  
Saive Anne-Lise,  
Jerbi Karim.  

