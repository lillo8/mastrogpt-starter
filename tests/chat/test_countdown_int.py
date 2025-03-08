import sys
import os, requests as req
sys.path.append("tests")
sys.path.append("packages/chat")
import streamock
import countdown

def test_countdown():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/chat/countdown"
    res = req.get(url).json()
    assert res.get("output").startswith("I")