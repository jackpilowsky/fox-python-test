"""
Task 1 - String & Collections
Find the most common word in a text, excluding stopwords.
"""


def most_common_word(text, stopwords=None):
    """
    Find the most common word in the given text, excluding stopwords.
    
    Args:
        text: The input text to analyze
        stopwords: Optional set of words to exclude from counting (case-insensitive)
    
    Returns:
        The most common word (lowercase), or None if no valid words found
    """
    if stopwords is None:
        stopwords = set()
    
    # Normalize stopwords to lowercase for case-insensitive comparison
    stopwords_lower = {word.lower() for word in stopwords}
    
    # Count word frequencies and track most common in a single pass
    word_counts = {}
    max_count = 0
    most_common = None
    
    for word in text.split():
        # Remove common punctuation from start and end
        cleaned = word.strip('.,!?;:"()[]{}').lower()
        # Only include non-empty words that aren't stopwords
        if cleaned and cleaned not in stopwords_lower:
            word_counts[cleaned] = word_counts.get(cleaned, 0) + 1
            if word_counts[cleaned] > max_count:
                max_count = word_counts[cleaned]
                most_common = cleaned
    
    return most_common
