"""
Main test runner for all tasks
"""

import sys
sys.path.insert(0, '.')

from tests import test_task_1, test_task_2, test_task_3, test_task_4, test_task_5


def run_all_tests():
    """Run all tests for all tasks"""
    
    print("=" * 60)
    print("TASK 1 - String & Collections")
    print("=" * 60)
    test_task_1.test_basic()
    test_task_1.test_with_stopwords()
    test_task_1.test_with_punctuation()
    test_task_1.test_empty_string()
    test_task_1.test_all_stopwords()
    test_task_1.test_complex_text()
    
    print("\n" + "=" * 60)
    print("TASK 2 - Data Structures & Algorithms")
    print("=" * 60)
    test_task_2.test_merge_basic()
    test_task_2.test_merge_all_overlapping()
    test_task_2.test_merge_no_overlap()
    test_task_2.test_merge_empty()
    test_task_2.test_merge_single()
    test_task_2.test_merge_unsorted()
    test_task_2.test_merge_touching()
    
    print("\n" + "=" * 60)
    print("TASK 3 - OOP Design & API")
    print("=" * 60)
    test_task_3.test_logger_basic()
    test_task_3.test_logger_levels()
    test_task_3.test_logger_search()
    test_task_3.test_logger_metadata()
    test_task_3.test_logger_limit()
    test_task_3.test_logger_api_simulation()
    test_task_3.test_logger_clear()
    
    print("\n" + "=" * 60)
    print("TASK 4 - Debugging & Refactoring")
    print("=" * 60)
    test_task_4.test_fib_base_cases()
    test_task_4.test_fib_small_values()
    test_task_4.test_fib_larger_value()
    test_task_4.test_fib_error_handling()
    test_task_4.test_fib_performance()
    
    print("\n" + "=" * 60)
    print("TASK 5 - Hashing & Grouping")
    print("=" * 60)
    test_task_5.test_group_anagrams_basic()
    test_task_5.test_group_anagrams_empty()
    test_task_5.test_group_anagrams_single()
    test_task_5.test_group_anagrams_no_matches()
    test_task_5.test_group_anagrams_case_insensitive()
    test_task_5.test_group_anagrams_duplicates()
    
    print("\n" + "=" * 60)
    print("ALL TESTS PASSED! ✓")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()
