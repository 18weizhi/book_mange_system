class BookType:
    # 主键id
    id = None
    # 图书类别名称
    bookTypeName = None
    # 图书类别描述
    bookTypeDesc = None

    def __init__(self, bookTypeName, bookTypeDesc):
        self.bookTypeName = bookTypeName
        self.bookTypeDesc = bookTypeDesc

    @classmethod
    def my_init(cls, id, bookTypeName, bookTypeDesc):
        cls.id = id
        return cls(bookTypeName, bookTypeDesc)