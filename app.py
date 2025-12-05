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


"""
Task 2 - Data Structures & Algorithms
Merge overlapping intervals.
"""


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    Merge overlapping intervals.
    
    Args:
        intervals: List of intervals where each interval is [start, end]
    
    Returns:
        List of merged intervals, sorted by start time
    """
    if not intervals:
        return []
    
    # Sort intervals by start time
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    
    merged = [sorted_intervals[0]]
    
    for current in sorted_intervals[1:]:
        last_merged = merged[-1]
        
        # Check if current interval overlaps with the last merged interval
        if current[0] <= last_merged[1]:
            # Merge by extending the end time to the maximum
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # No overlap, add current interval to merged list
            merged.append(current)
    
    return merged


"""
Task 4 - Debugging & Refactoring
Fixed Fibonacci implementations: recursive, iterative, and memoized.
"""


def fib_recursive(n: int) -> int:
    """
    Calculate the nth Fibonacci number using recursion.
    Fixed version with proper base cases.
    
    Args:
        n: The position in the Fibonacci sequence (0-indexed)
    
    Returns:
        The nth Fibonacci number
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """
    Calculate the nth Fibonacci number using iteration.
    More efficient than recursive approach - O(n) time, O(1) space.
    
    Args:
        n: The position in the Fibonacci sequence (0-indexed)
    
    Returns:
        The nth Fibonacci number
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    
    # Use two variables to track previous two numbers
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr


def fib_memoized(n: int, memo: Optional[dict[int, int]] = None) -> int:
    """
    Calculate the nth Fibonacci number using memoization.
    Combines recursion with caching - O(n) time, O(n) space.
    
    Args:
        n: The position in the Fibonacci sequence (0-indexed)
        memo: Optional dictionary for caching results
    
    Returns:
        The nth Fibonacci number
    """
    if memo is None:
        memo = {}
    
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    
    # Check if result is already cached
    if n in memo:
        return memo[n]
    
    # Calculate and cache the result
    memo[n] = fib_memoized(n - 1, memo) + fib_memoized(n - 2, memo)
    return memo[n]
