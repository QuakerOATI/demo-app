from dependency_injector.wiring import Provide, inject
from pathlib import Path

from .container import Container
from .adapters import PassengerAdapter


@inject
def main(passengers: PassengerAdapter = Provide[Container.passenger_store]) -> None:
    print(passengers.get_all())


if __name__ == "__main__":
    # BUGGY
    container = Container(PROJECT_ROOT=Path.home().joinpath("settings.yaml"))
    container.wire(modules=[__name__])
    main()
