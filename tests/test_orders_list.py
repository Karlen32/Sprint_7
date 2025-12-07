class TestOrdersFilters:

    def test_get_orders_by_courier(self, api, courier, order):
    
        response = api.get_orders_filtered(courier_id=courier["id"])

        assert response.status_code == 200
        assert isinstance(response.json().get("orders"), list)

    def test_get_orders_by_courier_with_station_filter(self, api, courier, order):

        response = api.get_orders_filtered(
            courier_id=courier["id"],
            nearest_station=["1","2"]
        )

        assert response.status_code == 200
        assert isinstance(response.json().get("orders"), list)

    def test_get_orders_with_limit_and_page(self, api, order):

        response = api.get_orders_filtered(limit=10, page=0)

        assert response.status_code == 200
        assert isinstance(response.json().get("orders"), list)

    def test_get_orders_by_station_only(self, api, order):

        response = api.get_orders_filtered(nearest_station=["110"]) 

        assert response.status_code == 200
        assert isinstance(response.json().get("orders"), list)

    def test_get_orders_by_nonexistent_courier(self, api):

        response = api.get_orders_filtered(courier_id=999999)

        assert response.status_code == 404
        assert response.json().get("message") == f"Курьер с идентификатором {999999} не найден"