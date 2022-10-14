class Book:
    def __init__(self,t,a,pub,pri,c=0):
        self.title = t
        self.author = a
        self.publisher = pub
        self.price = pri
        self.copies = c

    # title
    def getTitle(self):
        return self._title
    def setTitle(self,t):
        self._title = t
        return
    title = property(getTitle, setTitle)

    # author
    def getAuthor(self):
        return self._author
    def setAuthor(self,a):
        self._author = a
        return
    author = property(getAuthor, setAuthor)
    
    # publisher
    def getPublisher(self):
        return self._publisher
    def setPublisher(self,pub):
        self._publisher = pub
        return
    publisher = property(getPublisher, setPublisher)
    
    # price
    def getPrice(self):
        return self._price
    def setPrice(self,pri):
        self._price = pri
        return
    price = property(getPrice, setPrice)
    
    # copies
    def getCopies(self):
        return self._copies
    def setCopies(self,c):
        self._copies = c
        return
    copies = property(getCopies, setCopies)

    # ROYALTY
    def getRoyalty(self):
        if self.copies <= 500:
            self._royalty = (self.copies)*(self.price)*(10/100)
        elif self._copies <= 1000:
            self._royalty = 500*(self.price)*(10/100) + \
                           (self.copies-500)*(self.price)*(12.5/100)
        else:
            self._royalty = 500*(self.price)*(10/100) + \
                           500*(self.price)*(12.5/100) + \
                           (self.copies-1000)*(self.price)*(15/100)
        return self._royalty

class Ebook(Book):
    def __init__(self,t,a,pub,pri,c=0,f=None):
        super().__init__(t,a,pub,pri,c)
        self.format=f

    # E-Book format
    def getFormat(self):
        return self._format
    def setFormat(self,f):
        self._format = f
        return
    format = property(getFormat, setFormat)

    # override: getRoyalty
    # deduct GST on E-Books
    def getRoyalty(self):
        r = super().getRoyalty() # fetching from parent
        r = r - (r*12/100)   # deduct GST:12%
        self._royalty = r
        return self._royalty

if __name__ == "__main__":
    
    print("BOOK EXAMPLE\n")
    b1 = Book("Mathilda","Roadl Dalh","XOXO",100,600)
    print("Title: ",b1.getTitle())
    print("Author: ",b1.getAuthor())
    print("Publication: ",b1.getPublisher())
    print("Price: ",b1.getPrice())
    print("Copies: ",b1.getCopies())
    print("Royalty Earned: ",b1.getRoyalty())

    print("\nE-BOOK EXAMPLE\n")
    e1 = Ebook("Princess Diaries","Meg Cabot","yzyz",100,600,"pdf")
    e1.title = "Broklin 99"     # chaning title of book: property - set
    print(e1.getTitle())        # print using function
    print(e1.author)            # print directly using: property - get
    print("Royalty Earned: ",e1.getRoyalty())
    
