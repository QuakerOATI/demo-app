from dependency_injector import containers, providers
from . import entities
from .adapters import MongoPassengerAdapter
from pathlib import Path

# Could also inject as a providers.Dependency instance
PROJECT_ROOT = Path(__file__).parent.parent.parent


class Container(containers.DeclarativeContainer):
    """Main app container class."""

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
