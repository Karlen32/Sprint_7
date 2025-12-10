import pytest
from helpers.generator import generate_order_payload


class TestCreateOrder:
    @pytest.mark.parametrize("colors", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_different_colors(self, colors, api):
        payload = generate_order_payload(colors)

        response = api.create_order(payload)

        assert response.status_code == 201

        body = response.json()

        assert "track" in body, "Ответ не содержит track"
        assert isinstance(body["track"], int), "track должен быть int"
