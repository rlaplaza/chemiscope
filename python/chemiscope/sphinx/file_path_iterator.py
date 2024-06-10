import uuid

from sphinx.errors import ExtensionError


class FilePathIterator:
    def __init__(self, prefix="fig", extension=".json.gz"):
        """
        Initialize the iterator

        Parameters:
        - prefix (str): The prefix for image filenames
        - extension (str): The file extension for files
        """
        self.prefix = prefix
        self.extension = extension
        self.counter = 0
        self._stop = 1000000
        self.infix = uuid.uuid4()

    def __iter__(self):
        """Iterate over paths"""
        for _i in range(self._stop):
            yield self.next()
        else:
            raise ExtensionError(f"Generated over {self._stop} files")

    def __next__(self):
        """Generates the file name"""
        self.counter += 1
        return f"{self.prefix}_{self.infix}_{self.counter:03d}{self.extension}"

    def next(self):
        """Return the next file path, with numbering starting at 1"""
        return self.__next__()

    def set_infix(self, infix):
        self.infix = infix
