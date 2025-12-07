import requests
import json


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url


    def create_courier(self, payload):
        return requests.post(f"{self.base_url}/courier", json=payload)

    def login_courier(self, login, password):
        payload = {}
        if login is not None:
            payload["login"] = login
        if password is not None:
            payload["password"] = password

        return requests.post(f"{self.base_url}/courier/login", json=payload)

    def delete_courier(self, courier_id):
        return requests.delete(f"{self.base_url}/courier/{courier_id}")

    def create_order(self, payload):
        return requests.post(f"{self.base_url}/orders", json=payload)

    def accept_order(self, track, courier_id):
        return requests.put(
            f"{self.base_url}/orders/accept/{track}",
            params={"courierId": courier_id}
        )


    def get_orders_filtered(self, courier_id=None, nearest_station=None, limit=None, page=None):
        params = {}

        if courier_id is not None:
            params["courierId"] = courier_id

        if nearest_station is not None:
            # если список → сериализуем в JSON строку
            if isinstance(nearest_station, list):
                params["nearestStation"] = json.dumps(nearest_station)
            else:
                params["nearestStation"] = nearest_station

        if limit is not None:
            params["limit"] = limit

        if page is not None:
            params["page"] = page

        return requests.get(f"{self.base_url}/orders", params=params)

    def get_order_by_track(self, track):
        params = {}
        if track is not None:
            params["t"] = track
        return requests.get(f"{self.base_url}/orders/track", params=params)

