from lib.diary_entry import *
import pytest

"""
Return a title and contents
"""

def test_diary_entry():
    diary_entry = DiaryEntry("My diary", "My life as a coder")
    result = diary_entry.format()
    assert result == "My diary: My life as a coder"

def test_counts_words_in_diary():
    diary_entry = DiaryEntry("My diary", "My life as a coder")
    result1 = diary_entry.count_words()
    assert result1 == 7

def test_reading_time_in_wpm():
    diary_entry = DiaryEntry("My diary", "My life as a coder")
    result = diary_entry.reading_time(5)
    assert result == 1

def test_reading_time_raise_error():
    diary_entry = DiaryEntry("My diary", "My life as a coder")
    with pytest.raises(Exception) as err:
        diary_entry.reading_time(0)
    assert str(err.value) == "Cannot calculate reading time with wpm 0."


def test_reading_chunk_in_minutes():
    diary_entry = DiaryEntry("My diary", "My life as a coder")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "My life"
    
def test_reading_chunk_in_3_words():
    diary_entry = DiaryEntry("My diary", "My life as a coder")
    result = diary_entry.reading_chunk(3, 1)
    assert result == "My life as"
    
