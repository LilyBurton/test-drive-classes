As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

Input track titles and add them to a list. 
self._list = []
class MusicTracker:

def __init__(self):
    self._list = []
    

def add(self, track):
    if self.track == None:
        raise Error
    else:
        self._list.append(self.track)

