from dependency_injector import containers, providers
from . import entities
from .adapters import MongoPassengerAdapter
from pathlib import Path


class Container(containers.DeclarativeContainer):
    """Main app container class."""

    PROJECT_ROOT = providers.Dependency(Path)
    CONFIG_ROOT = providers.Dependency(Path)
    conf = providers.Configuration(
        yaml_files=[p.joinpath("settings.yaml") for p in (PROJECT_ROOT, CONFIG_ROOT)]
    )
    passenger = providers.Factory(entities.Passenger)
    passenger_store = providers.Factory(
        MongoPassengerAdapter,
        passenger.provider,
        conf.mongo.uri,
        conf.mongo.auth_db,
        conf.mongo.collection,
    )
