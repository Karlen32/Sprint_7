class TestLoginCourier:

    def test_courier_login_successfully(self, courier, api):
        response = api.login_courier(courier["login"], courier["password"])

        assert response.status_code == 200
        assert isinstance(response.json()["id"], int)

    def test_login_without_login(self, courier, api):
        response = api.login_courier(None, courier["password"])

        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для входа"

    def test_login_without_password(self, courier, api):
        response = api.login_courier(courier["login"], None)

        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для входа"

    def test_login_with_wrong_password_fails(self, courier, api):
        response = api.login_courier(courier["login"], "wrong_pass")

        assert response.status_code == 404
        assert response.json().get("message") == "Учетная запись не найдена"

    def test_login_nonexistent_user_fails(self, api):
        response = api.login_courier("nonexistent_user", "123456")

        assert response.status_code == 404
        assert response.json().get("message") == "Учетная запись не найдена"



