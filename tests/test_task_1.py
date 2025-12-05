"""
Tests for Task 1 - String & Collections
"""

from task_1 import most_common_word


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
    print("\nAll Task 1 tests passed!")
