import logging
from argparse import ArgumentParser
from dependency_injector.wiring import Provide, inject
from demoapp import __version__

__author__ = "Michael Haynes"
__copyright__ = "Michael Haynes"
__license__ = "MIT"


from container import Container
from adapters import PassengerAdapter


def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = ArgumentParser(description="Just a Fibonacci demonstration")
    parser.add_argument(
        "--version",
        action="version",
        version=f"DemoApp {__version__}",
    )
    parser.add_argument(dest="n", help="n-th Fibonacci number", type=int, metavar="INT")
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )
    return parser.parse_args(args)


@inject
def main(passengers: PassengerAdapter = Provide[Container.passenger_store]) -> None:
    with passengers as repository:
        print(list(repository.get_all()))


if __name__ == "__main__":
    # BUGGY
    container = Container()
    container.wire(modules=[__name__])
    main()
