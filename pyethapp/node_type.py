from enum import Enum


# define node type because different behavior for different node.
class NodeType(Enum):
    boot = 0
    pow = 1
    pos = 2
