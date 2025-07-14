def binary_search(arr: list[int], target: int) -> int:
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


# Example "search on answer space": minimum k where condition is True
def find_first_true(lo: int, hi: int, condition) -> int:
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if condition(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans
