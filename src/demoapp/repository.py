import pymongo
from abc import ABC, abstractmethod
from typing import List, Any
from contextlib import AbstractContextManager
from dependency_injector import containers, providers


class DbAdapter(containers.DeclarativeContainer):
    ...
