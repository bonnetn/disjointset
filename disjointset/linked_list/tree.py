from __future__ import annotations

import typing
from dataclasses import dataclass

from disjointset.abstract import SetID


@dataclass
class Node:
    parent: typing.Optional[Node]
    id: SetID
    rank: int
    size: int
