
import requests
import os
import json
data={"text":"hey"}
webhook="https://hooks.slack.com/services/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"
requests.post(webhook,json.dumps(data))
