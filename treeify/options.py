from dataclasses import dataclass
from treeify.style import Style

@dataclass
class Options:
    style: Style
    spaces: int
