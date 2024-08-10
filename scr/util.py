import pandas as pd
import re
import unicodedata

def japanese_to_int_util(str):
    japanese_dict = {
        "一": 1,
        "二": 2,
        "三": 3,
        "四": 4,
        "五": 5,
        "六": 6,
        "七": 7,
        "八": 8,
        "九": 9,
        "十": 10
    }
    
    current = 0
    total = 0
    for char in str:
        if char in japanese_dict:
            num = japanese_dict[char]
            if num >= 10:
                current *= num
            else:
                current += num
    
    if current:
        total += current
    
    return total

def japanese_to_int(Age):
    digits = re.findall(r'\d+', Age)
    non_digits = re.sub(r'[^\D]', '', Age)
    
    if pd.isna(Age):
        return None
    
    if digits:
        return int(digits[0])
    
    return japanese_to_int_util(non_digits)

def convert_to_second(duration):
    if '秒' in duration:
        return int(duration.replace('秒', ''))
    elif '分' in duration:
        return int(duration.replace('分', '')) * 60
    else:
        return int(duration)
    
def normalize_gender(gender):
    gender = gender.strip().lower().replace('\u3000', '')
    gender = gender.replace('ｆｅｍａｌｅ', 'female')
    gender = gender.replace('ｍａｌｅ', 'male')
    if 'female' in gender:
        return 'female'
    elif 'male' in gender:
        return 'male'
    else:
        return gender
    
def normalize_trips(trip):
    if trip.isdigit():
        return int(trip)
    elif '半年に' in trip:
        return int(trip.replace('半年に', '').replace('回', ''))
    elif '四半期に' in trip:
        return int(trip.replace('四半期に', '').replace('回', '')) * 2
    elif '年に' in trip:
        return int(trip.replace('年に', '').replace('回', '')) * 4
    else:
        return trip

def normalize_product_pitched(product):
    product = product.lower()
    product = unicodedata.normalize('NFKC', product)
    product = product.replace('|', 'l').replace('×', 'x').replace('𝘳', 'r').replace('𝘤', 'c')
    product_dict = {
        'basic': 'Basic',
        'standard': 'Standard',
        'deluxe': 'Deluxe',
        'super deluxe': 'Super Deluxe',
        'king': 'King'
    }
    
    for key, value in product_dict.items():
        if key in product:
            return value
    
    return product

def normalize_designation(designation):
    designation = designation.lower()
    designation = unicodedata.normalize('NFKC', designation)
    designation = designation.replace('×', 'x').replace('ｕ', 'u').replace('ѵ', 'v')
    designation_dict = {
        'executive': 'Executive',
        'senior manager': 'Senior Manager',
        'avp': 'AVP',
        'manager': 'Manager',
        'vp': 'VP'
    }
    
    for key, value in designation_dict.items():
        if key in designation:
            return value
    return designation
