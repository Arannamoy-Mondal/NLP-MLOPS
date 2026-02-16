from pydantic import Field,BaseModel

class BookModel:
    title:str
    author:str
    price:float
    rating:float
    def __init__(self,title,author,price,rating):
        self.title=title
        self.author=author
        self.price=price
        self.rating=rating
        
class BookRequest(BaseModel):
    title:str=Field(min_length=5,max_length=50)
    author:str=Field(min_length=5,max_length=100)
    price:float=Field(min=0,max=100)
    rating:float=Field(gt=0,lt=10)


