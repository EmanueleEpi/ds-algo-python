from week_00_bootup.binary_search_utils import binary_search, find_first_true


def test_binary_search():
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 3) == 1
    assert binary_search(arr, 8) == -1


def test_find_first_true():
    condition = lambda x: x >= 5
    assert find_first_true(0, 10, condition) == 5
