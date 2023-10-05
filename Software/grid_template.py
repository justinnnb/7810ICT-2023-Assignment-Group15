# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-376-g11d0e737)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import wx.adv
import wx.grid

mainNotebook = 1000

###########################################################################
## Class MainApp
###########################################################################

class MainApp ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"New South Wales Traffic and Panalty Analysis Tool", pos = wx.DefaultPosition, size = wx.Size( 1024,640 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		main_container = wx.BoxSizer( wx.VERTICAL )

		# self.main_notebook = wx.aui.AuiNotebook( self, mainNotebook, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		# delete close button
		self.main_notebook = wx.aui.AuiNotebook(self, mainNotebook, wx.DefaultPosition, wx.DefaultSize,
												wx.aui.AUI_NB_TAB_SPLIT | wx.aui.AUI_NB_TAB_MOVE | wx.aui.AUI_NB_SCROLL_BUTTONS)

		self.panel_1 = wx.Panel( self.main_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.main_notebook.AddPage( self.panel_1, u"Home", False, wx.NullBitmap )
		self.panel_2 = wx.Panel( self.main_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		boxGeneralReport = wx.BoxSizer( wx.VERTICAL )

		boxDatePicker = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1_panel2 = wx.StaticText( self.panel_2, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1_panel2.Wrap( -1 )

		boxDatePicker.Add( self.m_staticText1_panel2, 0, wx.ALL, 5 )

		self.m_datePicker1_panel2 = wx.adv.DatePickerCtrl( self.panel_2, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 100,-1 ), wx.adv.DP_DEFAULT )
		boxDatePicker.Add( self.m_datePicker1_panel2, 0, wx.ALL, 5 )

		self.m_staticText2_panel2 = wx.StaticText( self.panel_2, wx.ID_ANY, u"To:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2_panel2.Wrap( -1 )

		boxDatePicker.Add( self.m_staticText2_panel2, 0, wx.ALL, 5 )

		self.m_datePicker2_panel2 = wx.adv.DatePickerCtrl( self.panel_2, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 100,-1 ), wx.adv.DP_DEFAULT )
		boxDatePicker.Add( self.m_datePicker2_panel2, 0, wx.ALL, 5 )

		self.m_button1_panel2 = wx.Button( self.panel_2, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxDatePicker.Add( self.m_button1_panel2, 0, wx.ALL, 5 )


		boxGeneralReport.Add( boxDatePicker, 0, wx.ALIGN_CENTER, 5 )

		boxGrid = wx.BoxSizer( wx.HORIZONTAL )

		self.resultGrid = wx.grid.Grid( self.panel_2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.resultGrid.CreateGrid( 5, 5 )
		self.resultGrid.EnableEditing( True )
		self.resultGrid.EnableGridLines( True )
		self.resultGrid.EnableDragGridSize( False )
		self.resultGrid.SetMargins( 0, 0 )

		# Columns
		self.resultGrid.SetColSize( 0, 80 )
		self.resultGrid.SetColSize( 1, 80 )
		self.resultGrid.SetColSize( 2, 80 )
		self.resultGrid.SetColSize( 3, 80 )
		self.resultGrid.SetColSize( 4, 186 )
		self.resultGrid.EnableDragColMove( False )
		self.resultGrid.EnableDragColSize( True )
		self.resultGrid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.resultGrid.EnableDragRowSize( True )
		self.resultGrid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.resultGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		boxGrid.Add( self.resultGrid, 1, wx.ALL|wx.EXPAND, 5 )


		boxGeneralReport.Add( boxGrid, 1, wx.EXPAND, 5 )


		self.panel_2.SetSizer( boxGeneralReport )
		self.panel_2.Layout()
		boxGeneralReport.Fit( self.panel_2 )
		self.main_notebook.AddPage( self.panel_2, u"Overall report", False, wx.NullBitmap )
		self.panel_3 = wx.Panel( self.main_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1_panel3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_canvas1_panel3 = wx.Panel( self.panel_3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1_panel3.Add( self.m_canvas1_panel3, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer12_panel3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1_panel3 = wx.StaticText( self.panel_3, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1_panel3.Wrap( -1 )

		bSizer12_panel3.Add( self.m_staticText1_panel3, 0, wx.ALL, 5 )

		self.m_datePicker1_panel3 = wx.adv.DatePickerCtrl( self.panel_3, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		bSizer12_panel3.Add( self.m_datePicker1_panel3, 0, wx.ALL, 5 )

		self.m_staticText2_panel3 = wx.StaticText( self.panel_3, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2_panel3.Wrap( -1 )

		bSizer12_panel3.Add( self.m_staticText2_panel3, 0, wx.ALL, 5 )

		self.m_datePicker2_panel3 = wx.adv.DatePickerCtrl( self.panel_3, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		bSizer12_panel3.Add( self.m_datePicker2_panel3, 0, wx.ALL, 5 )

		self.m_button1_panel3 = wx.Button( self.panel_3, wx.ID_ANY, u"Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12_panel3.Add( self.m_button1_panel3, 0, wx.ALL, 5 )


		bSizer1_panel3.Add( bSizer12_panel3, 0, wx.EXPAND, 5 )


		self.panel_3.SetSizer( bSizer1_panel3 )
		self.panel_3.Layout()
		bSizer1_panel3.Fit( self.panel_3 )
		self.main_notebook.AddPage( self.panel_3, u"Chart Distribution", False, wx.NullBitmap )
		self.panel_4 = wx.Panel( self.main_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		boxCaseCaptured = wx.BoxSizer( wx.VERTICAL )

		boxDatePickertab4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText71 = wx.StaticText( self.panel_4, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )

		boxDatePickertab4.Add( self.m_staticText71, 0, wx.ALL, 5 )

		self.datePickerTab4From = wx.adv.DatePickerCtrl( self.panel_4, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 100,-1 ), wx.adv.DP_DEFAULT )
		boxDatePickertab4.Add( self.datePickerTab4From, 0, wx.ALL, 5 )

		self.m_staticText81 = wx.StaticText( self.panel_4, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		boxDatePickertab4.Add( self.m_staticText81, 0, wx.ALL, 5 )

		self.datePickerTab4To = wx.adv.DatePickerCtrl( self.panel_4, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 100,-1 ), wx.adv.DP_DEFAULT )
		boxDatePickertab4.Add( self.datePickerTab4To, 0, wx.ALL, 5 )

		self.checkBoxRadar = wx.CheckBox( self.panel_4, wx.ID_ANY, u"Radar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.checkBoxRadar.SetValue(True)
		boxDatePickertab4.Add( self.checkBoxRadar, 0, wx.ALL, 5 )

		self.checkBoxCamera = wx.CheckBox( self.panel_4, wx.ID_ANY, u"Camera", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxDatePickertab4.Add( self.checkBoxCamera, 0, wx.ALL, 5 )

		self.checkBoxLidar = wx.CheckBox( self.panel_4, wx.ID_ANY, u"Lidar", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxDatePickertab4.Add( self.checkBoxLidar, 0, wx.ALL, 5 )

		self.buttonSubmitTab4 = wx.Button( self.panel_4, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxDatePickertab4.Add( self.buttonSubmitTab4, 0, wx.ALL, 5 )


		boxCaseCaptured.Add( boxDatePickertab4, 0, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( self.panel_4, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer12.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.inputBoxDescTab4 = wx.TextCtrl( self.panel_4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		bSizer12.Add( self.inputBoxDescTab4, 0, wx.ALL, 5 )


		boxCaseCaptured.Add( bSizer12, 0, wx.EXPAND, 5 )

		boxGridtab4 = wx.BoxSizer( wx.VERTICAL )

		self.resultGridTab4 = wx.grid.Grid( self.panel_4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.resultGridTab4.CreateGrid( 5, 5 )
		self.resultGridTab4.EnableEditing( True )
		self.resultGridTab4.EnableGridLines( True )
		self.resultGridTab4.EnableDragGridSize( False )
		self.resultGridTab4.SetMargins( 0, 0 )

		# Columns
		self.resultGridTab4.SetColSize( 0, 80 )
		self.resultGridTab4.SetColSize( 1, 80 )
		self.resultGridTab4.SetColSize( 2, 80 )
		self.resultGridTab4.SetColSize( 3, 80 )
		self.resultGridTab4.SetColSize( 4, 186 )
		self.resultGridTab4.EnableDragColMove( False )
		self.resultGridTab4.EnableDragColSize( True )
		self.resultGridTab4.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.resultGridTab4.EnableDragRowSize( True )
		self.resultGridTab4.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.resultGridTab4.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		boxGridtab4.Add( self.resultGridTab4, 1, wx.ALL|wx.EXPAND, 5 )


		boxCaseCaptured.Add( boxGridtab4, 1, wx.EXPAND, 5 )


		self.panel_4.SetSizer( boxCaseCaptured )
		self.panel_4.Layout()
		boxCaseCaptured.Fit( self.panel_4 )
		self.main_notebook.AddPage( self.panel_4, u"Cases Captured", False, wx.NullBitmap )
		self.panel_5 = wx.Panel( self.main_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1_panel5 = wx.BoxSizer( wx.VERTICAL )

		bSizer3_panel5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2_panel5 = wx.StaticText( self.panel_5, wx.ID_ANY, u"Offence Codes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2_panel5.Wrap( -1 )

		bSizer3_panel5.Add( self.m_staticText2_panel5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_comboBox1Choices = []
		self.m_comboBox1 = wx.ComboBox( self.panel_5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		bSizer3_panel5.Add( self.m_comboBox1, 0, wx.ALL, 5 )

		self.m_staticText3_panel5 = wx.StaticText( self.panel_5, wx.ID_ANY, u"From", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3_panel5.Wrap( -1 )

		bSizer3_panel5.Add( self.m_staticText3_panel5, 0, wx.ALL, 5 )

		self.m_datePicker1_panel5 = wx.adv.DatePickerCtrl( self.panel_5, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 100,-1 ), wx.adv.DP_DEFAULT )
		bSizer3_panel5.Add( self.m_datePicker1_panel5, 0, wx.ALL, 5 )

		self.m_staticText4_panel5 = wx.StaticText( self.panel_5, wx.ID_ANY, u"To", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4_panel5.Wrap( -1 )

		bSizer3_panel5.Add( self.m_staticText4_panel5, 0, wx.ALL, 5 )

		self.m_datePicker2_panel5 = wx.adv.DatePickerCtrl( self.panel_5, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 100,-1 ), wx.adv.DP_DEFAULT )
		bSizer3_panel5.Add( self.m_datePicker2_panel5, 0, wx.ALL, 5 )

		self.m_button2_panel5 = wx.Button( self.panel_5, wx.ID_ANY, u"Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3_panel5.Add( self.m_button2_panel5, 0, wx.ALL, 5 )


		bSizer1_panel5.Add( bSizer3_panel5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer4_panel5 = wx.BoxSizer( wx.VERTICAL )

		self.m_canvas1_panel5 = wx.Panel( self.panel_5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4_panel5.Add( self.m_canvas1_panel5, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer1_panel5.Add( bSizer4_panel5, 1, wx.EXPAND, 5 )


		self.panel_5.SetSizer( bSizer1_panel5 )
		self.panel_5.Layout()
		bSizer1_panel5.Fit( self.panel_5 )
		self.main_notebook.AddPage( self.panel_5, u"Cases Analysis", False, wx.NullBitmap )
		self.panel_6 = wx.Panel( self.main_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		boxFinancialAnalysis = wx.BoxSizer( wx.VERTICAL )

		boxDatePickertab41 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText711 = wx.StaticText( self.panel_6, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText711.Wrap( -1 )

		boxDatePickertab41.Add( self.m_staticText711, 0, wx.ALL, 5 )

		self.datePickerTab6From = wx.adv.DatePickerCtrl( self.panel_6, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 100,-1 ), wx.adv.DP_DEFAULT )
		boxDatePickertab41.Add( self.datePickerTab6From, 0, wx.ALL, 5 )

		self.m_staticText811 = wx.StaticText( self.panel_6, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText811.Wrap( -1 )

		boxDatePickertab41.Add( self.m_staticText811, 0, wx.ALL, 5 )

		self.datePickerTab6To = wx.adv.DatePickerCtrl( self.panel_6, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 100,-1 ), wx.adv.DP_DEFAULT )
		boxDatePickertab41.Add( self.datePickerTab6To, 0, wx.ALL, 5 )


		boxFinancialAnalysis.Add( boxDatePickertab41, 0, wx.EXPAND, 5 )

		bSizer121 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText51 = wx.StaticText( self.panel_6, wx.ID_ANY, u"Categories:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		bSizer121.Add( self.m_staticText51, 0, wx.ALL, 5 )

		m_choice11Choices = []
		self.m_choice11 = wx.Choice( self.panel_6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice11Choices, 0 )
		self.m_choice11.SetSelection( 0 )
		bSizer121.Add( self.m_choice11, 0, wx.ALL, 5 )

		self.buttonSubmitTab41 = wx.Button( self.panel_6, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer121.Add( self.buttonSubmitTab41, 0, wx.ALL, 5 )


		boxFinancialAnalysis.Add( bSizer121, 0, wx.EXPAND, 5 )

		boxGridtab41 = wx.BoxSizer( wx.VERTICAL )

		self.resultGridTab6 = wx.grid.Grid( self.panel_6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.resultGridTab6.CreateGrid( 5, 5 )
		self.resultGridTab6.EnableEditing( True )
		self.resultGridTab6.EnableGridLines( True )
		self.resultGridTab6.EnableDragGridSize( False )
		self.resultGridTab6.SetMargins( 0, 0 )

		# Columns
		self.resultGridTab6.SetColSize( 0, 80 )
		self.resultGridTab6.SetColSize( 1, 80 )
		self.resultGridTab6.SetColSize( 2, 80 )
		self.resultGridTab6.SetColSize( 3, 80 )
		self.resultGridTab6.SetColSize( 4, 186 )
		self.resultGridTab6.EnableDragColMove( False )
		self.resultGridTab6.EnableDragColSize( True )
		self.resultGridTab6.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.resultGridTab6.EnableDragRowSize( True )
		self.resultGridTab6.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.resultGridTab6.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		boxGridtab41.Add( self.resultGridTab6, 1, wx.ALL|wx.EXPAND, 5 )


		boxFinancialAnalysis.Add( boxGridtab41, 1, wx.EXPAND, 5 )


		self.panel_6.SetSizer( boxFinancialAnalysis )
		self.panel_6.Layout()
		boxFinancialAnalysis.Fit( self.panel_6 )
		self.main_notebook.AddPage( self.panel_6, u"Financial Analysis", True, wx.NullBitmap )

		main_container.Add( self.main_notebook, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( main_container )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1_panel2.Bind( wx.EVT_BUTTON, self.onShowTablePanel2 )
		self.m_button1_panel3.Bind( wx.EVT_BUTTON, self.onPlotPanel3 )
		self.buttonSubmitTab4.Bind( wx.EVT_BUTTON, self.onShowTablePanel4 )
		self.m_button2_panel5.Bind( wx.EVT_BUTTON, self.onPlotPanel5 )
		self.buttonSubmitTab41.Bind( wx.EVT_BUTTON, self.onShowTablePanel6 )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def onShowTablePanel2( self, event ):
		event.Skip()

	def onPlotPanel3( self, event ):
		event.Skip()

	def onShowTablePanel4( self, event ):
		event.Skip()

	def onPlotPanel5( self, event ):
		event.Skip()

	def onShowTablePanel6( self, event ):
		event.Skip()


