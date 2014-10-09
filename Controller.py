import subprocess

# This class controls the program, delegating tasks to other classes
# This is not the file you should execute. Gui.py is.
# It passes data from and to the GUI without knowing how it gets displayed

class Controller():

	dimensionOptions = ( (640,480), (800,600), (1280,960) )
	rotationOptions = ( 'None', 'Left', '180', 'Right' )
	rotationAngles = ( '0', '270', '180', '90' )

	def __init__(self, ui):
		self.ui=ui
		ui.SetDimensionOptions(self.dimensionOptions)
		ui.SetRotationOptions(self.rotationOptions)

	def ProcessImages(self, directory, filenames, d_index, r_index):
		width = self.dimensionOptions[d_index][0]
		height = self.dimensionOptions[d_index][1]
		angle = self.rotationAngles[r_index]
		for f in filenames:
			old_filepath = directory+'/'+f
			new_filename = `width`+'w'+`height`+'h'+angle+'a_'+f
			new_filepath = directory+'/'+new_filename
			cmd = ['convert',old_filepath,'-resize',`width`+'x'+`height`,'-rotate',angle,'-quality','95', new_filename]
			return_code = subprocess.call(cmd)
			self.ui.AppendToLog('')
			self.ui.AppendToLog('Original:\n'+f)
			self.ui.AppendToLog('Resized copy:\n'+new_filename)
			if (return_code==0):
				self.ui.AppendToLog('OK')
			else:
				self.ui.AppendToLog('FAIL')

