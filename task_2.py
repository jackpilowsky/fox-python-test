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
