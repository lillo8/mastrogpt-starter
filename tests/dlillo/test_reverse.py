import sys 
sys.path.append("packages/dlillo/reverse")
import reverse

def test_reverse():
    res = reverse.reverse({})
    assert res["output"] == "dammi un input che te lo rivolto io"
