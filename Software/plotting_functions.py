import pandas as pd
from datetime import datetime
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


def read_data(file_name):
    cols_name: list = ['OFFENCE_MONTH', 'OFFENCE_CODE', 'OFFENCE_DESC', 'LEGISLATION', 'CAMERA_IND', 'LOCATION_CODE',
                       'LEGISLATION', 'LOCATION_DETAILS', 'SPEED_CAMERA_IND', 'RED_LIGHT_CAMERA_IND', 'CAMERA_TYPE',
                       'TOTAL_NUMBER', 'TOTAL_VALUE']
    df = pd.read_csv(file_name, usecols=cols_name)
    df['OFFENCE_MONTH'] = pd.to_datetime(df['OFFENCE_MONTH'], format='%m/%d/%Y')
    return df


def filter_by_period(df, from_date, to_date):
    """Filter the data based on date range."""
    # start_date = self.m_datePicker1.GetValue().FormatISODate()
    # end_date = self.m_datePicker2.GetValue().FormatISODate()
    from_wx_date = from_date.GetValue()
    to_wx_date = to_date.GetValue()

    # Convert wx.DateTime to Python datetime
    # from_date = datetime.fromtimestamp(from_date.GetTicks())
    # to_date = datetime.fromtimestamp(to_date.GetTicks())
    from_date = datetime.fromtimestamp(from_wx_date.GetTicks())
    to_date = datetime.fromtimestamp(to_wx_date.GetTicks())

    # Format the datetime object as a string in the format "20/09/2023"
    from_date = from_date.strftime('%d/%m/%Y')
    to_date = to_date.strftime('%d/%m/%Y')
    start_date = datetime.strptime(from_date, '%d/%m/%Y')
    end_date = datetime.strptime(to_date, '%d/%m/%Y')

    # Assuming the date column in your dataframe is named 'Date'
    # self.original_df['OFFENCE_MONTH'] = pd.to_datetime(self.original_df['OFFENCE_MONTH'], format='%m/%d/%Y')

    filtered_df = df[(df['OFFENCE_MONTH'] >= start_date) & (df['OFFENCE_MONTH'] <= end_date)]

    # print(filtered_df)

    # self.load_csv_to_grid_from_df(filtered_df)  # /////////// Using a new method to load data from DataFrame
    return filtered_df


import matplotlib.pyplot as plt

import matplotlib.pyplot as plt


import matplotlib.pyplot as plt


import matplotlib.pyplot as plt

def plot_data_line(df, selected_offence_code=None):
    if df.empty:
        # If the dataframe is empty, create a white figure with the specified message
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.text(0.5, 0.5, "No data in the selected timeframe", ha='center', va='center', fontsize=12)
        ax.axis('off')  # Turn off axis
    else:
        # Sort dataframe by 'OFFENCE_MONTH' column in ascending order
        df = df.sort_values(by='OFFENCE_MONTH')

        # Extract 'OFFENCE_MONTH' and 'total value' columns from the dataframe
        x = df['OFFENCE_MONTH'].dt.strftime('%d/%m/%Y')  # Convert dates to 'Day/Month/Year' format
        y = df['TOTAL_VALUE']

        # Line plot
        fig, ax = plt.subplots(figsize=(10, 5))
        print(df['OFFENCE_DESC'])
        ax.plot(x, y, 'ro-.', label=f"{selected_offence_code}: {df['OFFENCE_DESC'].iloc[1]}")  # Use the first description as the label
        ax.set_title(f"Data for: {selected_offence_code}")
        ax.set_xlabel('Day/Month/Year')
        ax.set_ylabel('# of Occurrences')
        ax.set_xticks(x)
        ax.set_xticklabels(x, rotation=45)
        ax.legend()
        plt.tight_layout()  # Adjust subplot parameters to give specified padding

    return fig




def plot_data_pie(df):
    if len(df) == 0:
        figure_empty = Figure(figsize=(6, 6))
        ax = figure_empty.add_subplot(1, 1, 1)
        ax.text(0.5, 0.5, 'There is no data within the timeframe',
                horizontalalignment='center',
                verticalalignment='center',
                transform=ax.transAxes)
        ax.axis('off')  # Turn off axis
        return figure_empty

    df_top_10 = filter_by_top_10(df)

    # Combining offence_code and offence_description for labels
    combined_labels = df_top_10['OFFENCE_CODE'].astype(str) + " - " + df_top_10['OFFENCE_DESC']

    # If the label is too long, split it into two lines for the legend
    max_length = 35
    wrapped_labels = ['\n'.join([label[i:i + max_length] for i in range(0, len(label), max_length)]) for label in
                      combined_labels]

    sizes = df_top_10['TOTAL_NUMBER']  # Total numbers as sizes

    figure_pie = Figure(figsize=(8, 6))
    axes = figure_pie.add_subplot(1, 1, 1)
    wedges, texts, autotexts = axes.pie(sizes, labels=df_top_10['OFFENCE_CODE'].astype(str), autopct='%1.1f%%',
                                        startangle=90)
    axes.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Adjust the position of the pie chart to be more to the left
    axes.set_position([0.1, 0.1, 0.55, 0.75])

    # Adjust legend to be closer to the pie chart
    axes.legend(wedges, wrapped_labels, title="Offence Codes and Descriptions", loc="center left",
                bbox_to_anchor=(1.1, 0.5), fontsize='small', ncol=1)

    axes.set_title("Top 10 Offence Cases in the selected timeframe", fontweight='bold', fontsize=14)

    return figure_pie


def filter_by_top_10(df):
    # Grouping by offence_code and offence_desc and summing total_number
    selected_df = df[['OFFENCE_CODE', 'OFFENCE_DESC', 'TOTAL_NUMBER']]
    grouped_df = selected_df.groupby(['OFFENCE_CODE', 'OFFENCE_DESC']).sum().reset_index()

    # Sorting the dataframe by TOTAL_NUMBER in descending order and selecting top 10
    top_10_df = grouped_df.sort_values(by='TOTAL_NUMBER', ascending=False).head(10).reset_index(drop=True)

    return top_10_df


def filter_by_off_desc(df, desc):
    filtered_df = df[df['OFFENCE_DESC'].str.contains(desc)]
    return filtered_df

def filter_by_phone(df):
    filtered_df = df[df['OFFENCE_DESC'].str.contains('mobile|phone', case=False, na=False)]
    return filtered_df


def filter_by_off_code(df, code):
    filtered_df = df[df['OFFENCE_CODE'].astype(str).str.contains(str(code))]
    return filtered_df


def filter_by_camera_radar(df, camera_checked, lidar_checked, radar_checked):
    conditions = []

    if camera_checked:
        conditions.append(df['CAMERA_TYPE'].notna())
        conditions.append(df['OFFENCE_DESC'].str.contains("Camera", case=False, na=False))

    if lidar_checked:
        conditions.append(df['OFFENCE_DESC'].str.contains("Lidar", case=False, na=False))

    if radar_checked:
        conditions.append(df['OFFENCE_DESC'].str.contains("Radar", case=False, na=False))
        conditions.append(df['SPEED_CAMERA_IND'].notna())

    if not conditions:  # if no checkboxes are selected
        return df  # or you can return an empty DataFrame with df.iloc[0:0]

    final_condition = conditions[0]
    for condition in conditions[1:]:
        final_condition |= condition  # Combine using OR

    filtered_df = df[final_condition]

    return filtered_df


def group_total_fees_by_column_name(df, column_name):
    filtered_df = df.groupby([column_name])['TOTAL_VALUE'].sum().reset_index()
    filtered_df = filtered_df.sort_values('TOTAL_VALUE', ascending=False)
    return filtered_df