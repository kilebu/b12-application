import json
import hmac
import hashlib
import requests
from datetime import datetime, timezone
import os

payload = {
    "action_run_link": os.environ["ACTION_RUN_LINK"],
    "email": "calebchunguli22@gmail.com",
    "name": "Caleb Chunguli",
    "repository_link": "https://github.com/kilebu/b12-application",
    "resume_link": "https://www.linkedin.com/in/caleb-chunguli-b00997247/",
    "timestamp": datetime.now(timezone.utc)
        .isoformat(timespec="milliseconds")
        .replace("+00:00", "Z")
}

body = json.dumps(
    payload,
    separators=(",", ":"),
    sort_keys=True
).encode("utf-8")

secret = b"hello-there-from-b12"

signature = hmac.new(
    secret,
    body,
    hashlib.sha256
).hexdigest()

headers = {
    "Content-Type": "application/json",
    "X-Signature-256": f"sha256={signature}"
}

response = requests.post(
    "https://b12.io/apply/submission",
    data=body,
    headers=headers
)

response.raise_for_status()

result = response.json()

print("Receipt:", result["receipt"])
