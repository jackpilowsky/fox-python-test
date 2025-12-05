"""
Task 5 - Hashing & Grouping
Group anagrams together from a list of words.
"""

from collections import defaultdict


def group_anagrams(words: list[str]) -> list[list[str]]:
    """
    Group anagrams together from a list of words.
    
    Args:
        words: List of words to group
    
    Returns:
        List of groups, where each group contains anagrams
    """
    # Use sorted characters as key to group anagrams
    anagram_groups = defaultdict(list)
    
    for word in words:
        # Sort characters to create a key for anagrams
        key = "".join(sorted(word.lower()))
        anagram_groups[key].append(word)
    
    # Return list of groups
    return list(anagram_groups.values())
