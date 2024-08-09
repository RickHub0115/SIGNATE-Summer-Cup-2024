import pandas as pd
import re

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