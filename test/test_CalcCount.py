# -*- coding: utf-8 -*-
from src.Types import DataType
from src.CalcCount import CalcCount
import pytest


class TestCalcCount:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, int]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 80),
                    ("русский язык", 76),
                    ("программирование", 100)
                ],

            "Петров Игорь Владимирович":
                [
                    ("математика", 61),
                    ("русский язык", 80),
                    ("программирование", 78),
                    ("литература", 97)
                ],

            "Абрамов1 Петр Сергеевич":
                [
                    ("математика", 80),
                    ("русский язык", 41),
                    ("программирование", 100)
                ],

            "Петров1 Игорь Владимирович":
                [
                    ("математика", 61),
                    ("русский язык", 80),
                    ("программирование", 78),
                    ("литература", 61)
                ],
        }

        return data, 1

    def test_init_calc_count(self, input_data: tuple[DataType, int]) -> None:

        calc_count = CalcCount(input_data[0])
        print(input_data[0])
        assert input_data[0] == calc_count.data

    def test_count(self, input_data: tuple[DataType, int]) -> None:

        count = CalcCount(input_data[0]).calc()
        assert count == input_data[1]

    def test_count_zero(self, input_data: tuple[DataType, int]) -> None:

        input_data[0].popitem()
        input_data[0].popitem()

        count = CalcCount(input_data[0]).calc()
        assert count == 0
