#! /bin/bash
clear
printf "Welcome to the muse ml python installation script\n"
printf "The script will create a new python environment called 'muse'\n"
printf "install the necessary packages, run tests and create a command alias\n"
printf "for you to easily activate the muse environment.\n"
read -p "Press any key when you are ready (make sure you are connected to internet)." -n1 -s
printf "\n"

python -m venv muse
echo 'alias muse="source '"$(pwd)"'/muse/bin/activate"' >> ~/.bashrc

source ./muse/bin/activate
wait

printf "installing python packages... it will take a few minutes\n"
pip install sklearn python-osc numpy scipy xgboost &>/dev/null
printf "done.\n"
wait

printf "Testing the python environment.\n"
python test_env.py
wait

printf "it's all good, activate the environment by typing 'muse'\n"
deactivate 
