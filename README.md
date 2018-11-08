# cocobrainchannel

## Introduction

CocoBrainChannel is a project that allows real-time musical exploration of mental states. To achieve this, we use brain-computer interfaces and mobile EEG.

## Instructions

### Get python ready

Install the python environment with the script "install_muse_ml.sh"

./install_muse_ml.sh

Or install the packages manually and run "test_env.py" to check if everyhtinh is working fine.
list of packages:
- sklearn
- python-osc
- numpy
- scipy
- xgboost

### Start the experience on someone

Start the "calibration.sh" script with the required arguments :
- Subject number (for file name if data is saved)
- path to save folder (if data is saved)
- Port to listen to to gather OSC data

exemple:
./calibration.sh S0001 data 2

Follow the instructions...
Have Fun!

## Credits

CocoLab (UdeM, Montreal, Quebec, CA).
Bellemare-Pepin Antoine,
Dehgan Arthur,
Harel Yann,
Saive Anne-Lise,
Jerbi Karim.

