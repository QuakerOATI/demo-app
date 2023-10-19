from dependency_injector import containers, providers
import entities
from adapters import MongoPassengerAdapter
from demoapp import PROJECT_ROOT, CONFIG_ROOT


class Container(containers.DeclarativeContainer):
    """Main app container class."""

    conf = providers.Configuration(
        yaml_files=[
            p.joinpath("config.yaml")
            for p in (PROJECT_ROOT.joinpath("data"), CONFIG_ROOT)
        ]
    )
    passenger = providers.Factory(entities.Passenger)
    passenger_store = providers.Factory(
        MongoPassengerAdapter,
        passenger.provider,
        conf.mongo.uri,
        conf.mongo.auth_db,
        conf.mongo.collection,
    )
