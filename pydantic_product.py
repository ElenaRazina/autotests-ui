from pydantic import BaseModel,Field

class Market(BaseModel):
    id: int
    name: str

class Product(BaseModel):
    name: str
    price: float=Field(...,ge=0, description="Цена должна быть больше 0")
    tags: list[str]=[]
    market: Market



product_data={
    "name": "Phone",
    "price": 499.99,
    "tags": ["electronics", "smartphone"],
    "market": {
        "id": 1,
        "name": "Ozon"
    }
}

product=Product(**product_data)
print(product.market.name)
print(product_data['market']['name'])

new_product=Product(
    name="Phone",
    price=499.99,
    tags=["electronics", "smartphone"],
    market=Market(id=1, name="Ozon")
)
print('new_product:',new_product)
