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
    
    # Count word frequencies manually
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    # Find the most common word
    max_count = 0
    most_common = None
    for word, count in word_counts.items():
        if count > max_count:
            max_count = count
            most_common = word
    
    return most_common
