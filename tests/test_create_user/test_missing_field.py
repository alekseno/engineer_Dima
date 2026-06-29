#from typing import Literal

import pytest
import httpx

ENDPOINT = "/api/v1/users"
class TestRequiredFieldMissing:
#Проверка обязательных полей
    @pytest.mark.parametrize("missing_field", [
    "email",
    "password",
    "lastName",
    "firstName",
    "middleName"
])

    def test_required_field_missing(self, client, valid_user_data, missing_field):
        """Проверка отсутствия обязательного поля"""
        # 1. Копируем полные данные и удаляем проверяемое поле
        incomplete_data = valid_user_data.copy()
        del incomplete_data[missing_field]

        # 2. POST-запрос без одного поля
        response = client.post(ENDPOINT, json = incomplete_data)

        assert response.status_code == httpx.codes.UNPROCESSABLE_ENTITY, (f"Ожидался 422, при отсутствии '{missing_field}',"
        f"получен {response.status_code}. Тело: {response.text}")

        # 4. Проверка структуры ошибки
        detail = response.json().get("detail")
        assert detail is not None, f"Нет ключа 'detail' в ответе {response.json()}"


        #5 Поиск ошибки value_error.missing для конкретного поля
        field_errors = [
            err for err in detail if err.get("type") == "missing" and err.get("loc") == ["body", missing_field]
        ]
        assert len(field_errors) > 0, (
            f"Нет ошибки 'value_error.missing' для поля '{missing_field}'. "
            f"Полученные ошибки: {detail}"
            )
        

