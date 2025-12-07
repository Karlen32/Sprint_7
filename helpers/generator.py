from faker import Faker

fake = Faker()


def generate_courier_payload():
    return {
        "login": fake.user_name(),
        "password": fake.password(),
        "firstName": fake.first_name()
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
