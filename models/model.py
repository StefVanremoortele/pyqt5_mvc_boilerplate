from PyQt5.QtCore import QObject, pyqtSignal


class Model(QObject):
    barcode_old_changed = pyqtSignal()
    barcode_new_changed = pyqtSignal()

    @property
    def barcode_old(self):
        return self._barcode_old

    @barcode_old.setter
    def barcode_old(self, value):
        self._barcode_old = value

    @property
    def barcode_new(self):
        return self._barcode_new

    @barcode_new.setter
    def barcode_new(self, value):
        self._barcode_new = value

    @property
    def version(self):
        return self._version

    def __init__(self):
        super().__init__()

        self._version = '0.0.1'
        self._barcode_old = ''
        self._barcode_new = ''

        
        