import copy
import collections


class Atomic:
    def __init__(self, container, deep_copy=True):
        assert (isinstance(container, collections.MutableSequence) or isinstance(container, collections.MutableSet) or
                isinstance(container, collections.MutableMapping)), ("Must be a mutable collection!")
        self.original = container
        self.copy = copy.deepcopy if deep_copy else copy.copy

    def __enter__(self):
        self.modified = self.copy(self.original)
        return self.modified

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            if isinstance(self.original, collections.MutableSequence):
                self.original[:] = self.modified
            elif (isinstance(self.original, collections.MutableSet) or
                  isinstance(self.original, collections.MutableMapping)):
                self.original.clear()
                self.original.update(self.modified)