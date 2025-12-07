from helpers.generator import generate_courier_payload
from faker import Faker

fake = Faker()


class TestCreateCourier:

    def test_create_courier_success(self, api):
        payload = generate_courier_payload()

        response = api.create_courier(payload)
        assert response.status_code == 201
        assert response.json().get("ok") is True

        login_resp = api.login_courier(payload["login"], payload["password"])
        assert login_resp.status_code == 200
        assert "id" in login_resp.json()

        api.delete_courier(login_resp.json()["id"])

    def test_cannot_create_two_identical_couriers(self, courier, api):
        duplicate_payload = {
            "login": courier["login"],
            "password": fake.password(),
            "firstName": fake.first_name()
        }

        response = api.create_courier(duplicate_payload)

        assert response.status_code == 409
        assert response.json().get("message") == "Этот логин уже используется"

    def test_create_courier_without_login_fails(self, api):
        payload = generate_courier_payload()
        payload.pop("login")

        response = api.create_courier(payload)

        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для создания учетной записи"

    def test_create_courier_without_password_fails(self, api):
        payload = generate_courier_payload()
        payload.pop("password")

        response = api.create_courier(payload)

        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для создания учетной записи"



    

