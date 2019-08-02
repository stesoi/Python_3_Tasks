import os

class BinaryRecordFile:
    def __init__(self, filename, record_size, auto_flush=True):
        self.__record_size = record_size
        mode = "w+b" if not os.path.exists(filename) else "r+b"
        self.__fh = open(filename, mode)
        self.auto_flush = auto_flush

    @property
    def record_size(self):
        return self.__record_size

    @property
    def name(self):
        return self.__fh.name

    def flush(self):
        self.__fh.flush()

    def close(self):
        self.__fh.close()

    def append(self, record):
        assert isinstance(record, (bytes, bytearray)), "binary data required"
        assert len(record) == self.record_size, ("record must be exactly {0} bytes".format(self.record_size))
        self.__fh.seek(0, os.SEEK_END)
        self.__fh.write(record)
        if self.auto_flush:
            self.__fh.flush()

    def __setitem__(self, index, record):
        assert isinstance(record, (bytes, bytearray)), "binary data required"
        assert len(record) == self.record_size, ("record must be exactly {0} bytes".format(self.record_size))
        self.__seek_to_index(index)
        self.__fh.write(record)
        if self.auto_flush:
            self.__fh.flush()

    def __getitem__(self, index):
        self.__seek_to_index(index)
        return self.__fh.read(self.record_size)

    def __seek_to_index(self, index):
        if self.auto_flush:
            self.__fh.flush()
        self.__fh.seek(0, os.SEEK_END)
        end = self.__fh.tell()
        offset = index * self.__record_size
        if offset >= end:
            raise IndexError("no record at index position {0}".format(
                index))
        self.__fh.seek(offset)

    def __delitem__(self, index):
        length = len(self)
        for next_item in range(index + 1, length):
            self[index] = self[next_item]
            index += 1
        self.__fh.truncate((length - 1) * self.record_size)
        self.__fh.flush()

    def __len__(self):
        if self.auto_flush:
            self.__fh.flush()
        self.__fh.seek(0, os.SEEK_END)
        end = self.__fh.tell()
        return end // self.__record_size