"""
Task 5 - Hashing & Grouping
Group anagrams together from a list of words.
"""


def group_anagrams(words: list[str]) -> list[list[str]]:
    """
    Group anagrams together from a list of words.
    
    Args:
        words: List of words to group
    
    Returns:
        List of groups, where each group contains anagrams
    """
    # Use sorted characters as key to group anagrams
    anagram_groups = {}
    
    for word in words:
        # Sort characters to create a key for anagrams
        key = "".join(sorted(word.lower()))
        
        # Check if key exists, create empty list if not
        if key not in anagram_groups:
            anagram_groups[key] = []
        
        anagram_groups[key].append(word)
    
    # Return list of groups
    return list(anagram_groups.values())
