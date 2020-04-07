#!/bin/bash

echo "~~~~~~~~~~ Starting REST server ~~~~~~~~~~"
exec gunicorn app.server:init_app --config config/gunicorn_config.py --worker-class aiohttp.GunicornWebWorker
