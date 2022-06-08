# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 12:17:00 2022

@author: sebas
"""

ASSESSMENT_WEIGHTS = [30, 30, 40]


class Student:
    def __init__(self, id, name, a1, a2, exam):
        self.__sid = id
        self.__name = name
        self.__a1marks = a1
        self.__a2marks = a2
        self.__exam_marks = exam

    def get_name(self):
        return self.__name

    def get_a1marks(self):
        return self.__a1marks

    def get_a2marks(self):
        return self.__a2marks

    def get_exam_marks(self):
        return  self.__exam_marks

    def get_weighted_mark(self):
        return (ASSESSMENT_WEIGHTS[0] * self.__a1marks + ASSESSMENT_WEIGHTS[1] * self.__a2marks
                + ASSESSMENT_WEIGHTS[2] * self.__exam_marks) / 100

    def __str__(self):
        # desired format - Ali Hyder: 75, 68, 80, 74.9
        return f'{self.__name}: {self.__a1marks}, {self.__a2marks}, {self.__exam_marks}, {self.get_weighted_mark():.1f}'


def main():
    # create two instances
    ali_hyder = Student(129, 'Ali Hyder', 75, 68, 80)
    sarah_white = Student(243, 'Sarah White', 63, 70, 79)

    print(ali_hyder)
    print(sarah_white)


main()
