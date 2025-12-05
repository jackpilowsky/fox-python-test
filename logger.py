"""
Logger class for Task 3 - OOP Design & API
"""

from datetime import datetime
from enum import Enum
from typing import Optional


class LogLevel(Enum):
    """Log level enumeration"""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class Logger:
    """
    A simple logger class that stores logs in memory and provides search functionality.
    Can be extended to send logs to external APIs.
    """
    
    def __init__(self, name: str = "default"):
        """
        Initialize the logger.
        
        Args:
            name: Name identifier for this logger instance
        """
        self.name = name
        self._logs: list[dict] = []
    
    def log(self, message: str, level: LogLevel = LogLevel.INFO, metadata: Optional[dict] = None) -> None:
        """
        Log a message with specified level and optional metadata.
        
        Args:
            message: The log message
            level: Log level (DEBUG, INFO, WARNING, ERROR)
            metadata: Optional dictionary of additional data
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "level": level.value,
            "message": message,
            "logger": self.name,
            "metadata": metadata or {}
        }
        self._logs.append(log_entry)
    
    def get_logs(self, level: Optional[LogLevel] = None, limit: Optional[int] = None) -> list[dict]:
        """
        Retrieve logs, optionally filtered by level.
        
        Args:
            level: Optional log level to filter by
            limit: Optional maximum number of logs to return (most recent first)
        
        Returns:
            List of log entries
        """
        logs = self._logs
        
        # Filter by level if specified
        if level:
            logs = [log for log in logs if log["level"] == level.value]
        
        # Apply limit if specified (return most recent)
        if limit:
            logs = logs[-limit:]
        
        return logs
    
    def search(self, query: str, case_sensitive: bool = False) -> list[dict]:
        """
        Search logs by message content.
        
        Args:
            query: Search string to find in log messages
            case_sensitive: Whether search should be case-sensitive
        
        Returns:
            List of log entries matching the query
        """
        results = []
        
        for log in self._logs:
            message = log["message"]
            search_message = message if case_sensitive else message.lower()
            search_query = query if case_sensitive else query.lower()
            
            if search_query in search_message:
                results.append(log)
        
        return results
    
    def send_to_api(self, api_url: str) -> dict:
        """
        Simulate sending logs to an external API.
        In a real implementation, this would use requests library.
        
        Args:
            api_url: The API endpoint URL
        
        Returns:
            Simulated API response
        """
        # Dummy API simulation
        return {
            "status": "success",
            "message": f"Sent {len(self._logs)} logs to {api_url}",
            "logs_sent": len(self._logs),
            "timestamp": datetime.now().isoformat()
        }
    
    def clear(self) -> None:
        """Clear all logs from memory"""
        self._logs.clear()
    
    def __len__(self) -> int:
        """Return the number of logs stored"""
        return len(self._logs)
