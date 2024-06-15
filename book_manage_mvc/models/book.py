class Book():
    # 图书id
    id = None
    # 图书名字
    bookName = None
    # 作者名字
    author = None
    # 性别
    sex = None
    # 图书价格
    price = None
    # 图书类型id
    bookTypeId = None
    # 图书描述
    bookDesc = None

    def __init__(self, bookName, author, bookTypeId):
        self.bookName = bookName
        self.author = author
        self.bookTypeId = bookTypeId

    @classmethod
    def myinit(cls,bookName, author, sex, price, bookTypeId, bookDesc):
        book = Book(bookName, author, bookTypeId)
        book.sex = sex
        book.bookTypeId = bookTypeId
        book.bookDesc = bookDesc
        return book

    @classmethod
    def myinit2(cls, id, bookName, author, sex, price, bookTypeId, bookDesc):
        book = Book(bookName, author, bookTypeId)
        book.sex = sex
        book.price = price
        book.bookDesc = bookDesc
        book.id = id
        return book

    def add_book(self):
        pass

    def update_book(self):
        pass

    def del_book(self):
        pass