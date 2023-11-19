from peewee import SqliteDatabase, Model, IntegerField, CharField, IntegrityError
from contextlib import contextmanager
from time import perf_counter

db = SqliteDatabase('my_database.db')

class User(Model):
    id = IntegerField(primary_key=True)
    name = CharField()

    class Meta:
        database = db

db.connect()
db.create_tables([User], safe=True)

class DatabaseTransaction:
    def __enter__(self):
        self.db = db
        self.db.begin()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.db.rollback()  # Wycofanie zmian w przypadku wyjątku
        else:
            self.db.commit()  # Zatwierdzenie zmian

def upsert_user(id: int, name: str) -> None:
    try:
        User.create(id=id, name=name)
    except IntegrityError as e:
        print(f"A user with id {id} already exists")
        user = User.get(id=id)
        user.name = name
        user.save()

@contextmanager
def measure_transaction_perf():
    start = perf_counter()
    try:
        yield
    finally:
        print(f"transaction took {perf_counter() - start}s")

with measure_transaction_perf(), DatabaseTransaction():
    upsert_user(id=1, name="Alice")
    upsert_user(id=2, name="Bob")

for user in User.select():
    print(f"User ID: {user.id}, Name: {user.name}")

db.close()
