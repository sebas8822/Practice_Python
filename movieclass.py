# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 13:14:50 2022

@author: sebas
"""

class Movie:
    def __init__(self, title, direct, yr, genre, duration):
        self.__title = title
        self.__director = direct
        self.__year = yr
        self.__genre = genre
        self.__runtime = duration

    def get_title(self):
        return self.__title

    def get_director(self):
        return  self.__director

    def get_year(self):
        return  self.__year

    def get_genre(self):
        return self.__genre

    def get_runtime(self):
        return self.__runtime

    def set_title(self, new_title):
        # Basic validation - at least 3 characters, alphanumeric characters only
        if len(new_title) >= 3 and new_title.is_alnum():
            self.__title = new_title
        else:
            print('Invalid movie title')


def main():
    inception = Movie('Inception', 'Christopher Nolan', 200, ['Action', 'Adventure', 'Sci-Fi'], 148)
    gravity = Movie('Gravity', 'Alfonso Cuarón', 2013, ['Drama', 'Sci-Fi', 'Thriller'], 91)

    print('Inception is directed by', inception.get_director())
    print('It falls under', len(inception.get_genre()), 'genre.')
    print()

    print('Gravity has a duration of', round(gravity.get_runtime() / 60, 1), 'hours.')
    print('It is a', gravity.get_genre()[0], 'film.')


main()