import pymongo
import pathlib
from dependency_injector.wiring import Provide, inject
from typing import Dict, Any, Optional, List
from collections.abc import Iterable
from src.demoapp.container import Container
import getpass
from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def get_all(self) -> Iterable[Any]:
        ...


class DbAdapter(ABC):
    @abstractmethod
    def _get_repo(self, name: str) -> Repository:
        ...


class MongoDBAdapter:
    def __init__(
        self,
        host: str,
        port: Optional[int],
        username: Optional[str],
        password: Optional[str],
        authSource: Optional[str],
    ):
        ...


@inject
def setup_mongo(mongo_config: Dict[str, Any] = Provide[Container.conf.mongo]):
    with pymongo.MongoClient(
        host=mongo_config.host,
        port=mongo_config.port or 27017,
        username=mongo_config.username,
        password=mongo_config.password,
        authSource=mongo_config.authSource,
    ) as client:
        ...


def setup_fixtures():
    ...


if __name__ == "__main__":
    setup_fixtures()
