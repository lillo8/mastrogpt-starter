import os, requests as req
def test_reverse():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/dlillo/reverse"
    res = req.get(url).json()
    assert res.get("output").startswith("d")
    args = { "input": "Test"}
    res = req.post(url, json=args).json()
    assert res["output"] == "L'input al contrario è: **tseT**" 
