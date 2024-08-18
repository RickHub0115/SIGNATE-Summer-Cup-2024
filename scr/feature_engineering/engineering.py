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

def make_LivingCost_CityTier(citytier):
    if citytier == 1:
        return 1.5
    elif citytier == 2:
        return 1.3
    else:
        return 1

def make_LivingCost_Child(child):
    if child == '0_child':
        return 0
    elif child == '1_child':
        return 0.1
    elif child == '2_child':
        return 0.2
    else:
        return 0.3

def make_LivingCost_Marry(marry):
    if marry == 'Married':
        return 0.1
    else:
        return 0

def make_LivingCost_Car(car):
    if car == 'Has Car':
        return 0.05
    else:
        return 0

def make_EconomicStability_Occupation(occupation):
    if occupation == 'Large Business':
        return 1.2
    elif occupation == 'Salaried':
        return 1.1
    else:
        return 0.9

def make_EconomicStability_Disignation(designation):
    if designation == 'VP':
        return 1.5
    elif designation == 'AVP':
        return 1.4
    elif designation == 'Senior Manager':
        return 1.3
    elif designation == 'Manager':
        return 1.2
    else:
        return 1.1

def make_TripFreaqency(trips):
    if trips <= 4:
        return 0
    elif trips <= 8:
        return 1
    else:
        return 2

def make_TravelCost_PreferredPropertyStar(star):
    if star == 3.0:
        return 1
    elif star == 4.0:
        return 1.5
    else:
        return 2.0