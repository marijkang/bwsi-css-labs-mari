import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_normal():
    assert max_subarray_sum([1]) == 1                       # single element
    assert max_subarray_sum([5, 4, -1, 7, 8]) == 23         # just regular test
    assert max_subarray_sum([1, -2, 3, -2]) == 3            # positives and negatives, answer is single positive

def test_all_negative():
    assert max_subarray_sum([-1, -2, -3, -4]) == -1         # all negatives, answer must be single negative

def test_has_zero():
    assert max_subarray_sum([0, -2, 3, -2, 2]) == 3         # has zero
    assert max_subarray_sum([1, -2, 0, 3]) == 3             # has zero
    assert max_subarray_sum([0, 1, 0]) == 1                 # all combinations have same result

if __name__ == "__main__":
    pytest.main()