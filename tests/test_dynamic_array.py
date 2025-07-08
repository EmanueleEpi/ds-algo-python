from week_00_bootup.dynamic_array import DynamicArray


def test_dynamic_array_append():
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    arr.append(3)
    assert len(arr) == 3
    assert arr[0] == 1
    assert arr[1] == 2
    assert arr[2] == 3
