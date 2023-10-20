class LRUCache:
    '''LRU (Least Recently Used) Cache w/out OrderedDict'''
    __slots__ = ("_dct", "limit")

    def __init__(self, limit=42):
        self._dct = {}
        self.limit = limit

    def __setattr__(self, name, value):
        if name == 'limit':
            if not isinstance(value, int):
                raise TypeError("limit have to be an integer")
            if value < 1:
                raise ValueError("limit should be positive")
        return super().__setattr__(name, value)

    def get(self, key):
        res = self._dct.get(key, None)
        if res is not None:
            self._dct.pop(key)
            self._dct[key] = res
        return res

    def set(self, key, value):
        if key.__hash__ is None:
            raise TypeError("key should be hashable")
        if key not in self._dct and len(self._dct) == self.limit:
            self._dct.pop(list(self._dct.keys())[0])
        if key in self._dct:
            self._dct.pop(key)
        self._dct[key] = value

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.set(key, value)
