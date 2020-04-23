#! /bin/bash
cd "$(dirname "$0")"
while true
do
printf "\n*** Starting Bot: Development ***\n\n"
python3 run.dev.py
printf "\n*** Bot has stopped! ***\n"
sleep 3
done