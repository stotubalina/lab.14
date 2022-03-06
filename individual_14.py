#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sample(string):
    def name_surname(n, s):
        sample_data = string.replace("%N%", n)
        sample_data = sample_data.replace("%F%", s)
        return sample_data

    return name_surname


if __name__ == "__main__":
    sample_string = (
         "Уважаемый %F% %N%! Вы делаете работу по замыканиям функции."
    )
    name, surname = input("Введите имя и фамилию: ").split()
    print(sample(sample_string)(name, surname))
