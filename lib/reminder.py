# EXAMPLE

class Reminder:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        self._name = name
        self._list = []
        

    def remind_me_to(self, task):
        self._task = task
    

    def add(self, task):
        self._list.append(task)

    def mark_complete(self, index):
        del self._list[index]



    def remind(self):
        if self._task == None:
            raise Exception("No task.")
        else:
            return f"{self._name}, {self._task}!"

        