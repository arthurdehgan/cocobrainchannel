# CoCo Brain Channel

## Send Muse data to puredata :
1. Install MuseDirect (Windaube10 only)

2. Pair Muse headband and activate headband in MuseDirect

3. Add new OSC output to an UDP port (e.g. 5091) add check all EEG features. Activate sending to this port

4. Run cmd.exe

5. Run the following command :
```muse-player -l udp:5091 -s osc.udp://localhost:5001```

## Run cbc_harmonizer :
1. Install Pure data 

2. Add the following librairies to your pd path :
- Cyclone
- list-abs
- mrpeach
- iemlib

3. Add cbc_objects to your pd path

## Use cbc_harmonizer :
1. Open the cbc_harmonizer patch and activate the DSP

2. Before doing anything, on the main patch, click the checkbox right above the "s bellson" box near the top right corner (to prevent a bug with the bells module)

3. When the subject is seated and the setup is connected, start the baseline recording by clicking the corresponding button in the top right corner

4. You can allocate different parameters to different EEG headbands by selecting one of the five boxes wherever they are available (0 = not routed)

5. When the baseline is computed, the generative algorithm automatically starts to be modulated by the EEG signal (if correctly routed)

# Python

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

