# 役立つものを格納するモジュール

import numpy as np
import pandas as pd
import re
from rapidfuzz import process

# numeric_match_types_with_kanji_and_zenkaku = r"[0-9]+|[一二三四五六七八九]+|[１２３４５６７８９]+"

numeric_translation_table_with_kanji_and_zenkaku = str.maketrans(
    "一二三四五六七八九１２３４５６７８９", "123456789123456789"
)

zenkaku_match_types = "\u3000" + "".join(chr(i) for i in range(0xFF01, 0xFF5E + 1))
hankaku_match_types = "".join(chr(i) for i in range(0x0020, 0x007E + 1))

z2h_translation_table = str.maketrans(zenkaku_match_types, hankaku_match_types)

decimal_pattern = r"\d+\.?\d*"


def extract_number(s: str) -> int:
    """文字列から数字（半角のみ）を抽出する関数

    半角数字以外の文字は無視される

    また、数字が含まれない場合は0を返す

    Args:
        s (str): 抽出する文字列

    Returns:
        int: 抽出された数字
    """

    search_result = re.search(r"\d+", s)
    if search_result is None:
        return 0
    return int(search_result.group())


def extract_alphabet(s: str) -> str:
    """文字列からアルファベットを抽出する関数

    Args:
        s (str): 抽出する文字列

    Returns:
        str: 抽出されたアルファベット
    """

    search_result = re.findall(r"[a-zA-Z]+", s)
    if search_result is None:
        return ""
    return "".join(search_result)


def str_to_int_with_kanji_and_zenkaku(s: str) -> int:
    """漢数字や全角数字に対応した、文字列を整数に変換する関数

    数字以外の文字は無視される

    Args:
        s (str): 変換する文字列

    Returns:
        int: 変換後の整数
    """

    translated = s.translate(numeric_translation_table_with_kanji_and_zenkaku)
    splitted_ju = translated.split("十")  # 「十」の位置で分割（多分「百」はないので無視
    if len(splitted_ju) == 1:
        return extract_number(splitted_ju[0])
    elif len(splitted_ju) == 2:
        return extract_number(splitted_ju[0]) * 10 + extract_number(splitted_ju[1])
    else:
        raise ValueError("Invalid input")


def convert_age_to_int(age_str: str) -> int:
    """年齢を表す文字列を整数に変換する関数

    Args:
        s (str): 変換する文字列

    Returns:
        int: 年齢を表す整数
    """

    if pd.isnull(age_str):
        return np.nan
    age_int = str_to_int_with_kanji_and_zenkaku(age_str)

    if age_str.find("代") != -1:
        # ○○代の場合は、その年代の中間の年齢を返す
        return age_int + 5
    return age_int


def convert_duration_to_int(duration_str: str) -> int:
    """期間を表す文字列を整数に変換する関数

    Args:
        s (str): 変換する文字列

    Returns:
        int: 期間を表す整数
    """

    if pd.isnull(duration_str):
        return np.nan
    duration_int = str_to_int_with_kanji_and_zenkaku(duration_str)

    if duration_str.find("分") != -1:
        return duration_int * 60
    elif duration_str.find("秒") != -1:
        return duration_int
    else:
        raise ValueError("Invalid input")


def convert_gender_to_int(gender_str: str) -> int:
    """性別を表す文字列を整数に変換する関数

    Args:
        s (str): 変換する文字列

    Returns:
        int: 性別を表す整数
    """

    gender_str_stripped = gender_str.replace(" ", "").replace("　", "")
    gender_str_normalized = gender_str_stripped.translate(z2h_translation_table).lower()

    if gender_str_normalized == "male":
        return 0
    elif gender_str_normalized == "female":
        return 1
    else:
        return -1


def normalize_number_of_followups(followups: float) -> float:
    """フォローアップの回数を正規化する関数

    Args:
        followups (float): フォローアップの回数

    Returns:
        float: 正規化されたフォローアップの回数
    """

    if pd.isnull(followups):
        return np.nan
    if followups < 100:
        return followups
    elif followups < 1000:
        return followups / 100
    else:
        raise ValueError("Invalid input" + str(followups))


def convert_product_pitched_to_int(product_str: str) -> int:
    """提案された商品を表す文字列を整数に変換する関数

    Args:
        s (str): 変換する文字列

    Returns:
        int: 提案された商品を表す整数
    """
    product_pitched_mapping = {
        "basic": 0,
        "standard": 1,
        "deluxe": 2,
        "superdeluxe": 3,
    }

    product_str_stripped = product_str.replace(" ", "").replace("　", "")
    product_str_normalized = product_str_stripped.translate(z2h_translation_table).lower()
    product_str_filtered = extract_alphabet(product_str_normalized)

    closest_match = process.extractOne(product_str_filtered, product_pitched_mapping.keys())
    closest_match_str = closest_match[0]

    if closest_match_str in product_pitched_mapping:
        return product_pitched_mapping[closest_match_str]
    else:
        raise ValueError("Invalid input")


def convert_trips_to_int(trips_str: str) -> int:
    """旅行回数を表す文字列を整数に変換する関数

    Args:
        trips_str (str): 旅行回数を表す文字列

    Returns:
        int: 旅行回数を表す整数
    """

    if pd.isnull(trips_str):
        return np.nan
    trips_int = extract_number(trips_str)
    if trips_str.find("半年") != -1:
        return trips_int * 2
    elif trips_str.find("四半期") != -1:
        return trips_int * 4
    else:
        return trips_int


def convert_designation_to_int(designation_str: str) -> int:
    """役職を表す文字列を整数に変換する関数

    Args:
        designation_str (str): 役職を表す文字列

    Returns:
        int: 役職を表す整数
    """

    designation_mapping = {
        "executive": 0,
        "manager": 1,
        "seniormanager": 2,
        "avp": 3,
        "vp": 4,
    }

    designation_str_stripped = designation_str.replace(" ", "").replace("　", "")
    designation_str_normalized = designation_str_stripped.translate(z2h_translation_table).lower()
    designation_str_filtered = extract_alphabet(designation_str_normalized)

    closest_match = process.extractOne(designation_str_filtered, designation_mapping.keys())
    closest_match_str = closest_match[0]

    if closest_match_str in designation_mapping:
        return designation_mapping[closest_match_str]
    else:
        raise ValueError("Invalid input")


def convert_income_to_int(income_str: str) -> int:
    """収入を表す文字列を整数に変換する関数

    Args:
        income_str (str): 収入を表す文字列

    Returns:
        int: 収入を表す整数
    """

    if pd.isnull(income_str):
        return np.nan
    if income_str.find("万") != -1:
        my_match = re.search(decimal_pattern, income_str)
        return float(my_match.group(0)) * 10000
    else:
        try:
            return float(income_str)
        except ValueError:
            return -1


def extract_marital_from_customer_info(customer_info_str: str) -> str:
    """顧客情報から結婚状況を抽出する関数

    Args:
        customer_info (str): 顧客情報

    Returns:
        str: 結婚状況
    """

    if customer_info_str.find("未婚") != -1 or customer_info_str.find("独身") != -1:
        return 0
    if customer_info_str.find("結婚") != -1:
        return 1
    if customer_info_str.find("離婚") != -1:
        return 2
    else:
        raise ValueError("Invalid input")


def extract_car_from_customer_info(customer_info_str: str) -> str:
    """顧客情報から車を所有しているかを抽出する関数

    Args:
        customer_info (str): 顧客情報

    Returns:
        str: 車を所有しているか
    """

    if customer_info_str.find("車所") != -1 or customer_info_str.find("車あり") != -1:
        return 1
    elif (
        customer_info_str.find("車未所") != -1
        or customer_info_str.find("車なし") != -1
        or customer_info_str.find("車保有なし") != -1
    ):
        return 0
    else:
        return 1


def extract_child_from_customer_info(customer_info_str: str) -> str:
    """顧客情報から子供の有無を抽出する関数

    Args:
        customer_info (str): 顧客情報

    Returns:
        str: 子供の有無
    """

    child_pattern = r"([0-9]+人)|([0-9]+児)"

    if (
        customer_info_str.find("子供なし") != -1
        or customer_info_str.find("子供無し") != -1
        or customer_info_str.find("子供ゼロ") != -1
        or customer_info_str.find("無子") != -1
        or customer_info_str.find("非育児家庭") != -1
    ):
        return 0
    my_match = re.search(child_pattern, customer_info_str)
    if my_match:
        return extract_number(my_match.group())
    else:
        return -1


if __name__ == "__main__":
    print(str_to_int_with_kanji_and_zenkaku("32さい"))
    print(str_to_int_with_kanji_and_zenkaku("50歳"))
    print(str_to_int_with_kanji_and_zenkaku("４７才"))
    print(str_to_int_with_kanji_and_zenkaku("７０歳"))
    print(str_to_int_with_kanji_and_zenkaku("五十三歳"))
    print(str_to_int_with_kanji_and_zenkaku("四十歳"))
