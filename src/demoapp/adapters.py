import pymongo
from collections.abc import Iterator
from typing import Callable, List
from abc import ABC, abstractmethod
from contextlib import AbstractContextManager, AbstractAsyncContextManager

from .entities import Passenger


class PassengerAdapter(ABC):
    def __init__(self, passenger_factory: Callable[..., Passenger]) -> None:
        self._factory = passenger_factory

    @abstractmethod
    def get_all(self) -> List[Passenger]:
        ...


class MongoPassengerAdapter(PassengerAdapter, AbstractContextManager):
    """Obtains Passenger objects from a Mongo DB.

    Can (and probably should) be used as a context manager.

    Note that because pymongo.MongoClient is not fork-safe, a separate
    instance of this class should be created for every client process.  See
    `the PyMogo documentation <https://pymongo.readthedocs.io/en/stable/faq.html#multiprocessing>`_.
    """

    def __init__(
        self,
        passenger_factory: Callable[..., Passenger],
        uri: str,
        authSource: str,
        collection_name: str,
    ) -> None:
        """
        Args:
            passenger_factory: Callable which returns Passenger instances
            uri: URI of Mongo server, including DB name
            authSorce: Name of authentication DB
            collection_name: Name of collection containing Passenger data
        """
        self._client = pymongo.MongoClient(
            uri,
            authSource=authSource,
        )
        super().__init__(passenger_factory)
        self._collection = self._client.get_default_database().get_collection(
            collection_name
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self._client.close()

    def get_all(self) -> Iterator[Passenger]:
        """Generator of all Passenger documents in the configured collection."""
        yield from map(lambda record: self._factory(**record), self._collection.find())

    def test_connection(self) -> bool:
        """Return True if attempt to ping the Mongo client is successful."""
        try:
            self._client.get_default_database().command("ping")
            return True
        except pymongo.errors.ConnectionFailure:
            return False


class AsyncMongoPassengerAdapter(PassengerAdapter, AbstractAsyncContextManager):
    """Uses Motor for non-blocking IO with Mongo DB."""

    def __init__(self):
        raise NotImplementedError()

    def __enter__(self):
        raise NotImplementedError()

    def __exit__(self, exc_type, exc_value, exc_tb):
        raise NotImplementedError()
