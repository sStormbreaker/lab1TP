# -*- coding: utf-8 -*-
import argparse
import sys

from ReadJSON import ReaderJSON
from CalcCount import CalcCount


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = ReaderJSON()
    students = reader.read(path)

    for student in students:
        print("Student: ", student, students[student])

    count = CalcCount(students).calc()
    print("\nCount students with mark lower than 61: ", count)


if __name__ == "__main__":
    main()
