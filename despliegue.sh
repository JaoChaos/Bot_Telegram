#!/bin/bash

# Start the first process
gunicorn --config=config_gunicorn.py web:__hug_wsgi__ &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start my_first_process: $status"
  exit $status
else
  echo "Started correctly my_first_process"
fi

# Start the second process
python3 JaoChaosBot.py &

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
