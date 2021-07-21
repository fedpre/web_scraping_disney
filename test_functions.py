import pytest
import pandas as pd
from datetime import datetime
from functions import money_conversion, minutes_to_int, date_conversion, high_low
from pandas import Timestamp

def test_minutes_to_int():
    assert date_conversion('N/A') is None
    assert minutes_to_int('83 minutes') == 83
    assert minutes_to_int('340 minutes') == 340
    assert minutes_to_int('3 minutes') == 3
    assert minutes_to_int('56') == 56
    assert minutes_to_int('30 min') == 30

def test_date_conversion(): 
    assert date_conversion('N/A') is None
    assert date_conversion('10 July 2021 (worldwide)') == datetime(2021, 7, 10, 0, 0)
    assert date_conversion('10 July 2021') == datetime(2021, 7, 10, 0, 0)
    assert date_conversion('July 2021 (world wide)') == datetime(2021, 7, 1, 0, 0)
    assert date_conversion('July 2021') == datetime(2021, 7, 1, 0, 0)
    assert date_conversion('2021 (world wide)') == datetime(2021, 1, 1, 0, 0)
    assert date_conversion('2021') == datetime(2021, 1, 1, 0, 0)
    assert date_conversion('July 10, 2021') == datetime(2021, 7, 10, 0, 0)
    assert date_conversion('July 10, 2021 (world wide)') == datetime(2021, 7, 10, 0, 0)
    assert date_conversion('25 October 1950 (worldwide)') == datetime(1950, 10, 25, 0, 0)
    assert date_conversion('25 October 1950') == datetime(1950, 10, 25, 0, 0)
    assert date_conversion('October 1950 (world wide)') == datetime(1950, 10, 1, 0, 0)
    assert date_conversion('October 1950') == datetime(1950, 10, 1, 0, 0)
    assert date_conversion('1950 (world wide)') == datetime(1950, 1, 1, 0, 0)
    assert date_conversion('1950') == datetime(1950, 1, 1, 0, 0)
    assert date_conversion('October 25, 1950') == datetime(1950, 10, 25, 0, 0)
    assert date_conversion('October 25, 1950 (world wide)') == datetime(1950, 10, 25, 0, 0)

def test_money_conversion():
    assert money_conversion("$3 million") == 3000000
    assert money_conversion("$99 million") == 99000000
    assert money_conversion("$3.5 million") == 3500000
    assert money_conversion("$1.234 million") == 1234000
    assert money_conversion("$1.25 billion") == 1250000000
    assert money_conversion("$900.9 thousand") == 900900
    assert money_conversion("$3.5-4 million") == 3500000
    assert money_conversion("$3.5 to 4 million") == 3500000
    assert money_conversion("$950000") == 950000
    assert money_conversion("$127,850,000") == 127850000
    assert money_conversion("$10,000,000.50") == 10000000.5
    assert money_conversion("estimated $5,000,000 (USD)") == 5000000
    assert money_conversion("60 million Norwegian Kroner (around $8.7 million in 1989)") == 8700000
    assert money_conversion(['$410.6 million (gross)', '$378.5 million (net']) == 410600000
    assert money_conversion('70 crore') is None

movie_list = [{'title': 'Academy Award Review of',
  'Running time (int)': 41,
  'Budget (float)': None,
  'Box office (float)': 45472000.0,
  'Release date (datetime)': datetime(1937, 5, 19, 0, 0)},
 {'title': 'Snow White and the Seven Dwarfs',
  'Running time (int)': 83,
  'Budget (float)': 1490000.0,
  'Box office (float)': 418000000.0,
  'Release date (datetime)': datetime(1937, 12, 21, 0, 0)},
 {'title': 'Pinocchio',
  'Running time (int)': 88,
  'Budget (float)': 2600000.0,
  'Box office (float)': 164000000.0,
  'Release date (datetime)': datetime(1940, 2, 7, 0, 0)},
 {'title': 'Fantasia',
  'Running time (int)': 126,
  'Budget (float)': 2280000.0,
  'Box office (float)': 83300000.0,
  'Release date (datetime)': datetime(1940, 11, 13, 0, 0)},
 {'title': 'The Reluctant Dragon',
  'Running time (int)': 74,
  'Budget (float)': 600000.0,
  'Box office (float)': 960000.0,
  'Release date (datetime)': datetime(1941, 6, 27, 0, 0)}]

df = pd.DataFrame(data=movie_list)

def test_high_low_budget(): 
    assert high_low(df,'Budget (float)') == (2600000.0, 'Pinocchio', 600000.0, 'The Reluctant Dragon')
    assert high_low(df,'Box office (float)') == (418000000.0, 'Snow White and the Seven Dwarfs', 960000.0, 'The Reluctant Dragon')
    assert high_low(df,'Running time (int)') == (126, 'Fantasia', 41, 'Academy Award Review of')
    assert high_low(df,'Release date (datetime)') == (Timestamp('1941-06-27 00:00:00'), 'The Reluctant Dragon', Timestamp('1937-05-19 00:00:00'), 'Academy Award Review of')
    

pytest.main(["-v", "--tb=line", "-rN", "test_functions.py"])