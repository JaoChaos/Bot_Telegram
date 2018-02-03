#!/bin/bash

# Start the first process
pip3 install -r requirements.txt

python ../web.py &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start my_first_process: $status"
  exit $status
else
  echo "Started correctly my_first_process"
fi

# Start the second process
python ../JaoChaosBot.py &

status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start my_second_process: $status"
  exit $status
else
  echo "Started correctly my_second_process"
fi

sleep 2

read -p "To exit press enter" answer
case ${answer:0:1} in
    * ) ;;
esac


kill -9 -$$
