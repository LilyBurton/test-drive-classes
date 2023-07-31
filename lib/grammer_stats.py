class GrammerStats:

    def __init__(self):
        pass

    def check(self, text):
        self.text = text
        self.first_letter = text[0]
        self.last_letter = text[-1]
        self.punctuation = ".!?"
        if self.text == None:
            raise Exception("Cannot check without text")
        elif self.first_letter.isupper() and self.last_letter in self.punctuation:
            return True
        else:
            return False
        
    def percentage_good(self):
        is_good = self.check(self.text)
        if is_good:
            return 100
        elif self.first_letter.isupper() or self.last_letter in self.punctuation:
            return 50
        else:
            return 0
