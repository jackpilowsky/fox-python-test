"""
Tests for Task 3 - OOP Design & API
"""

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
    test_logger_basic()
    test_logger_levels()
    test_logger_search()
    test_logger_metadata()
    test_logger_limit()
    test_logger_api_simulation()
    test_logger_clear()
    print("\nAll Task 3 tests passed!")
