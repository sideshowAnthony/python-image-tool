#!/usr/bin/env python

# Developed using wx version 2.8.12.1
import wx
from Controller import Controller

class MainWindow(wx.Frame):

	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(450,560))
		bkg = wx.Panel(self)
		
		self.chDimension = wx.Choice(self)
		self.chRotation = wx.Choice(self)
		self.btnOpen = wx.Button(self, label='Choose image/s')
		self.txtLog = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE, size=[415,400])
		
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sizer.Add(self.chDimension, proportion=0, flag=wx.ALL, border=5)
		self.sizer.Add(self.chRotation, proportion=0, flag=wx.ALL, border=5)
		self.sizer.Add(self.btnOpen, proportion=0, flag=wx.ALL, border=5)
		self.sizer.Add(self.txtLog, proportion=0, flag=wx.ALL, border=5)

		self.panel_sizer = wx.BoxSizer()
		self.panel_sizer.Add(self.sizer, flag=wx.EXPAND | wx.ALL, border=10)

		bkg.SetSizer(self.panel_sizer)
		self.AppendToLog('1.Select dimensions')
		self.AppendToLog('2.Set rotation - if any')
		self.AppendToLog('3.Choose image/s to work on')
		self.AppendToLog('4.Wait for image/s to copy')

		bkg.Show(True)		
		self.Show(True)
		
		self.Controller = Controller(self)
		
		self.btnOpen.Bind(wx.EVT_BUTTON, self.ProcessImages)

	def AppendToLog(self, message):
		self.txtLog.AppendText('\n'+message)
		
	def SetDimensionOptions(self, dimensionOptions):
		client_data = 0
		for i in dimensionOptions:
			self.chDimension.Append('Dimension:'+`i[0]`+'x'+`i[1]`, client_data)
			client_data = client_data+1
		self.chDimension.SetSelection(0)
		self.chDimension.SetInitialSize()
		
	def SetRotationOptions(self, rotationOptions):
		client_data = 0
		for option in rotationOptions:
			self.chRotation.Append('Rotate:'+option, client_data)
			client_data = client_data+1
		self.chRotation.SetSelection(0)
		self.chRotation.SetInitialSize()
		
	def ProcessImages(self, event):
		dlg = wx.FileDialog(self, "Choose image/s", '/home/anthony/Dropbox/Python/Image Tool', "", "*.*", wx.OPEN | wx.FD_MULTIPLE)
		if dlg.ShowModal() != wx.ID_OK:
			return
					
		directory = dlg.GetDirectory()
		filenames = dlg.GetFilenames()
		n = self.chDimension.GetSelection()
		d_index = self.chDimension.GetClientData(n)
		n = self.chRotation.GetSelection()
		r_index = self.chRotation.GetClientData(n)
		self.Controller.ProcessImages(directory, filenames, d_index, r_index)
		dlg.Destroy()


app = wx.App(False)
frame = MainWindow(None, "teamug Image Tool")
app.MainLoop()