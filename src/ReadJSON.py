from Types import DataType
from src.DataReader import DataReader


class ReaderJSON(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        pass
