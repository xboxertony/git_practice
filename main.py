import graphene
from graphene import ObjectType
from test import UserType, ProductType


class UserQuery(ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        # 示例用戶列表，實際情況下，您應該從數據庫或其他數據源獲取用戶數據
        users_data = [
            {
                "id": 1,
                "name": "Alice",
                "email": "alice@example.com"
            },
            {
                "id": 2,
                "name": "Bob",
                "email": "bob@example.com"
            },
        ]
        return [
            UserType(id=user["id"], name=user["name"], email=user["email"])
            for user in users_data
        ]


class ProductQuery(ObjectType):
    products = graphene.List(ProductType)

    def resolve_products(self, info):
        # 示例產品列表，實際情況下，您應該從數據庫或其他數據源獲取產品數據
        products_data = [
            {
                "id": 1,
                "name": "Product A",
                "description": "Description A",
                "price": 100.0
            },
            {
                "id": 2,
                "name": "Product B",
                "description": "Description B",
                "price": 200.0
            },
        ]
        return [
            ProductType(id=product["id"],
                        name=product["name"],
                        description=product["description"],
                        price=product["price"]) for product in products_data
        ]


class Query(UserQuery, ProductQuery, ObjectType):
    pass


schema = graphene.Schema(query=Query)

result = schema.execute('query {users{id},products{id,name}}')
print(result.data)
