"""
Tests for Task 5 - Hashing & Grouping
"""

from task_5 import group_anagrams


def test_group_anagrams_basic():
    """Test basic anagram grouping"""
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(words)
    
    # Convert to sets for comparison (order doesn't matter)
    result_sets = [set(group) for group in result]
    
    expected_groups = [
        {"eat", "tea", "ate"},
        {"tan", "nat"},
        {"bat"}
    ]
    
    assert len(result) == 3
    for expected in expected_groups:
        assert expected in result_sets
    
    print(f"Test group anagrams basic: {result}")


def test_group_anagrams_empty():
    """Test empty list"""
    result = group_anagrams([])
    assert result == []
    print("Test group anagrams empty: []")


def test_group_anagrams_single():
    """Test single word"""
    result = group_anagrams(["hello"])
    assert len(result) == 1
    assert result[0] == ["hello"]
    print("Test group anagrams single: [['hello']]")


def test_group_anagrams_no_matches():
    """Test words with no anagrams"""
    words = ["abc", "def", "ghi"]
    result = group_anagrams(words)
    assert len(result) == 3
    print(f"Test group anagrams no matches: {result}")


def test_group_anagrams_case_insensitive():
    """Test case insensitive grouping"""
    words = ["Listen", "Silent", "hello", "HELLO"]
    result = group_anagrams(words)
    
    result_sets = [set(group) for group in result]
    
    assert len(result) == 2
    assert {"Listen", "Silent"} in result_sets
    assert {"hello", "HELLO"} in result_sets
    
    print(f"Test group anagrams case insensitive: {result}")


def test_group_anagrams_duplicates():
    """Test with duplicate words"""
    words = ["cat", "tac", "cat", "act"]
    result = group_anagrams(words)
    
    assert len(result) == 1
    assert len(result[0]) == 4
    
    print(f"Test group anagrams duplicates: {result}")


if __name__ == "__main__":
    test_group_anagrams_basic()
    test_group_anagrams_empty()
    test_group_anagrams_single()
    test_group_anagrams_no_matches()
    test_group_anagrams_case_insensitive()
    test_group_anagrams_duplicates()
    print("\nAll Task 5 tests passed!")
