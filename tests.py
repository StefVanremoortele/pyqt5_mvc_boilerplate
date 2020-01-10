from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

import sys
import unittest
import datetime
from unittest import mock

from controllers.controller import Controller
from models.model import Model
from views.view import View

app = QApplication(sys.argv)

class AppTest(unittest.TestCase):
    '''Test the margarita mixer GUI'''

    def setUp(self):
        '''Create the model, controller & GUI'''
        self.current_version = '4.4.1'
        self.model = Model()
        self.controller = Controller(self.model)
        self.controller.scanner_thread.close() # getting PermissionError when left open while testing - Mock it instead
        self.view = View(self.model, self.controller)
    def test_version(self):
        self.assertEqual(self.controller._model.version, self.current_version, 'Version should be changed for each update')

    

if __name__ == "__main__":
    unittest.main()
