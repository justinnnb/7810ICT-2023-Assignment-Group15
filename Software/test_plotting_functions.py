import pytest
import pandas as pd
from datetime import datetime
from plotting_functions import read_data, filter_by_period, filter_by_top_10, filter_by_off_desc

# Test read_data function
file_names = ['wrong.csv', 'test_data.csv', ' ']
@pytest.mark.parametrize("file_name", file_names)
def test_read_data(file_name):
    try:
        df = read_data(file_name)
        error = False
    except:
        error = True
    assert error == False
#### DONE

# # Test filter_by_period function
date_inputs = [
    (pd.Timestamp('2022-01-01'), pd.Timestamp('2022-02-01')),
    (pd.Timestamp('2022-03-01'), pd.Timestamp('2022-04-01')),
    (pd.Timestamp(''), pd.Timestamp('2022-04-01')),
    (pd.Timestamp('2022-03-01'), pd.Timestamp(''))


]
@pytest.mark.parametrize("from_date, to_date", date_inputs)
def test_filter_by_period(from_date, to_date):
    df = pd.DataFrame({
        'OFFENCE_MONTH': pd.date_range(start='2021-01-01', end='2022-01-01', freq='M')
    })
    filtered_df = filter_by_period(df, from_date, to_date)
    assert filtered_df is not None
# ####DONE


# Test filter_by_top_10 function
def test_filter_by_top_10():
    df = pd.DataFrame({
        'OFFENCE_CODE': [1, 2, 3, 4, 5],
        'OFFENCE_DESC': ['Speeding', 'Parking', 'Texting', 'Drinking', 'Eating'],
        'TOTAL_NUMBER': [10, 20, 30, 40, 50]
    })
    top_10_df = filter_by_top_10(df)
    assert top_10_df is not None

# # Test filter_by_off_desc function
desc_inputs = ['Speeding', 'Parking', 'Texting']
@pytest.mark.parametrize("desc", desc_inputs)
def test_filter_by_off_desc(desc):
    df = pd.DataFrame({
        'OFFENCE_DESC': ['Speeding', 'Parking', 'Texting', 'Drinking', 'Eating']
    })
    filtered_df = filter_by_off_desc(df, desc)
    assert filtered_df is not None


##############
##############
##############ADDITIONAL TESTS
##############
##############
# 1. File exists and has correct format
def test_read_data_valid_file():
    df = read_data("test_data.csv")  # Assuming you have a test_data.csv that is valid
    assert isinstance(df, pd.DataFrame)

# 2. File does not exist
def test_read_data_file_not_exist():
    df = read_data("file_not_exist.csv")
    assert df == "File not found or wrong file type."

# 3. File has incorrect format (e.g., JSON instead of CSV)
def test_read_data_wrong_format():
    df = read_data("wrong_format.json")  # Assuming you have a wrong_format.json
    assert df == "File not found or wrong file type."

# 4. Check returned DataFrame columns
def test_read_data_columns():
    df = read_data("test_data.csv")  # Assuming test_data.csv exists and is well-formatted
    expected_columns = ['OFFENCE_MONTH', 'OFFENCE_CODE', 'OFFENCE_DESC', 'LEGISLATION', 'CAMERA_IND', 'LOCATION_CODE',
                        'LOCATION_DETAILS', 'SPEED_CAMERA_IND', 'RED_LIGHT_CAMERA_IND', 'CAMERA_TYPE',
                        'TOTAL_NUMBER', 'TOTAL_VALUE']
    assert list(df.columns) == expected_columns

# 5. Check if OFFENCE_MONTH is converted to datetime
def test_read_data_datetime_conversion():
    df = read_data("test_data.csv")
    assert pd.api.types.is_datetime64_any_dtype(df['OFFENCE_MONTH'])