from pydantic import BaseModel


class ProductRequestSchema(BaseModel):
    category: str
    name: str
    image: str
    description_long: str


class ProductResponseSchema(ProductRequestSchema):
    id: int

    class Config():
        orm_mode = True
