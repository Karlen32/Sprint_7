class TestDeleteCourier:
    def test_delete_courier_success(self, courier, api):
        courier_id = courier["id"]

        response = api.delete_courier(courier_id)

        assert response.status_code == 200
        assert response.json().get("ok") is True

    def test_delete_without_id(self, api):
        response = api.delete_courier("")

        assert response.status_code == 400  
        assert response.json().get("message") == "Недостаточно данных для удаления курьера"

    def test_delete_nonexistent_courier_fails(self, api):
        nonexistent_id = 999999

        response = api.delete_courier(nonexistent_id)

        assert response.status_code == 404
        assert response.json().get("message") == "Курьера с таким id нет."

