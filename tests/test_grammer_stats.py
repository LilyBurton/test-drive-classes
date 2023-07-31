from lib.grammer_stats import *
import pytest

"""
Checking grammer,
returns True if the text contains a capital letter and an end of sentence punctuation.
Otherwise return False.
"""
"""
Boolean return True
"""
def test_grammer_check():
    grammer_stats = GrammerStats()
    result = grammer_stats.check("Hello!")
    assert result == True

"""
Return False if there's no capital letter
"""
def test_grammer_check_if_no_capital_letter():
    grammer_stats = GrammerStats()
    result = grammer_stats.check("hello!")
    assert result == False

"""
Return False if there's no punctuation at the end
"""
def test_grammer_check_if_no_punctuation():
    grammer_stats = GrammerStats()
    result = grammer_stats.check("Hello")
    assert result == False

"""
Return False if there's no capital letter or no punctuation
"""
def test_grammer_check_if_no_capital_letter_and_no_punctuation():
    grammer_stats = GrammerStats()
    result = grammer_stats.check("hello")
    assert result == False

"""
Return integer of the percentage of text checked, 100 = 100% if text is True
"""
def test_grammer_percentage():
    grammer_stats = GrammerStats()
    grammer_stats.check("Hello!")
    result = grammer_stats.percentage_good()
    assert result == 100

"""
Return integer 50 if the text has no capital letter or punctuation
"""
def test_grammer_percentage_if_no_capital_letter():
    grammer_stats = GrammerStats()
    grammer_stats.check("hello!")
    result = grammer_stats.percentage_good()
    assert result == 50

"""
Return integer 50 if the text has no punctuation
"""
def test_grammer_percentage_if_no_punctuation():
    grammer_stats = GrammerStats()
    grammer_stats.check("Hello")
    result = grammer_stats.percentage_good()
    assert result == 50

def test_grammer_percentage_if_no_punctuation_and_capital_letter():
    grammer_stats = GrammerStats()
    grammer_stats.check("hello")
    result = grammer_stats.percentage_good()
    assert result == 0

"""
Raises error if text is empty string
"""
def test_grammer_check_if_raises_error():
    grammer_stats = GrammerStats()
    with pytest.raises(Exception) as err:
        grammer_stats.check("")
        assert str(err.value) == "Cannot check without text"