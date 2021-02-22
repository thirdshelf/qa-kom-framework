import os
import json


current_path = os.path.dirname(os.path.abspath(__file__))
if os.environ.get("KOM_CONFIG_STRING"):
    kom_config = json.loads(os.environ.get("KOM_CONFIG_STRING"))
else:
    config_file = f'{current_path}/resources/.kom.config.json'
    kom_config = json.load(open(os.path.abspath(config_file)))

js_waiter_file = f'{current_path}/resources/.http.waiter.js'
