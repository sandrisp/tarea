#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore

class Tarea(QtGui.QMainWindow):
	"""docstring for Tarea"""
	def __init__(self):
		super(Tarea, self).__init__()
		self.hw_lbl  = QtGui.QLabel("Hola mundo", self)

		self.menubar = self.menuBar()
		self.menu_tarea = self.menubar.addMenu("&Tarea")
		self.action_Kurt_Poehler = QtGui.QAction("&Kurt Poehler", self)
		self.action_Kurt_Poehler.triggered.connect(self.menu_event)#, "Kurt Poehler")
		self.menu_tarea.addAction(self.action_Kurt_Poehler)

		self.show()

	def menu_event(self):
		trigger = "Kurt Poehler"
		msg = QtGui.QMessageBox.information(
						self,
						"Info",
						u"%s" % trigger,
						QtGui.QMessageBox.Ok
						)

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	main = Tarea()
	sys.exit(app.exec_())