import requests
import json


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url


    def create_courier(self, payload):
        return requests.post(f"{self.base_url}/courier", json=payload)

    def login_courier(self, login, password):
        payload = {
            "login": login,
            "password": password
        }
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
        params = {
            "courierId": courier_id,
            "nearestStation": nearest_station,
            "limit": limit,
            "page": page
        }

        return requests.get(f"{self.base_url}/orders", params=params)

    def get_order_by_track(self, track):
        params = {}
        if track is not None:
            params["t"] = track
        return requests.get(f"{self.base_url}/orders/track", params=params)

