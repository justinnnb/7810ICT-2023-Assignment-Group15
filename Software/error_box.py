# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-370-gc831f1f7)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class errorDialog
###########################################################################

class errorDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"An error has occured!", pos = wx.DefaultPosition, size = wx.Size(1000,1000), style = wx.DEFAULT_DIALOG_STYLE )

        # self.SetSizeHints( wx.Size( 1000,1000 ), wx.DefaultSize )
        # Remove the explicit size setting or set a smaller default size
        # self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)


        bSizer21 = wx.BoxSizer( wx.VERTICAL )

        bSizer23 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel9.SetMaxSize( wx.Size( -1,50 ) )

        bSizer23.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Error Message:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )

        bSizer23.Add( self.m_staticText20, 0, wx.ALL, 5 )

        self.errorMessage = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.errorMessage.Wrap( -1 )

        bSizer23.Add( self.errorMessage, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer21.Add( bSizer23, 1, wx.EXPAND, 5 )

        bSizer22 = wx.BoxSizer( wx.VERTICAL )

        self.m_button6 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer22.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer21.Add( bSizer22, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer21 )
        self.Layout()
        bSizer21.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button6.Bind( wx.EVT_BUTTON, self.onDestroy )

    def __del__( self ):
        pass
    def set_error_message(self, error_message):
        self.errorMessage.SetLabel(error_message)


    def onDestroy(self, event):
        self.Destroy()


