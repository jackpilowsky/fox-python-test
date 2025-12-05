"""
Task 4 - Debugging & Refactoring
Fixed Fibonacci implementations: recursive, iterative, and memoized.
"""

from typing import Optional


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
