from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  QApplication
from PyQt5.QtGui import QPalette, QColor

import sys
import os
import logging
import logging.config
import yaml

from controllers.controller import Controller
from models.model import Model
from views.view import View

def setup_logging(
    default_path='resources/logger_config.yaml',
    default_level=logging.DEBUG,
    env_key='LOG_CFG'
):
    """
    Setup logging configuration
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


class App(QApplication):
    """
    The application
    """
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()
        self.controller = Controller(self.model)
        self.view = View(self.model, self.controller)

        self.view.show()
        # self.view.showFullScreen()
        self.view.setWindowTitle("App")


def setTheme(app):
    """
    Setup app theme
    """
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.setStyle('Fusion')
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(15,15,15))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)

    palette.setColor(QPalette.Highlight, QColor(255, 202, 5).lighter())
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)


if __name__ == '__main__':
    setup_logging()
    logger = logging.getLogger(__name__)
    app = App(sys.argv)
    setTheme(app)
    sys.exit(app.exec_())
