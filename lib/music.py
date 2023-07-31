class MusicTracker:
    
    def __init__(self):
        self._list = []

    def add(self, track):
        if track == None:
            raise Exception("No music track")
        else:
            self._list.append(track)