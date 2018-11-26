#! /bin/bash

# On recupere les arguments du script
subject=$1
length=$3
#path=$2
sport=$2
source "$(pwd)"/muse/bin/activate
clear
printf "Calibration utility\n"
#read -p "Press Any key to start calibration." -n1 -s
printf "\n"

read -p "Press Any key to start the first recording." -n1 -s
# le dernier argument est la duree de l'enregistrement en secondes
# l'avant dernier argument est la lettre utilisee pour identifier la condition
# cette lettre doit correspondre aux lettres dans calibration.py
printf "\n"
python save_gamma2mat.py $subject $sport n $length
printf "\n"
printf "done.\n"

printf "\n"

read -p "Press Any key to start the second recording." -n1 -s
printf "\n"
python save_gamma2mat.py $subject $sport s $length
printf "\n"
printf "done.\n"
printf "\n"

printf "training the classifier...\n"
# Dernier argument permet de specifier quelles lettres sont dans condition 1 et dans cond 2
# separees par un _ la condition a gauche du _ sera un 1 et l'autre un 0
python calibration.py $subject s_n
printf "\n"
wait

# combine raw mats to create the mat file to send to karim
python combine_mat.py $subject
read -p "Press Any key to start sending predictions" -n1 -s
# nohup python save_gamma2mat.py $subject $sport pred &>/dev/null
# blob=$!
printf "\n"
python prediction.py $subject $sport
# wait
# kill -9 $blob
