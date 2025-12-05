"""
Tests for Task 2 - Data Structures & Algorithms
"""

from task_2 import merge_intervals


def test_merge_basic():
    """Test basic interval merging"""
    result = merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])
    print(f"Test merge basic: {result}")
    assert result == [[1, 6], [8, 10], [15, 18]]


def test_merge_all_overlapping():
    """Test when all intervals overlap"""
    result = merge_intervals([[1, 4], [2, 5], [3, 6]])
    print(f"Test merge all overlapping: {result}")
    assert result == [[1, 6]]


def test_merge_no_overlap():
    """Test when no intervals overlap"""
    result = merge_intervals([[1, 2], [3, 4], [5, 6]])
    print(f"Test merge no overlap: {result}")
    assert result == [[1, 2], [3, 4], [5, 6]]


def test_merge_empty():
    """Test empty list"""
    result = merge_intervals([])
    print(f"Test merge empty: {result}")
    assert result == []


def test_merge_single():
    """Test single interval"""
    result = merge_intervals([[1, 5]])
    print(f"Test merge single: {result}")
    assert result == [[1, 5]]


def test_merge_unsorted():
    """Test unsorted intervals"""
    result = merge_intervals([[8, 10], [1, 3], [2, 6], [15, 18]])
    print(f"Test merge unsorted: {result}")
    assert result == [[1, 6], [8, 10], [15, 18]]


def test_merge_touching():
    """Test intervals that touch at boundaries"""
    result = merge_intervals([[1, 3], [3, 5], [5, 7]])
    print(f"Test merge touching: {result}")
    assert result == [[1, 7]]


if __name__ == "__main__":
    test_merge_basic()
    test_merge_all_overlapping()
    test_merge_no_overlap()
    test_merge_empty()
    test_merge_single()
    test_merge_unsorted()
    test_merge_touching()
    print("\nAll Task 2 tests passed!")
