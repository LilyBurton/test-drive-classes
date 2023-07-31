class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
    

    def format(self):
        self.diary = f"{self.title}: " + f"{self.contents}"
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return f"{self.diary}"
        

    def count_words(self):
        diary_title = len(self.title.split())
        diary_contents = len(self.contents.split())
        return diary_title + diary_contents
        


    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("Cannot calculate reading time with wpm 0.")
        content_words = len(self.contents.split())
        return content_words / wpm
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        words_we_read = wpm * minutes
        words = self.contents.split()
        count_words = words[:words_we_read]
        return " ".join(count_words)

        return "My life"
        # Parameters
    #     #   wpm: an integer representing the number of words the user can read
    #     #        per minute
    #     #   minutes: an integer representing the number of minutes the user has
    #     #            to read
    #     # Returns:
    #     #   string: a chunk of the contents that the user could read in the
    #     #           given number of minutes
    #     #
    #     # If called again, `reading_chunk` should return the next chunk,
    #     # skipping what has already been read, until the contents is fully read.
    #     # The next call after that should restart from the beginning.
    #     pass