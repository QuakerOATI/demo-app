from typing import Optional
from dataclasses import dataclass


@dataclass
class Passenger:
    name: str
    age: Optional[int]
    survived: bool
    numSiblings: Optional[int]
    ticket: str
    fare: float
    cabin: Optional[str]
    embarked: str

    def __repr__(self):
        return "{0}(name='{1}', age={2}, survived={3})".format(
            self.__class__.__name__, self.name, self.age, self.survived
        )
