class CustomList(list):
    '''Custom class for lists'''
    def __init__(self, lst=None):
        if lst is None:
            self.lst = []
        else:
            if not isinstance(lst, list):
                raise TypeError("object is not a list")
            self.lst = lst

    def __validate_index(self, index):
        if not isinstance(index, int):
            raise TypeError("incorrect index value")
        if not index < len(self) or -index < -len(self):
            raise IndexError("index is out of range")

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, index):
        if isinstance(index, slice):
            start = index.start
            stop = index.stop
            step = index.step
            if start is not None:
                self.__validate_index(start)
            if stop is not None:
                self.__validate_index(stop)
            if step is not None:
                if not isinstance(step, int):
                    raise TypeError("incorrect step")

            return self.lst[start: stop: step]

        self.__validate_index(index)

        return self.lst[index]

    def __add__(self, obj):
        if isinstance(obj, CustomList):
            obj = obj.lst

        lst_new = [el1 + el2 for el1, el2 in zip(self.lst, obj)]
        if len(self) > len(obj):
            lst_new.extend(self[len(obj):])
        else:
            lst_new.extend(obj[len(self):])

        return CustomList(lst_new)

    def __radd__(self, obj):
        return self + obj

    def __sub__(self, obj):
        if isinstance(obj, CustomList):
            obj = obj.lst

        lst_new = [el1 - el2 for el1, el2 in zip(self.lst, obj)]
        if len(self) > len(obj):
            lst_new.extend(self[len(obj):])
        else:
            lst_new.extend(map(lambda x: -x, obj[len(self):]))

        return CustomList(lst_new)

    def __rsub__(self, obj):
        if isinstance(obj, CustomList):
            obj = obj.lst

        lst_new = [el2 - el1 for el1, el2 in zip(self.lst, obj)]
        if len(self) > len(obj):
            lst_new.extend(map(lambda x: -x, self[len(obj):]))
        else:
            lst_new.extend(obj[len(self):])

        return CustomList(lst_new)

    def __eq__(self, obj):
        return sum(self.lst) == sum(obj.lst)

    def __ne__(self, obj):
        return not self == obj

    def __gt__(self, obj):
        return sum(self.lst) > sum(obj.lst)

    def __ge__(self, obj):
        return sum(self.lst) >= sum(obj.lst)

    def __lt__(self, obj):
        return sum(self.lst) < sum(obj.lst)

    def __le__(self, obj):
        return sum(self.lst) <= sum(obj.lst)

    def __str__(self):
        r = ""
        for el in self.lst:
            r += str(el) + " "
        r += f"\nsum = {sum(self.lst)}"
        return r
