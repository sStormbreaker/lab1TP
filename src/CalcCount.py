# -*- coding: utf-8 -*-
from Types import DataType


class CalcCount:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.count = 0

    def calc(self) -> int:
        for student in self.data:
            for tuple in self.data[student]:
                if tuple[1] < 61:
                    self.count += 1
                    break

        return self.count
