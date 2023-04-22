import graphene
from graphene import ObjectType
# 如果使用 Django ORM 或 SQLAlchemy，可以導入相應的模型
# from myapp.models import User, Product

class UserType(ObjectType):
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()
    # 其他 User 模型相關的字段

class ProductType(ObjectType):
    id = graphene.Int()
    name = graphene.String()
    description = graphene.String()
    price = graphene.Float()
    # 其他 Product 模型相關的字段
