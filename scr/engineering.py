import numpy as np
import pandas as pd

def make_TypeOfContactNULL(value):
    if value == 'No':
        return 1
    else:
        return 0

def make_motivation_gender(gender):
    if gender == 'female':
        return 1.0
    elif gender == 'male':
        return 1.3