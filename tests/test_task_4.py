"""
Tests for Task 4 - Debugging & Refactoring
"""

from task_4 import fib_recursive, fib_iterative, fib_memoized
import time


def test_fib_base_cases():
    """Test Fibonacci base cases"""
    # Test all three implementations
    for fib_func in [fib_recursive, fib_iterative, fib_memoized]:
        assert fib_func(0) == 0
        assert fib_func(1) == 1
    print("Test fib base cases: All implementations correct")


def test_fib_small_values():
    """Test Fibonacci with small values"""
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    
    for fib_func in [fib_recursive, fib_iterative, fib_memoized]:
        for i, exp in enumerate(expected):
            result = fib_func(i)
            assert result == exp, f"{fib_func.__name__}({i}) = {result}, expected {exp}"
    
    print(f"Test fib small values: All implementations match expected sequence")


def test_fib_larger_value():
    """Test Fibonacci with larger value (only iterative and memoized)"""
    n = 30
    expected = 832040
    
    # Recursive would be too slow for n=30
    result_iter = fib_iterative(n)
    result_memo = fib_memoized(n)
    
    assert result_iter == expected
    assert result_memo == expected
    print(f"Test fib larger value: fib({n}) = {expected}")


def test_fib_error_handling():
    """Test error handling for negative input"""
    for fib_func in [fib_recursive, fib_iterative, fib_memoized]:
        try:
            fib_func(-1)
            assert False, f"{fib_func.__name__} should raise ValueError for negative input"
        except ValueError:
            pass
    print("Test fib error handling: All implementations handle negative input correctly")


def test_fib_performance():
    """Compare performance of different implementations"""
    n = 20
    
    # Recursive (slower)
    start = time.time()
    result_rec = fib_recursive(n)
    time_rec = time.time() - start
    
    # Iterative (fast)
    start = time.time()
    result_iter = fib_iterative(n)
    time_iter = time.time() - start
    
    # Memoized (fast)
    start = time.time()
    result_memo = fib_memoized(n)
    time_memo = time.time() - start
    
    assert result_rec == result_iter == result_memo
    print(f"Test fib performance for n={n}:")
    print(f"  Recursive: {time_rec:.6f}s")
    print(f"  Iterative: {time_iter:.6f}s")
    print(f"  Memoized:  {time_memo:.6f}s")


if __name__ == "__main__":
    test_fib_base_cases()
    test_fib_small_values()
    test_fib_larger_value()
    test_fib_error_handling()
    test_fib_performance()
    print("\nAll Task 4 tests passed!")
