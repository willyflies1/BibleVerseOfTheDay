class Verse(object):
    """ This will be the template for each bible verse """

    # Example should look John 3:16, Book chapter:verse
    quote = ""          # holds the actual verse
    book = ""           # what book of the bible quote is located
    chapter = None      # Number chapter quote is located
    verse = None        # Number verse the quote is located

    def __init__(self, book, chapter, verse, quote=None):
        self.book = book
        self.chapter = chapter
        self.verse = verse
        self.quote = quote

    def __str__(self):
        return '{} {}:{}, \"{}\"'.format(self.book, self.chapter, self.verse, self.quote)

    def getVerseInfo(self):
        return '{} {}:{}'.format(self.book, self.chapter, self.verse)

