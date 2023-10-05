import wx
import wx.grid

from data_table import DataTable

import plotting_functions
from grid_template import MainApp

import matplotlib

matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg

filename = "original.csv"
# filename="test_data.csv"
df = plotting_functions.read_data(filename)


class MainFrame(MainApp):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.onShowTablePanel2(None)
        self.onShowTablePanel4(None)
        self.initOffenceCodeByPhone()
        self.initFinancialAnalysis()


        self.Layout()
        self.Show(True)

    def onShowTablePanel2(self, event):
        filtered_df = plotting_functions.filter_by_period(df, self.m_datePicker1_panel2, self.m_datePicker2_panel2)
        table = DataTable(filtered_df)
        self.resultGrid.SetTable(table, takeOwnership=True)
        self.resultGrid.AutoSize()
        self.Layout()

    def onPlotPanel3(self, event):
        filtered_df = plotting_functions.filter_by_period(df, self.m_datePicker1_panel3, self.m_datePicker2_panel3)
        figure_score = plotting_functions.plot_data_pie(filtered_df)
        h, w = self.m_canvas1_panel3.GetSize()
        figure_score.set_size_inches(h / figure_score.get_dpi(), w / figure_score.get_dpi())

        canvas = FigureCanvasWxAgg(self.m_canvas1_panel3, -1, figure_score)
        canvas.SetSize(self.m_canvas1_panel3.GetSize())

        self.Layout()

    def onShowTablePanel4(self, event):
        radar_checked = self.checkBoxRadar.GetValue()
        camera_checked = self.checkBoxCamera.GetValue()
        lidar_checked = self.checkBoxLidar.GetValue()

        filtered_df = plotting_functions.filter_by_period(df, self.datePickerTab4From, self.datePickerTab4To)

        filtered_df = plotting_functions.filter_by_camera_radar(
            filtered_df,
            radar_checked=radar_checked,
            camera_checked=camera_checked,
            lidar_checked=lidar_checked
        )

        desc = self.inputBoxDescTab4.GetValue()  # Read the value of the input box
        filtered_df = plotting_functions.filter_by_off_desc(filtered_df, desc)

        table = DataTable(filtered_df)
        self.resultGridTab4.SetTable(table, takeOwnership=True)
        self.resultGridTab4.AutoSize()
        self.Layout()


    def initOffenceCodeByPhone(self):
        filtered_df = plotting_functions.filter_by_phone(df)

        # Get unique values from 'OFFENCE_CODE' column
        offence_codes = sorted(filtered_df['OFFENCE_CODE'].unique().astype(str).tolist())

        # Initialize m_comboBox1 with the unique offence codes
        self.m_comboBox1.Clear()  # Clear existing items if any
        self.m_comboBox1.AppendItems(offence_codes)  # Add the new list of items
        self.m_comboBox1.SetSelection(0)
    def onPlotPanel5(self, event):

        # Get the selected offence code from m_comboBox1
        selected_offence_code = self.m_comboBox1.GetStringSelection()

        # Check if selected_offence_code is empty
        if not selected_offence_code:
            wx.MessageBox('No offence code selected!', 'Warning', wx.OK | wx.ICON_WARNING)
            return

        # Use the filter_by_off_code function to filter df by the selected offence code
        filtered_by_code_df = plotting_functions.filter_by_off_code(df, selected_offence_code)

        filtered_by_date_df = plotting_functions.filter_by_period(filtered_by_code_df, self.m_datePicker1_panel5,
                                                                  self.m_datePicker2_panel5)

        figure = plotting_functions.plot_data_line(filtered_by_date_df, selected_offence_code)

        # Use the appropriate canvas name (assuming m_canvas1_panel5 is the correct one)

        canvas = FigureCanvasWxAgg(self.m_canvas1_panel5, -1, figure)
        canvas.SetSize(self.m_canvas1_panel5.GetSize())

        self.Layout()


    def initFinancialAnalysis(self):
        categories = ["LOCATION_CODE", "LEGISLATION", "OFFENCE_DESC", "LOCATION_DETAILS"]
        self.m_choice11.Clear()  # Clear existing items if any
        self.m_choice11.AppendItems(categories)  # Add the new list of items
    def onShowTablePanel6(self, event):
        filtered_df = plotting_functions.filter_by_period(df, self.datePickerTab6From, self.datePickerTab6To)
        selected_category = self.m_choice11.GetStringSelection()
        filtered_df = plotting_functions.group_total_fees_by_column_name(filtered_df, selected_category)


        table = DataTable(filtered_df)
        self.resultGridTab6.SetTable(table, takeOwnership=True)
        self.resultGridTab6.AutoSize()
        self.Layout()




if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame(None)
    app.MainLoop()
