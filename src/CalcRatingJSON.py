# -*- coding: utf-8 -*-
from Types import DataType

RatingType = dict[str, float]


class CalcRatingJSON:
    
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}

    def calc(self) -> RatingType:
        pass
