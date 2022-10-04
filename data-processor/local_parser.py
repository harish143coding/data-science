import pandas as pd
import os
import random


data = pd.read_csv(r"../notebooks/boston.csv")
FILENAME = 'boston_living.json'


def put_data(filename: str):
    if os.path.exists(filename):
        return f"{filename} is already exists"
    else:
        with open(filename, "w") as file:
            file.write(data.loc[:5,:].values())
        return print("file added")


def it_is_composite(a: int, b: int):
    rem = abs(b) % abs(a)
    return rem


def know_list_len(l1: list, l2: list):
    if len(l1) == len(l2):
       l3 = l1 +l2
    else:
        l3 = print("not computeable")
    return l3








# python unit-testing

