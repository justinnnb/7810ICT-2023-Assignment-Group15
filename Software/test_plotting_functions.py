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


# # Test filter_by_period function
# date_inputs = [
#     (pd.Timestamp('2022-01-01'), pd.Timestamp('2022-02-01')),
#     (pd.Timestamp('2022-03-01'), pd.Timestamp('2022-04-01'))
# ]
# @pytest.mark.parametrize("from_date, to_date", date_inputs)
# def test_filter_by_period(from_date, to_date):
#     df = pd.DataFrame({
#         'OFFENCE_MONTH': pd.date_range(start='2021-01-01', end='2022-01-01', freq='M')
#     })
#     filtered_df = filter_by_period(df, from_date, to_date)
#     assert filtered_df is not None

# # Test filter_by_top_10 function
# def test_filter_by_top_10():
#     df = pd.DataFrame({
#         'OFFENCE_CODE': [1, 2, 3, 4, 5],
#         'OFFENCE_DESC': ['Speeding', 'Parking', 'Texting', 'Drinking', 'Eating'],
#         'TOTAL_NUMBER': [10, 20, 30, 40, 50]
#     })
#     top_10_df = filter_by_top_10(df)
#     assert top_10_df is not None

# # Test filter_by_off_desc function
# desc_inputs = ['Speeding', 'Parking', 'Texting']
# @pytest.mark.parametrize("desc", desc_inputs)
# def test_filter_by_off_desc(desc):
#     df = pd.DataFrame({
#         'OFFENCE_DESC': ['Speeding', 'Parking', 'Texting', 'Drinking', 'Eating']
#     })
#     filtered_df = filter_by_off_desc(df, desc)
#     assert filtered_df is not None
