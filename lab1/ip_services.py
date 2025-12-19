import requests
from abc import ABC, abstractmethod

# Базовый класс, определяющий интерфейс для всех сервисов получения IP.
# Это "контракт": любой наследник обязан реализовать метод get_ip.
class IPService(ABC):
    @abstractmethod
    def get_ip(self) -> str:
        pass

# Этот класс реализует наш контракт для сервиса ip-api.com.
class IpApiService(IPService):
    def get_ip(self) -> str:
        response = requests.get('http://ip-api.com/json/')
        response.raise_for_status()
        return response.json().get('query')

# Этот класс реализует наш контракт для сервиса jsonip.com.
class JsonIpService(IPService):
    def get_ip(self) -> str:
        response = requests.get('https://jsonip.com/')
        response.raise_for_status()
        return response.json().get('ip')

# ФАБРИКА
# Отвечает за инкапсуляцию логики создания конкретных объектов-сервисов.
class IPServiceFactory:
    @staticmethod
    def create(service_type: str) -> IPService:
        services = {
            'ip-api': IpApiService,
            'jsonip': JsonIpService
        }
        service_class = services.get(service_type, IpApiService)
        return service_class()