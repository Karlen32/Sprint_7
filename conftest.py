import pytest
from config import BASE_URL
from helpers.api_client import ApiClient
from helpers.generator import generate_order_payload, generate_courier_payload


@pytest.fixture
def api():
    return ApiClient(BASE_URL)


@pytest.fixture
def courier(api):
    payload = generate_courier_payload()

    # создание
    create_resp = api.create_courier(payload)
    assert create_resp.status_code == 201, "Курьер не создался"

    # логин
    login_resp = api.login_courier(payload["login"], payload["password"])
    assert login_resp.status_code == 200, "Не удалось залогиниться курьером"

    payload["id"] = login_resp.json()["id"]

    # отдаём наружу
    yield payload

    # cleanup
    try:
        api.delete_courier(payload['id'])
    except Exception:
        pass


@pytest.fixture
def auto_cleanup(api):
    created = []
    yield created
    for courier_id in created:
        try:
            api.delete_courier(courier_id)
        except:
            pass


@pytest.fixture
def order(api):
    payload = generate_order_payload()

    resp = api.create_order(payload)
    assert resp.status_code == 201, "Не удалось создать заказ"

    return resp.json()["track"]

