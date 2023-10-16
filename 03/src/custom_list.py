class CustomList(list):
    '''Custom class for lists'''
    def __validate_index(self, index):
        if not isinstance(index, int):
            raise TypeError("incorrect index value")
        if not index < len(self) or -index < -len(self):
            raise IndexError("index is out of range")

    def __add__(self, obj):
        lst_new = [el1 + el2 for el1, el2 in zip(self, obj)]
        if len(self) > len(obj):
            lst_new.extend(self[len(obj):])
        else:
            lst_new.extend(obj[len(self):])

        return CustomList(lst_new)

    def __radd__(self, obj):
        return self + obj

    def __sub__(self, obj):
        lst_new = [el1 - el2 for el1, el2 in zip(self, obj)]
        if len(self) > len(obj):
            lst_new.extend(self[len(obj):])
        else:
            lst_new.extend(map(lambda x: -x, obj[len(self):]))

        return CustomList(lst_new)

    def __rsub__(self, obj):
        lst_new = [el2 - el1 for el1, el2 in zip(self, obj)]
        if len(self) > len(obj):
            lst_new.extend(map(lambda x: -x, self[len(obj):]))
        else:
            lst_new.extend(obj[len(self):])

        return CustomList(lst_new)

    def __eq__(self, obj):
        return sum(self) == sum(obj)

    def __ne__(self, obj):
        return not self == obj

    def __gt__(self, obj):
        return sum(self) > sum(obj)

    def __ge__(self, obj):
        return sum(self) >= sum(obj)

    def __lt__(self, obj):
        return sum(self) < sum(obj)

    def __le__(self, obj):
        return sum(self) <= sum(obj)

    def __str__(self):
        r = ""
        for el in self:
            r += str(el) + " "
        r += f"\nsum = {sum(self)}"
        return r
