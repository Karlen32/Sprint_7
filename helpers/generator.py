from faker import Faker
import uuid
fake = Faker()


def generate_courier_payload():
    uniq = uuid.uuid4().hex[:6]
    return {
        "login": f"user_{uniq}",
        "password": "password123",
        "firstName": "Test"
    }


def generate_order_payload(colors=None):
    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": 1,
        "phone": fake.phone_number(),
        "rentTime": 3,
        "deliveryDate": "2025-12-01",
        "comment": "test",
        "color": colors if colors is not None else []
    }
