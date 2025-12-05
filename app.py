"""
Task 1 - String & Collections
Find the most common word in a text, excluding stopwords.
"""

from collections import Counter
from typing import Optional


def most_common_word(text: str, stopwords: Optional[set[str]] = None) -> Optional[str]:
    """
    Find the most common word in the given text, excluding stopwords.
    
    Args:
        text: The input text to analyze
        stopwords: Optional set of words to exclude from counting (case-insensitive)
    
    Returns:
        The most common word (lowercase), or None if no valid words found
    
    Examples:
        >>> most_common_word("Hello world hello")
        'hello'
        >>> most_common_word("The cat and the dog", {"the", "and"})
        'cat'
    """
    if stopwords is None:
        stopwords = set()
    
    # Normalize stopwords to lowercase for case-insensitive comparison
    stopwords_lower = {word.lower() for word in stopwords}
    
    # Extract words: split by whitespace and strip punctuation
    words = []
    for word in text.split():
        # Remove common punctuation from start and end
        cleaned = word.strip('.,!?;:"()[]{}').lower()
        # Only include non-empty words that aren't stopwords
        if cleaned and cleaned not in stopwords_lower:
            words.append(cleaned)
    
    # Return None if no valid words found
    if not words:
        return None
    
    # Count word frequencies and return the most common
    word_counts = Counter(words)
    most_common = word_counts.most_common(1)
    
    return most_common[0][0] if most_common else None
