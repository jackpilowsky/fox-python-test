"""
Tests for most_common_word function
"""

from app import most_common_word


def test_basic():
    """Test basic word counting"""
    result = most_common_word("Hello world hello")
    print(f"Test basic: {result}")
    assert result == "hello"


def test_with_stopwords():
    """Test with stopwords filtering"""
    result = most_common_word("The cat and the dog", {"the", "and"})
    print(f"Test with stopwords: {result}")
    assert result in ["cat", "dog"]


def test_with_punctuation():
    """Test punctuation removal"""
    result = most_common_word("Hello, hello! World.")
    print(f"Test with punctuation: {result}")
    assert result == "hello"


def test_empty_string():
    """Test empty string returns None"""
    result = most_common_word("")
    print(f"Test empty string: {result}")
    assert result is None


def test_all_stopwords():
    """Test when all words are stopwords"""
    result = most_common_word("the and or", {"the", "and", "or"})
    print(f"Test all stopwords: {result}")
    assert result is None


def test_complex_text():
    """Test with more complex text"""
    text = "The quick brown fox jumps over the lazy dog. The fox is quick."
    stopwords = {"the", "is", "over"}
    result = most_common_word(text, stopwords)
    print(f"Test complex text: {result}")
    assert result in ["quick", "fox"]


if __name__ == "__main__":
    test_basic()
    test_with_stopwords()
    test_with_punctuation()
    test_empty_string()
    test_all_stopwords()
    test_complex_text()
    
    print("\nAll tests passed!")



# Task 2 - Data Structures & Algorithms Tests
from app import merge_intervals


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
    # Task 1 tests
    test_basic()
    test_with_stopwords()
    test_with_punctuation()
    test_empty_string()
    test_all_stopwords()
    test_complex_text()
    
    print("\n--- Task 2 Tests ---")
    # Task 2 tests
    test_merge_basic()
    test_merge_all_overlapping()
    test_merge_no_overlap()
    test_merge_empty()
    test_merge_single()
    test_merge_unsorted()
    test_merge_touching()
    
    print("\nAll tests passed!")
