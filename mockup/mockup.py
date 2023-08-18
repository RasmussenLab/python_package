from typing import Union, TypeVar, Optional, Self
from collections.abc import Iterable

T = TypeVar("T")


# Simple example: Concrete types
def add_one(number: int) -> int:
    return number + 1


# Union types.
# Optional[T] == Union[T, None]
def reciprocal(number: Union[int, float]) -> Optional[float]:
    if number == 0:
        return None
    return 1 / number


# Abstract types
def flatten_ints(its: Iterable[Iterable[int]]) -> Iterable[int]:
    for it in its:
        for i in it:
            yield i


# Types generic over a TypeVar
def flatten_generic(its: Iterable[Iterable[T]]) -> Iterable[T]:
    for it in its:
        for i in it:
            yield i


class Circle:
    PI = 3.14159
    __slots__ = ["radius"]

    def __init__(self, radius: Union[int, float]):
        self.radius = float(radius)

    @property
    def diameter(self):
        return 2 * self.radius

    @classmethod
    def from_circumference(cls, circumference: Union[int, float]) -> Self:
        return cls(circumference / (2 * cls.PI))
