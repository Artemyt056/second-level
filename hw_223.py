from peewee import *

db = SqliteDatabase('internet_shopt.db')


class Customer(Model):
    name = CharField()
    email = CharField(unique=True)

    class Meta:
        database = db


class Product(Model):
    name = CharField()
    price = DecimalField(max_digits=10, decimal_places=2)
    description = TextField()
    production_date = DateField()

    class Meta:
        database = db


class Seller(Model):
    name = CharField()
    email = CharField(unique=True)

    class Meta:
        database = db


class Purchase(Model):
    customer = ForeignKeyField(Customer, backref='purchases')
    product = ForeignKeyField(Product, backref='purchases')
    seller = ForeignKeyField(Seller, backref='sales')
    purchase_date = DateField()
    quantity = IntegerField()

    class Meta:
        database = db


db.connect()
db.create_tables([Customer, Product, Seller, Purchase])

Customer.create(name='Bob light', email='john@example.com')
Customer.create(name='Jane Lans', email='jane@example.com')
Customer.create(name='Alice Johnson', email='alice@example.com')
Customer.create(name='Leon ', email='bob@example.com')
Customer.create(name='Eva White', email='eva@example.com')

Product.create(name='Laptop', price=1200, description='High-performance laptop', production_date='2023-01-15')
Product.create(name='Smartphone', price=800, description='Flagship smartphone', production_date='2023-02-20')
Product.create(name='Tablet', price=500, description='Portable tablet', production_date='2023-03-10')
Product.create(name='TV_set', price=150, description='Wireless headphones', production_date='2023-04-05')
Product.create(name='Smartwatch', price=300, description='Fitness smartwatch', production_date='2023-05-20')

Seller.create(name='Electo Master', email='techstore@example.com')
Seller.create(name='Electronics World', email='electronics@example.com')
Seller.create(name='Gadget Shop', email='gadgetshop@example.com')
Seller.create(name='Mobile Hub', email='mobilehub@example.com')
Seller.create(name='Digital Solutions', email='digitalsol@example.com')

Purchase.create(customer=Customer.get(Customer.id == 1), product=Product.get(Product.id == 1),
                seller=Seller.get(Seller.id == 1), purchase_date='2023-01-20', quantity=2)
Purchase.create(customer=Customer.get(Customer.id == 2), product=Product.get(Product.id == 2),
                seller=Seller.get(Seller.id == 2), purchase_date='2023-02-25', quantity=1)
Purchase.create(customer=Customer.get(Customer.id == 3), product=Product.get(Product.id == 3),
                seller=Seller.get(Seller.id == 3), purchase_date='2023-03-30', quantity=3)
Purchase.create(customer=Customer.get(Customer.id == 4), product=Product.get(Product.id == 4),
                seller=Seller.get(Seller.id == 4), purchase_date='2023-04-10', quantity=1)
Purchase.create(customer=Customer.get(Customer.id == 5), product=Product.get(Product.id == 5),
                seller=Seller.get(Seller.id == 5), purchase_date='2023-05-15', quantity=2)

popular_product = Product.select(Product, fn.SUM(Purchase.quantity).alias('total_purchases')).join(Purchase,
                                                                                                   JOIN.LEFT_OUTER).group_by(
    Product).order_by(SQL('total_purchases').desc()).get()

print(popular_product.name)

most_expensive_product = Product.select().order_by(Product.price.desc()).get()
print(most_expensive_product.name)

newest_product = Product.select().order_by(Product.production_date.desc())
print(newest_product)