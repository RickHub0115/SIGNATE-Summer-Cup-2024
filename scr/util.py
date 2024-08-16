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
    trip = str(trip)
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

def normalize_product_pitched_1(product):
    # Normalize full-width characters and lowercase all letters
    product = unicodedata.normalize('NFKC', product).lower()
    
    # Replace specific unicode characters and special symbols
    replacements = {
        r'[|｜︱︳𐄁𐊡Ⅰ]': 'i',  # Different forms of 'I' and similar symbols
        r'[×xｘχⅹ╳⤫⤬✕✖]': 'x',  # Forms of 'x'
        r'[εее]': 'e',          # Greek and Cyrillic 'e'
        r'[αаа]': 'a',          # Greek and Cyrillic 'a'
        r'[сϲс]': 'c',          # Cyrillic 'c'
        r'[βвѵ]': 'b',          # Greek and Cyrillic 'b'
        r'[ıiі]': 'i',          # Dotless i, Latin and Cyrillic 'i'
        r'[ԁᗞԀ]': 'd',          # Forms of 'D'
        r'[ꭰꓢ]': 's',          # Uncommon forms of 'S'
        r'[ςс]': 's',           # Greek final sigma and Cyrillic 's'
        r'[ոտռ]': 'n',         # Armenian letters similar to 'n' and 'h'
        r'[ȿ]': 's'             # Latin 's'
    }
    for pattern, repl in replacements.items():
        product = re.sub(pattern, repl, product)
    
    # Define standard product names and map them
    mappings = {
        'basic': 'Basic',
        'standard': 'Standard',
        'deluxe': 'Deluxe',
        'super deluxe': 'Super Deluxe',
        'king': 'King'
    }
    for key, value in mappings.items():
        if key in product:
            return value
    return product

def normalize_product_pitched_2(product):
    # Specific replacements for common transcription errors
    replacements = {
        'super deiuxe': 'Super Deluxe',
        'super seluxe': 'Super Deluxe',
        'banic': 'Basic',
        'deiuxe': 'Deluxe',
        'seluxe': 'Deluxe',
        'basis': 'Basic',
        'ntandard': 'Standard',
        'iasic': 'Basic',
        'standars': 'Standard',
        'basιc': 'Basic',  # Greek letter 'ι' to 'i'
        'ѕtandard': 'Standard',  # Cyrillic 'ѕ' to Latin 's'
        'seiuxe': 'Deluxe',
        'baѕic': 'Basic'
    }
    # Apply replacements, matching the entire string
    if product in replacements:
        return replacements[product]

    # Handle 'super' prefix to ensure proper placement
    if 'super' in product and 'deluxe' in product:
        return 'Super Deluxe'
    
    # Map to standardized names
    standard_mappings = {
        'basic': 'Basic',
        'standard': 'Standard',
        'deluxe': 'Deluxe',
        'king': 'King'
    }
    for key, value in standard_mappings.items():
        if key in product.lower():
            return value
    return product

def normalize_designation_1(designation):
    designation = unicodedata.normalize('NFKC', designation)
    replacements = {
        r'[μµ𝜇𝛍𝝁𝞵𝗌𝘀𝑠]': 'm',
        r'[αа𝛂𝜶𝝰𝞪𝖺𝗮𝘢𝑎]': 'a',
        r'[еёε𝜖𝜀𝛆𝝴𝞊𝖾𝗲𝘦𝑒]': 'e',
        r'[ν𝜈𝜈𝛎𝝂𝞶𝗇𝘯𝑛]': 'n',
        r'[ѵνѴ𝜈𝜈𝛎𝝂𝞶𝗇𝘯𝑛]': 'v',
        r'[տ]': 's'
    }
    
    for pattern, repl in replacements.items():
        designation = re.sub(pattern, repl, designation)

        designation = designation.lower()
    
        mappings = {
        'executive': 'Executive',
        'senior manager': 'Senior Manager',
        'avp': 'AVP',
        'manager': 'Manager',
        'vp': 'VP'
    }
    
    for key, value in mappings.items():
        if key in designation:
            return value
    return designation

def normalize_designation_2(designation):
    # Expanded mappings for given designations
    mappings = {
        'AVP': 'AVP', 'Senior Manager': 'Senior Manager', 'Executive': 'Executive',
        'Manager': 'Manager', 'VP': 'VP', 'Executivе': 'Executive',
        'Senior Managеr': 'Senior Manager', 'Exеcutivе': 'Executive', 'VＰ': 'VP',
        'Exеcutive': 'Executive', 'Senio𝙧 Manage𝙧': 'Senior Manager',
        'Sеnior Manager': 'Senior Manager', 'Execuｔive': 'Executive',
        'Executiѵe': 'Executive', 'Senio𝙧 Manager': 'Senior Manager', 'АVP': 'AVP',
        'Mαnager': 'Manager', 'Managеr': 'Manager', 'ΑVP': 'AVP', 'ΑVＰ': 'AVP',
        'Μαnager': 'Manager', 'Manage𝙧': 'Manager', 'E×ecutive': 'Executive',
        'Mαnαger': 'Manager', 'Μanager': 'Manager', 'Տenior Manager': 'Senior Manager',
        'Еxecutive': 'Executive', 'Senior Manage𝙧': 'Senior Manager', 'AVＰ': 'AVP',
        'Execｕtive': 'Executive', 'Senior Manαger': 'Senior Manager',
        'Senio𝙧 Manαger': 'Senior Manager', 'Manαger': 'Manager',
        'Ѕenior Μanage𝙧': 'Senior Manager', 'Exеcuｔive': 'Executive',
        'Μαnagеr': 'Manager', 'Manαgеr': 'Manager', 'Execｕｔive': 'Executive',
        'Managе𝙧': 'Manager', 'Տenior Μanager': 'Senior Manager',
        'Senio𝙧 Managеr': 'Senior Manager', 'Senior Μanager': 'Senior Manager',
        'Sеnior Managе𝙧': 'Senior Manager', 'Execｕtivе': 'Executive',
        'Senio𝙧 Mαnage𝙧': 'Senior Manager', 'Ѕenior Manager': 'Senior Manager',
        'Еxecｕtive': 'Executive', 'Mαnagеr': 'Manager', 'Senior Managе𝙧': 'Senior Manager',
        'Senior Mαnαger': 'Senior Manager', 'АVＰ': 'AVP', 'Sеnior Managеr': 'Senior Manager',
        'Mαnαgеr': 'Manager', 'Exеcｕtivе': 'Executive', 'Sеnio𝙧 Manager': 'Senior Manager',
        'Senior Mαnager': 'Senior Manager', 'μanager': 'Manager', 'e×ecutive': 'Executive',
        'senior μanager': 'Senior Manager', 'ѕenior μanager': 'Senior Manager'
    }
    
    # Return the normalized designation if it exists, otherwise return the original designation
    return mappings.get(designation, designation)

def normalize_monthly_income(income):
    if income is None or income == '':
        return None
    income = str(income)
    money = re.search(r'(\d+\.?\d*)万円', income)
    if money:
        return float(money.group(1)) * 10000
    else:
        cleaned_income = re.sub(r'[^\d\.]', '', income)
        if cleaned_income == '':
            return None
        return float(cleaned_income)
    

def divide_customer_info(info):
    if pd.isna(info):
        return pd.Series([None, None, None])
    parts = re.split(r'[、／　 ,./\t\n]+', info)
    return pd.Series(parts[:3])

def normalize_info_1(info):
    mappings = {
        '未婚': 'Single',
        '独身': 'Single',
        '結婚済み': 'Married',
        '離婚済み': 'Divorced'
    }
    
    return mappings.get(info, 'Other')

def normalize_info_2(info):
    has_car = {'車あり', '車所持', '自家用車あり', '車保有', '乗用車所持', '自動車所有', '自家用車あり'}
    no_car = {'車未所持', '自動車未所有', '車保有なし', '乗用車なし', '自家用車なし', '車なし'}
    
    if info in has_car:
        return 'Has Car'
    elif info in no_car:
        return 'No Car'
    else:
        return 'Unknown'

def normalize_info_3(info):
    no_children = {'子供なし', '子供無し', '無子', '子供ゼロ', '非育児家庭', '子育て状況不明', '子の数不詳', '子供の数不明', 'わからない', '不明'}
    one_child = {'こども1人', '1児', '子供1人', '子供有り(1人)', '子供有り'}
    two_children = {'こども2人', '子供2人', '子供有り(2人)', '2児'}
    three_children = {'こども3人', '子供3人', '子供有り(3人)', '3児'}
    
    if info in no_children:
        return '0_child'
    elif info in one_child:
        return '1_child'
    elif info in two_children:
        return '2_child'
    elif info in three_children:
        return '3_child'
    else:
        return info 

def normalize_customer_info(info):
    info = re.sub(r'[、,／/]', '/', info)
    parts = info.split('/')
    normalized_parts = []
    
    for part in parts:
        part = part.strip()
        if '未婚' in part or '独身' in part:
            normalized_parts.append('Single')
        elif '離婚済み' in part:
            normalized_parts.append('Divorced')
        elif '結婚済み' in part:
            normalized_parts.append('Married')
        
        if '車未所持' in part or '車保有なし' in part or '自家用車なし' in part:
            normalized_parts.append('No Car')
        elif '車あり' in part or '車所持' in part:
            normalized_parts.append('Has Car')
        
        if '子供なし' in part:
            normalized_parts.append('No Children')
        elif '子供有り' in part or 'こども' in part:
            # 子供の人数を抽出
            num_children = re.search(r'\d+', part)
            if num_children:
                normalized_parts.append(f'Children: {num_children.group()}')
            else:
                normalized_parts.append('Children')

    return ', '.join(normalized_parts)

def mapping_first_category(df_train, df_test):

    mapping = {
        'No': 0,
        'Self Enquiry': 1,
        'Company Invited': 2
    }
    df_train.loc[:, 'TypeofContact'] = df_train.loc[:, 'TypeofContact'].map(mapping)
    df_test.loc[:, 'TypeofContact'] = df_test.loc[:, 'TypeofContact'].map(mapping)

    mapping = {
        'Salaried': 0,
        'Small Business': 1,
        'Large Business': 2
    }
    df_train.loc[:, 'Occupation'] = df_train.loc[:, 'Occupation'].map(mapping)
    df_test.loc[:, 'Occupation'] = df_test.loc[:, 'Occupation'].map(mapping)

    mapping = {
        'male': 0,
        'female': 1
    }
    df_train.loc[:, 'Gender'] = df_train.loc[:, 'Gender'].map(mapping)
    df_test.loc[:, 'Gender'] = df_test.loc[:, 'Gender'].map(mapping)

    mapping = {
        'Super Deluxe': 0,
        'Standard': 1,
        'King': 2,
        'Deluxe': 3,
        'Basic': 4
    }
    df_train.loc[:, 'ProductPitched'] = df_train.loc[:, 'ProductPitched'].map(mapping)
    df_test.loc[:, 'ProductPitched'] = df_test.loc[:, 'ProductPitched'].map(mapping)

    mapping = {
        'Manager': 0,
        'VP': 1,
        'AVP': 2,
        'Senior Manager': 3,
        'Executive': 4
    }

    df_train.loc[:, 'Designation'] = df_train.loc[:, 'Designation'].map(mapping)
    df_test.loc[:, 'Designation'] = df_test.loc[:, 'Designation'].map(mapping)

    mapping = {
        'Married': 0,
        'Single': 1,
        'Divorced': 2,
    }
    df_train.loc[:, 'Marry'] = df_train.loc[:, 'Marry'].map(mapping)
    df_test.loc[:, 'Marry'] = df_test.loc[:, 'Marry'].map(mapping)

    mapping = {
        'No Car': 0,
        'Has Car': 1,
    }
    df_train.loc[:, 'Car'] = df_train.loc[:, 'Car'].map(mapping)
    df_test.loc[:, 'Car'] = df_test.loc[:, 'Car'].map(mapping)

    mapping = {
        '0_child': 0,
        '1_child': 1,
        '2_child': 2,
        '3_child': 3
    }
    df_train.loc[:, 'Child'] = df_train.loc[:, 'Child'].map(mapping)
    df_test.loc[:, 'Child'] = df_test.loc[:, 'Child'].map(mapping)
    
    return df_train, df_test

def feature_to_int(df_train, df_test):
    column_list_train = df_train.columns
    column_list_test = df_test.columns

    for col in column_list_train:
        #df_train[col] = df_train[col].astype(float)
        df_train[col] = df_train[col].astype(int)

    for col in column_list_test:
        #df_train[col] = df_train[col].astype(float)
        df_test[col] = df_test[col].astype(int)
    
    return df_train, df_test

def age_to_agegroup(age):
    if age == 0:
        return np.nan
    elif age < 20:
        return "10s"
    elif age < 30:
        return "20s"
    elif age < 40:
        return "30s"
    elif age < 50:
        return "40s"
    elif age < 60:
        return "50s"
    else:
        return "60s"