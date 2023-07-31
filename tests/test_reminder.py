from lib.reminder import *
import pytest

def test_to_add_tasks_to_the_list():
    reminder = Reminder("Lily")
    reminder.add("Feed the cat")
    reminder.add("Walk the dog")
    reminder.add("Milk the cow")
    
def test_to_mark_down_from_list():
    reminder = Reminder("Lily")
    reminder.add("Feed the cat")
    reminder.add("Walk the dog")
    reminder.add("Milk the cow")
    reminder.mark_complete(1)
    

def test_remind_me_to_do_the_task():
    reminder = Reminder("Lily")
    reminder.remind_me_to("Feed the cat")
    assert reminder.remind() == "Lily, Feed the cat!"

def test_remind_me_error():
    reminder = Reminder("Lily")
    with pytest.raises(Exception) as err:
        reminder.remind_me_to("")
        assert str(err.value) == "No task."