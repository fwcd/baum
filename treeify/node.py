from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    name: str
    children: list[Node]
