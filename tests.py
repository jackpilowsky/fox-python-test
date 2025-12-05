"""
Tests for most_common_word function
"""

from app import most_common_word


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
    
    print("\nAll tests passed!")



# Task 2 - Data Structures & Algorithms Tests
from app import merge_intervals


def test_merge_basic():
    """Test basic interval merging"""
    result = merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])
    print(f"Test merge basic: {result}")
    assert result == [[1, 6], [8, 10], [15, 18]]


def test_merge_all_overlapping():
    """Test when all intervals overlap"""
    result = merge_intervals([[1, 4], [2, 5], [3, 6]])
    print(f"Test merge all overlapping: {result}")
    assert result == [[1, 6]]


def test_merge_no_overlap():
    """Test when no intervals overlap"""
    result = merge_intervals([[1, 2], [3, 4], [5, 6]])
    print(f"Test merge no overlap: {result}")
    assert result == [[1, 2], [3, 4], [5, 6]]


def test_merge_empty():
    """Test empty list"""
    result = merge_intervals([])
    print(f"Test merge empty: {result}")
    assert result == []


def test_merge_single():
    """Test single interval"""
    result = merge_intervals([[1, 5]])
    print(f"Test merge single: {result}")
    assert result == [[1, 5]]


def test_merge_unsorted():
    """Test unsorted intervals"""
    result = merge_intervals([[8, 10], [1, 3], [2, 6], [15, 18]])
    print(f"Test merge unsorted: {result}")
    assert result == [[1, 6], [8, 10], [15, 18]]


def test_merge_touching():
    """Test intervals that touch at boundaries"""
    result = merge_intervals([[1, 3], [3, 5], [5, 7]])
    print(f"Test merge touching: {result}")
    assert result == [[1, 7]]


if __name__ == "__main__":
    # Task 1 tests
    test_basic()
    test_with_stopwords()
    test_with_punctuation()
    test_empty_string()
    test_all_stopwords()
    test_complex_text()
    
    print("\n--- Task 2 Tests ---")
    # Task 2 tests
    test_merge_basic()
    test_merge_all_overlapping()
    test_merge_no_overlap()
    test_merge_empty()
    test_merge_single()
    test_merge_unsorted()
    test_merge_touching()
    
    print("\nAll tests passed!")



# Task 3 - OOP Design & API Tests
from logger import Logger, LogLevel


def test_logger_basic():
    """Test basic logging functionality"""
    logger = Logger("test_logger")
    logger.log("Test message", LogLevel.INFO)
    
    logs = logger.get_logs()
    print(f"Test logger basic: {len(logs)} log(s)")
    assert len(logs) == 1
    assert logs[0]["message"] == "Test message"
    assert logs[0]["level"] == "INFO"


def test_logger_levels():
    """Test different log levels"""
    logger = Logger("test_logger")
    logger.log("Debug message", LogLevel.DEBUG)
    logger.log("Info message", LogLevel.INFO)
    logger.log("Warning message", LogLevel.WARNING)
    logger.log("Error message", LogLevel.ERROR)
    
    # Get all logs
    all_logs = logger.get_logs()
    print(f"Test logger levels: {len(all_logs)} total logs")
    assert len(all_logs) == 4
    
    # Filter by level
    error_logs = logger.get_logs(level=LogLevel.ERROR)
    print(f"Test logger levels: {len(error_logs)} error log(s)")
    assert len(error_logs) == 1
    assert error_logs[0]["level"] == "ERROR"


def test_logger_search():
    """Test log search functionality"""
    logger = Logger("test_logger")
    logger.log("User login successful", LogLevel.INFO)
    logger.log("Database connection failed", LogLevel.ERROR)
    logger.log("User logout", LogLevel.INFO)
    
    # Search for "user"
    results = logger.search("user")
    print(f"Test logger search: Found {len(results)} result(s) for 'user'")
    assert len(results) == 2
    
    # Case-sensitive search
    results_case = logger.search("User", case_sensitive=True)
    print(f"Test logger search: Found {len(results_case)} result(s) for 'User' (case-sensitive)")
    assert len(results_case) == 2


def test_logger_metadata():
    """Test logging with metadata"""
    logger = Logger("test_logger")
    logger.log("API request", LogLevel.INFO, metadata={"endpoint": "/api/users", "method": "GET"})
    
    logs = logger.get_logs()
    print(f"Test logger metadata: {logs[0]['metadata']}")
    assert logs[0]["metadata"]["endpoint"] == "/api/users"
    assert logs[0]["metadata"]["method"] == "GET"


def test_logger_limit():
    """Test log retrieval with limit"""
    logger = Logger("test_logger")
    for i in range(10):
        logger.log(f"Message {i}", LogLevel.INFO)
    
    # Get last 3 logs
    recent_logs = logger.get_logs(limit=3)
    print(f"Test logger limit: Retrieved {len(recent_logs)} recent logs")
    assert len(recent_logs) == 3
    assert recent_logs[-1]["message"] == "Message 9"


def test_logger_api_simulation():
    """Test API sending simulation"""
    logger = Logger("test_logger")
    logger.log("Test log 1", LogLevel.INFO)
    logger.log("Test log 2", LogLevel.ERROR)
    
    response = logger.send_to_api("https://api.example.com/logs")
    print(f"Test logger API: {response['message']}")
    assert response["status"] == "success"
    assert response["logs_sent"] == 2


def test_logger_clear():
    """Test clearing logs"""
    logger = Logger("test_logger")
    logger.log("Message 1", LogLevel.INFO)
    logger.log("Message 2", LogLevel.INFO)
    
    assert len(logger) == 2
    
    logger.clear()
    print(f"Test logger clear: {len(logger)} logs after clear")
    assert len(logger) == 0


if __name__ == "__main__":
    # Task 1 tests
    test_basic()
    test_with_stopwords()
    test_with_punctuation()
    test_empty_string()
    test_all_stopwords()
    test_complex_text()
    
    print("\n--- Task 2 Tests ---")
    # Task 2 tests
    test_merge_basic()
    test_merge_all_overlapping()
    test_merge_no_overlap()
    test_merge_empty()
    test_merge_single()
    test_merge_unsorted()
    test_merge_touching()
    
    print("\n--- Task 3 Tests ---")
    # Task 3 tests
    test_logger_basic()
    test_logger_levels()
    test_logger_search()
    test_logger_metadata()
    test_logger_limit()
    test_logger_api_simulation()
    test_logger_clear()
    
    print("\nAll tests passed!")



# Task 4 - Debugging & Refactoring Tests
from app import fib_recursive, fib_iterative, fib_memoized
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
    # Task 1 tests
    test_basic()
    test_with_stopwords()
    test_with_punctuation()
    test_empty_string()
    test_all_stopwords()
    test_complex_text()
    
    print("\n--- Task 2 Tests ---")
    # Task 2 tests
    test_merge_basic()
    test_merge_all_overlapping()
    test_merge_no_overlap()
    test_merge_empty()
    test_merge_single()
    test_merge_unsorted()
    test_merge_touching()
    
    print("\n--- Task 3 Tests ---")
    # Task 3 tests
    test_logger_basic()
    test_logger_levels()
    test_logger_search()
    test_logger_metadata()
    test_logger_limit()
    test_logger_api_simulation()
    test_logger_clear()
    
    print("\n--- Task 4 Tests ---")
    # Task 4 tests
    test_fib_base_cases()
    test_fib_small_values()
    test_fib_larger_value()
    test_fib_error_handling()
    test_fib_performance()
    
    print("\nAll tests passed!")
