import sys
from pathlib import Path

# Change here if project is renamed and does not equal the package name
dist_name = "DemoApp"
PROJECT_ROOT = Path(__file__).parent.parent.parent
CONFIG_ROOT = Path.home().joinpath(".config", dist_name)

if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

try:
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
