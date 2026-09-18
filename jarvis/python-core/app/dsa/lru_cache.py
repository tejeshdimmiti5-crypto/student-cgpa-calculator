from collections import OrderedDict
from typing import Any

class LRUCache:
    """Bounded LRU memory cache used for hot JARVIS context."""
    def __init__(self, capacity: int = 128):
        if capacity < 1: raise ValueError("capacity must be positive")
        self.capacity=capacity
        self._data=OrderedDict()

    def get(self,key: str, default: Any=None):
        if key not in self._data: return default
        value=self._data.pop(key); self._data[key]=value
        return value

    def put(self,key: str,value: Any):
        if key in self._data: self._data.pop(key)
        self._data[key]=value
        if len(self._data)>self.capacity: self._data.popitem(last=False)
