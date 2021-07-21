# Import regular expression library
import re 
from datetime import datetime
import pandas as pd


def minutes_to_int(running_time):
    if running_time == "N/A":
        return None
    elif isinstance(running_time, list):
        return int(running_time[0].split(" ")[0])
    else:
        return int(running_time.split(" ")[0])


def get_numerical_value(string):
    amounts = r"thousand|million|billion"
    number = r"\d+(,\d{3})*\.*\d*"
    word_re = rf"\${number}(-|\sto\s)?({number})?\s({amounts})"
    value_re = rf"\${number}"
    value_string = re.search(number, string).group()
    num_value = float(value_string.replace(",", ""))
    return num_value

def word_to_value(word):
    value_dict = {"thousand": 1000, "million":1000000, "billion":1000000000}
    return value_dict[word]

def parse_word_syntax(string):
    amounts = r"thousand|million|billion"
    number = r"\d+(,\d{3})*\.*\d*"
    word_re = rf"\${number}(-|\sto\s)?({number})?\s({amounts})"
    value_re = rf"\${number}"
    value = get_numerical_value(string)
    word = re.search(amounts, string, flags=re.I).group().lower()
    word_value = word_to_value(word)
    return value * word_value

def parse_value_syntax(string):  
    return get_numerical_value(string)

def money_conversion(money):
    """ 
    Given either a string or a list of strings as input, return
    a number (int or float) which is equal to the monetary value

    money_conversion("$12.2 million") ---> 12200000   ## Word syntax
    money_conversion("$790,000) ---> 790000           ## Value syntax

    use test_money_conveersion.py to test your solution

    """
    amounts = r"thousand|million|billion"
    number = r"\d+(,\d{3})*\.*\d*"
    word_re = rf"\${number}(-|\sto\s)?({number})?\s({amounts})"
    value_re = rf"\${number}"
    if money == "N/A":
        return None

    elif isinstance(money, list):
        money = money[0]

    word_syntax = re.search(word_re, money, flags=re.I)
    value_syntax = re.search(value_re, money, flags=re.I)

    if word_syntax:
        return parse_word_syntax(word_syntax.group())

    elif value_syntax:
        return parse_value_syntax(value_syntax.group())

    else:
        return None    

def clean_date(date):
    return date.split("(")[0].strip()

def date_conversion(date):
    if isinstance(date, list):
        date = date[0]
    
    elif date == 'N/A':
        return None
    
    date_str = clean_date(date)

    fmts = ['%B %d, %Y', '%d %B %Y', '%B %Y', '%Y']

    for fmt in fmts:
        try:
            return datetime.strptime(date_str, fmt)
        except:
            pass            
    
    return None

def high_low(dataframe, column):
    """" This function receives a dataframe and calculates the highest and lowest value and the associated title"""
    
    high_column = dataframe[column].max()
    low_column = dataframe[column].min()
    
    high_index = dataframe[dataframe[column] == dataframe[column].max()].index.values.astype(int)
    low_index = dataframe[dataframe[column] == dataframe[column].min()].index.values.astype(int)
    try: 
        high_index = int(high_index)
        low_index = int(low_index)
        high_title = dataframe['title'][high_index]
        low_title = dataframe['title'][low_index]
    except:
        high_title = dataframe['title'][high_index]
        low_title = dataframe['title'][low_index]
    
    return high_column, high_title, low_column, low_title
