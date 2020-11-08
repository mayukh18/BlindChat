import os
import json
import config
import requests

class Analytics:
    def __init__(self):
        self.token = os.environ.get('CHATMETRICS_TOKEN', config.CHATMETRICS_TOKEN)

    def record(self, entry):
        try:
            data = {"object":"page"}
            data["entry"] = entry
            r = requests.post(url="https://api.chatbottle.co/v2/updates/messenger/"+self.token+"/", data=json.dumps(data))
            print("analytics result", r.json(), data)
        except Exception as e:
            print("ANALYTICS ERROR", str(e))


