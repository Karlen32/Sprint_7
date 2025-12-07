import time
from helpers.generator import generate_order_payload


class TestAcceptOrderAPI:

    def create_order_track(self, api):
        resp = api.create_order(generate_order_payload())
        assert resp.status_code == 201
        assert "track" in resp.json()
        return resp.json()["track"]

    def test_accept_order_success(self, courier, api):
        track = self.create_order_track(api)
        time.sleep(1)

        response = api.accept_order(track, courier["id"])

        assert response.status_code == 200
        assert response.json().get("ok") is True

    def test_accept_order_without_courier_id_fails(self, api):
        track = self.create_order_track(api)

        response = api.accept_order(track, None)

        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для поиска"

    def test_accept_order_with_wrong_courier_id_fails(self, api):
        track = self.create_order_track(api)

        response = api.accept_order(track, 999999)

        assert response.status_code == 404
        assert response.json().get("message") == "Курьера с таким id не существует"

    def test_accept_order_without_order_id(self, courier, api):
        response = api.accept_order('', courier['id'])

        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для поиска"

    def test_accept_order_with_wrong_order_id(self, courier, api):
        response = api.accept_order(999999, courier['id'])

        assert response.status_code == 404
        assert response.json().get("message") == "Заказа с таким id не существует"

    def test_accept_order_already_in_work(self, courier, api):
        track = self.create_order_track(api)
        time.sleep(1)
        first = api.accept_order(track, courier["id"])
        assert first.status_code == 200

        second = api.accept_order(track, courier["id"])

        assert second.status_code == 409
        assert second.json().get("message") == "Этот заказ уже в работе"
