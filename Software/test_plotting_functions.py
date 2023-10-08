import pytest
import pandas as pd
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt 
from matplotlib.figure import Figure
from plotting_functions_for_testing import *

####Test Cases
empty_df = pd.DataFrame()
non_empty_df = pd.DataFrame({
    'OFFENCE_MONTH': pd.date_range(start='2021-01-01', periods=4, freq='D'),  
    'OFFENCE_DESC': ['Speeding', 'Red Light', 'Over Limit', 'No Seatbelt'], 
    'TOTAL_VALUE': [100, 200, 150, 50],  
    'OFFENCE_CODE': [123123, 200, "str_code", 999],
    'TOTAL_NUMBER': [100, 200, 300, 400] 
})

date_inputs = [
    (pd.Timestamp('2022-01-01'), pd.Timestamp('2022-02-01')),
    (wx.DateTime(2025, 1, 1), wx.DateTime(2025, 2, 1)),
    (pd.Timestamp('2022-03-01'), pd.Timestamp('2022-04-01')),
    (pd.Timestamp(''), pd.Timestamp('2022-04-01')),
    (pd.Timestamp('2022-03-01'), pd.Timestamp(''))
]

tests = [
    (empty_df, True),
    (non_empty_df, False),
]

desc_inputs = ['', '2', '--', 'x']


fees_test = [
    (pd.DataFrame({'OFFENCE_DESC': ['Speeding', 'Red Light', 'Over Limit', 'No Seatbelt'] }), 'OFFENCE_DESC',  "No TOTAL_VALUE Column in Dataframe"),
    (non_empty_df, 'OFFENCE_MONTH', pd.DataFrame)
]


df_phone = pd.DataFrame({
    'OFFENCE_DESC': ['mobile usage', 'Phone usage', 'speeding', 'null', None]
})

df_code = pd.DataFrame({
    'OFFENCE_CODE': [123, '123', 124, '125', '126a']
})


filter_by_phone_cases = [
    (df_phone, 2), 
    (pd.DataFrame({'OFFENCE_DESC': ['speeding', 'drinking']}), 0), 
    (pd.DataFrame({'OFFENCE_DESC': ['Mobile', 'PHONE']}), 2), 
    (pd.DataFrame({'OFFENCE_DESC': [None, 'speeding']}), 0) 
]

df_camera_radar = pd.DataFrame({
    'OFFENCE_DESC': ['Camera Speeding', 'Lidar Speeding', 'Radar Speeding', 'Normal Speeding'],
    'CAMERA_TYPE': [1, None, None, None],
    'SPEED_CAMERA_IND': [None, None, 1, None]
})

file_inputs = [("test_data.csv", pd.DataFrame), ("file_not_exist.csv", "File not found or wrong file type."), ("wrong_format.json", "File not found or wrong file type.")]

##### TEST DATA END
##### TEST DATA END
##### TEST DATA END
##### TEST DATA END
##### TEST DATA END

# Test for read_data
@pytest.mark.parametrize("file_name, expected_output", file_inputs)
def test_read_data(file_name, expected_output):
    df = read_data(file_name)
    if isinstance(expected_output, type):
        assert isinstance(non_empty_df, expected_output)
    else:
        assert df == expected_output

# Test filter_by_period function
@pytest.mark.parametrize("from_date, to_date", date_inputs)
def test_filter_by_period(from_date, to_date):
    try:
        filtered_df = filter_by_period(non_empty_df, from_date, to_date)
        assert isinstance(filtered_df, pd.DataFrame)
    except: 
        assert filtered_df is not None

@pytest.mark.parametrize("input_df, is_empty", tests)
def test_plot_data_line(input_df, is_empty):
    result = plot_data_line(input_df)
    if is_empty:
        assert result == "Plot is empty"
    else:
        assert isinstance(result, plt.Figure)  # Check if the returned object is a matplotlib Figure

@pytest.mark.parametrize("input_df, is_empty", tests)
def test_plot_data_pie(input_df, is_empty):
    result = plot_data_pie(input_df)
    
    if is_empty:
        ax = result.get_axes()[0]
        text_elements = [child.get_text() for child in ax.get_children() if isinstance(child, matplotlib.text.Text)]
        assert 'There is no data within the timeframe' in text_elements
    else:
        assert isinstance(result, Figure)  # Check if the returned object is a matplotlib Figure

@pytest.mark.parametrize("input_df, is_empty", tests)
def test_filter_by_top_10(input_df, is_empty):
    result = filter_by_top_10(input_df)
    if is_empty:
        assert result == None  
    else:
        assert len(result) <= 10  
        assert result['TOTAL_NUMBER'].is_monotonic_decreasing  



@pytest.mark.parametrize("desc", desc_inputs)
def test_filter_by_off_desc(desc):
    filtered_df = filter_by_off_desc(non_empty_df, desc)
    assert filtered_df is not None


# Test for read_data_columns
@pytest.mark.parametrize("file_name", ["test_data.csv"])
def test_read_data_columns(file_name):
    df = read_data(file_name)  # Assuming test_data.csv exists and is well-formatted
    expected_columns = ['OFFENCE_MONTH', 'OFFENCE_CODE', 'OFFENCE_DESC', 'LEGISLATION', 'CAMERA_IND', 'LOCATION_CODE',
                        'LOCATION_DETAILS', 'SPEED_CAMERA_IND', 'RED_LIGHT_CAMERA_IND', 'CAMERA_TYPE',
                        'TOTAL_NUMBER', 'TOTAL_VALUE']
    assert all(column in df.columns for column in expected_columns)


@pytest.mark.parametrize("input_df, column_name, expected_output", fees_test)
def test_group_total_fees_by_column_name(input_df, column_name, expected_output):
    try:
        result = group_total_fees_by_column_name(input_df, column_name)
        assert result == expected_output
    except:
        assert isinstance(result, pd.DataFrame)


# Test Cases for filter_by_phone
@pytest.mark.parametrize("input_df, expected_len", filter_by_phone_cases)
def test_filter_by_phone(input_df, expected_len):
    result = filter_by_phone(input_df)
    assert len(result) == expected_len

# Test Cases for filter_by_off_code
@pytest.mark.parametrize("input_df, code, expected_len", [
    (df_code, 123, 2),  
    (df_code, 127, 0),
    (df_code, '126a', 1) 
])
def test_filter_by_off_code(input_df, code, expected_len):
    result = filter_by_off_code(input_df, code)
    assert len(result) == expected_len

# Test Cases for filter_by_camera_radar
@pytest.mark.parametrize("input_df, camera_checked, lidar_checked, radar_checked, expected_len", [
    (df_camera_radar, False, False, False, 4),  # All Checks False
    (df_camera_radar, True, False, False, 1),   # Only Camera Checked
    (df_camera_radar, False, True, False, 1),   # Only Lidar Checked
    (df_camera_radar, False, False, True, 1),   # Only Radar Checked
    (df_camera_radar, True, True, False, 2)     # Multiple Checks
])
def test_filter_by_camera_radar(input_df, camera_checked, lidar_checked, radar_checked, expected_len):
    result = filter_by_camera_radar(input_df, camera_checked, lidar_checked, radar_checked)
    assert len(result) == expected_len