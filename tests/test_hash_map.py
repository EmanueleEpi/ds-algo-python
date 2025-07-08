from week_00_bootup.hash_map import HashMap


def test_hash_map_basic():
    hm = HashMap()
    hm.put("a", 100)
    assert hm.get("a") == 100
    hm.put("a", 200)
    assert hm.get("a") == 200
    hm.put("b", 300)
    assert hm.get("b") == 300
    hm.remove("a")
    assert hm.get("a") is None
