from Types import DataType
from json import load as jsLoad
from DataReader import DataReader


class ReaderJSON(DataReader):

    def __init__(self) -> DataType:
        self.students: DataType = {}

    def read(self, path: str):
        with open(path, encoding='utf-8') as file:
            dataJSON = jsLoad(file)
            studentNames = dataJSON.keys()

            for student in studentNames:
                tupleList = [(k,int(v)) for k,v in dataJSON[student].items()]
                self.students[student] = tupleList
        
        return self.students
