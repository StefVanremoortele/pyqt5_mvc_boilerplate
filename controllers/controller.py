from PyQt5.QtCore import *

from threading import Lock
import logging
import yaml
import datetime
import time
import re


class Controller(QObject):
    def __init__(self, model):
        super().__init__()
        self.logger = logging.getLogger(__name__)
        self._model = model


    def reset(self):
        """
        Handles application reset logic
        """
        pass

        
    @staticmethod
    def close():
        quit()
