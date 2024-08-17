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

def make_child01(child):
    if child == '0_child':
        return 0
    else:
        return 1

def make_TripEasier_ProductPitched(productpitched):
    if productpitched == 'Basic':
        return 3
    elif productpitched == 'Super Deluxe':
        return 0.001
    else:
        return 1

def make_TripEasier_Marry(marry):
    if marry == 'Single':
        return 2
    else:
        return 1

def make_TripEasier_Child(child):
    if child == '0_child':
        return 2
    elif child == '1_child':
        return 1
    elif child == '2_child':
        return 1
    else:
        return 0.4