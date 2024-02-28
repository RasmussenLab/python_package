from typing import Union, TypeVar, Optional, Self
from collections.abc import Iterable

T = TypeVar("T")


# Simple example: Concrete types
def add_one(number: int) -> int:
    """
    Add 1 to an `int`, returning the sum.

    >>> add_one(9)
    10
    >>> add_one(-11)
    -10
    >>> add_one(2**63-1)
    9223372036854775808
    """
    return number + 1


# Union types.
# Optional[T] == Union[T, None]
def reciprocal(number: Union[int, float]) -> Optional[float]:
    """
    Return the reciprocal of the given number. If the number is zero, return `None`.

    >>> reciprocal(5)
    0.2
    >>> reciprocal(-20)
    -0.05
    >>> reciprocal(-0.0) # returns None
    """
    if number == 0:
        return None
    return 1 / number


# Abstract types (also known as ABCs, Abstract Base Classes) are defined by their behaviour.
def flatten_ints(its: Iterable[Iterable[int]]) -> Iterable[int]:
    """
    Given an iterable of iterables of ints, return an iterable of all the ints
    in the inner iterables.

    >>> list(flatten_ints([[9, 11], [12], [4, 5]]))
    [9, 11, 12, 4, 5]
    >>> list(flatten_ints([[], (), set()]))
    []
    """
    for it in its:
        for i in it:
            yield i


# Types generic over a TypeVar
def flatten_generic(its: Iterable[Iterable[T]]) -> Iterable[T]:
    """
    Given an iterable of iterables, return an iterable of all the inner
    elements in the inner iterables.

    >>> list(flatten_generic(["hi", (4, 2.54)]))
    ['h', 'i', 4, 2.54]
    """
    for it in its:
        for i in it:
            yield i


class Circle:
    """
    Circle(radius) -> Self

    A `Circle` represents the abstract geometric shape.

    >>> c = Circle(2.21); c.diameter
    4.42
    >>> c2 = Circle.from_circumference(100); round(c2.radius, 3)
    15.916
    """

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

    def __repr__(self):
        return f"Circle({self.radius})"
