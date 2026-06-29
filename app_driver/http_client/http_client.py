import httpx

class HttpClient:
    """Клиент для инициализации классов для работы с API"""

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.Client(
            base_url = self.base_url,
            timeout = httpx.Timeout(5, read = 100, write = 100)
        )

    def get(self, endpoint: str, **kwargs) -> httpx.Response:
        return self.client.get(endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> httpx.Response:
        return self.client.post(endpoint, **kwargs)

    def patch(self,endpoint: str, **kwargs) -> httpx.Response:
        return self.client.patch(endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> httpx.Response:
        return self.client.delete(endpoint, **kwargs)

    def close(self) -> None:
        """Закрывает HTTP-клиет и освобождает ресурсы"""
        self.client.close()

    def __enter__(self) -> "HttpClient":
        """Вызывается при входе в блок with"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Вызывается при выходе из блока with — штатном, по исключению или по return"""
        self.close()

""" scope="session" — фикстура создаётся один раз за всю тестовую сессию (пока выполняются все тесты)
Закрытие (close()) происходит один раз после окончания всей сессии (благодаря yield), корректно освобождая соединения."""
