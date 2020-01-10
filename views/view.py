from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import logging

from views.view_ui import Ui_MainWindow


class View(QMainWindow):
    def __init__(self, model, controller):
        super().__init__()
        self.logger = logging.getLogger(__name__)
        self._model = model
        self.controller = controller

        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)


        self.connect_slots()

    def connect_slots(self):
        self._ui.actionClose.triggered.connect(self.controller.close)

