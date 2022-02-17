#!/bin/sh

export FLASK_APP=app.py
export FLASK_ENV=development

IP=`ipconfig getifaddr en0`

flask run --host="$IP"