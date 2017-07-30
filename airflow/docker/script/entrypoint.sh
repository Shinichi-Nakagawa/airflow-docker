#!/usr/bin/env bash

CMD="airflow"
TRY_LOOP="20"
cd ${AIRFLOW_HOME}

# make airflow.cfg
python make_conf.py

# Database (init or reset)
if [ "$2" = "init" ]; then
  $CMD initdb
elif [ "$2" = "reset" ]; then
  $CMD resetdb -y
else
  echo "migration skip"
fi

# run to server
if [ "$1" = "webserver" ]; then
  exec $CMD webserver -p 8080
elif [ "$1" = "scheduler" ]; then
  exec $CMD scheduler -p
elif [ "$1" = "worker" ]; then
  exec $CMD worker -p
else
  $1
fi