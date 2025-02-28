import sys
from PySide6.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow
from video_player import VideoPlayer
from yolo_processor import YOLOProcessor
from button_handler import ButtonHandler
from label_handler import LabelHandler

class easyai_app(QMainWindow, Ui_MainWindow):
    """
    Exp: Organizer class, all process that user want
    to do are splitted different class and this class
    manage all processes.

    Inputs: MainWindow(coming from qt designer)

    Returns:    
    """
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.playback_speed = 300
        self.ui.spin_box.setValue(300)

        self.yolo_processor = YOLOProcessor()

        self.ui.spin_box.valueChanged.connect(self.update_spin_box_value)
        self.video_player = VideoPlayer(self.ui.video_play_area, self.yolo_processor, self.playback_speed)

        self.label_handler = LabelHandler(self.ui.selected_modal, self.ui.selected_video)

        self.button_handler = ButtonHandler(self.video_player, self.yolo_processor, self.label_handler)

        self.ui.modal_selection_button.clicked.connect(self.button_handler.model_selection)
        self.ui.select_video_button.clicked.connect(self.button_handler.video_selection)
        self.ui.use_default_model_button.clicked.connect(self.button_handler.use_default_model)
        self.ui.use_default_video_button.clicked.connect(self.button_handler.use_default_video)

    def update_spin_box_value(self, value):
        self.playback_speed = value
        self.video_player.set_playback_speed(value)
        print(self.playback_speed)
