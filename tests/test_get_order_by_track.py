from helpers.generator import generate_order_payload


class TestGetOrderByTrack:
    def create_order_and_get_track(self, api):
        resp = api.create_order(generate_order_payload())
        assert resp.status_code == 201
        assert "track" in resp.json()
        return resp.json()["track"]

    def test_get_order_success(self, api):
        track = self.create_order_and_get_track(api)

        response = api.get_order_by_track(track)

        assert response.status_code == 200
        body = response.json()
        assert "order" in body
        assert isinstance(body["order"], dict)

    def test_get_order_without_track_fails(self, api):
        response = api.get_order_by_track(None)

        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для поиска"

    def test_get_order_nonexistent_track_fails(self, api):
        wrong_track = 999999999

        response = api.get_order_by_track(wrong_track)

        assert response.status_code == 404
        assert response.json().get("message") == "Заказ не найден"
