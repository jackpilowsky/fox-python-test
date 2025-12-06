"""
Task 3 - OOP Design & API
Logger class implementation
"""

from enum import Enum
from datetime import datetime


class LogLevel(Enum):
    """Log level enumeration"""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class Logger:
    """Logger class for managing and querying logs"""
    
    def __init__(self, name):
        """Initialize logger with a name"""
        self.name = name
        self._logs = []
    
    def log(self, message, level, metadata=None):
        """
        Log a message with specified level and optional metadata
        
        Args:
            message: The log message
            level: LogLevel enum value
            metadata: Optional dictionary of additional data
        """
        log_entry = {
            "message": message,
            "level": level.value,
            "timestamp": datetime.now().isoformat(),
            "metadata": metadata or {}
        }
        self._logs.append(log_entry)
    
    def get_logs(self, level=None, limit=None):
        """
        Retrieve logs with optional filtering
        
        Args:
            level: Optional LogLevel to filter by
            limit: Optional maximum number of logs to return (most recent)
        
        Returns:
            List of log entries
        """
        logs = self._logs
        
        if level:
            logs = [log for log in logs if log["level"] == level.value]
        
        if limit:
            logs = logs[-limit:]
        
        return logs
    
    def search(self, query, case_sensitive=False):
        """
        Search logs by message content
        
        Args:
            query: Search string
            case_sensitive: Whether search should be case-sensitive
        
        Returns:
            List of matching log entries
        """
        if case_sensitive:
            return [log for log in self._logs if query in log["message"]]
        else:
            query_lower = query.lower()
            return [log for log in self._logs if query_lower in log["message"].lower()]
    
    def send_to_api(self, url):
        """
        Simulate sending logs to an API endpoint
        
        Args:
            url: API endpoint URL
        
        Returns:
            Dictionary with status and logs_sent count
        """
        return {
            "status": "success",
            "logs_sent": len(self._logs),
            "message": f"Sent {len(self._logs)} logs to {url}"
        }
    
    def clear(self):
        """Clear all logs"""
        self._logs = []
    
    def __len__(self):
        """Return number of logs"""
        return len(self._logs)
