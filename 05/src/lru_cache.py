class LRUCache:
    '''LRU (Least Recently Used) Cache w/ OrderedDict'''
    def __init__(self, limit=42):
        self.dct = {}
        self.limit = limit

    def get(self, key):
        res = self.dct.get(key, None)
        if res is not None:
            self.dct.pop(key)
            self.dct[key] = res
        return res

    def set(self, key, value):
        if key not in self.dct and len(self.dct) == self.limit:
            self.dct.pop(list(self.dct.keys())[0])
        self.dct[key] = value

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.set(key, value)
