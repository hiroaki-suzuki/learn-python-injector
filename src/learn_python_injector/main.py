from abc import ABC, abstractmethod
from typing import Self

from injector import Binder, Injector, Module, inject, singleton


class Database(ABC):
    @abstractmethod
    def connect(self: Self) -> str:
        pass


class MyDatabase(Database):
    def connect(self: Self) -> str:
        return "Connected to my database"


class OtherDatabase(Database):
    def connect(self: Self) -> str:
        return "Connected to other database"


class Service:
    @inject
    def __init__(self: Self, database: Database) -> None:
        self._database = database

    def perform_action(self: Self) -> str:
        return self._database.connect()


class ConfigModule(Module):
    def configure(self: Self, binder: Binder) -> None:
        binder.bind(Database, to=MyDatabase, scope=singleton)


if __name__ == "__main__":
    injector = Injector([ConfigModule()])

    service = injector.get(Service)
    print(service.perform_action())
