# button_handler.py
from PySide6.QtCore import QThread
from PySide6.QtWidgets import QFileDialog
import os
import sys

if getattr(sys, 'frozen', False):
    # PyInstaller ile oluşturulmuş .exe
    base_path = sys._MEIPASS
else:
    # Normal .py dosyası
    base_path = os.getcwd()

default_video_path = os.path.join(base_path, 'car.mp4')
default_model_path = os.path.join(base_path, 'yolo11s.pt')

class ButtonHandler:
    """
    Exp: Handles all buttons and their actions.

    Inputs: Coming from user interface(video path and model path).
    
    Returns: Processed frames (video)
    """
    def __init__(self, video_player, yolo_processor, label_handler):
        try:
            self.video_player = video_player
            self.yolo_processor = yolo_processor
            self.label_handler = label_handler
            self.default_video_path = default_video_path
            self.default_model_path = default_model_path
            self.video_path = None
        except Exception as e:
            print('Error in button_handler init:',e)

    def model_selection(self):
        """
        Exp: User choose model from UI and takes the model.
        Inputs: self and yolo model coming from user selection.
        Returns: Nothing
        """
        try:
            self.video_player.stop_video()
            options = "YOLO Model Files (*.pt);;All Files (*)"
            model_path, _ = QFileDialog.getOpenFileName(None, "Select Model", "", options)
            if model_path:
                self.yolo_processor.load_model(model_path)
                self.label_handler.update_model_label(model_path)
                self.video_player.load_video(self.video_path)
                self.label_handler.update_video_label(self.video_path)
            # If user do not choice any file and click cancel
            else:
                self.video_player.load_video(self.video_path)
                self.label_handler.update_video_label(self.video_path)

        except Exception as e:
            print('Error in button_handler model_selection:', e)

    def video_selection(self):
        """
        Exp: User choose video from UI and takes the model.
        Inputs: self and video coming from user selection.
        Returns: Nothing
        """
        try:
            self.video_player.stop_video()
            options = "Video Files (*.mp4 *.avi *.mov *.mkv);;All Files (*)"
            video_path, _ = QFileDialog.getOpenFileName(None, "Select Video", "", options)
            if video_path:
                self.video_path = video_path
                self.video_player.load_video(self.video_path)
                self.label_handler.update_video_label(self.video_path)
                
            # If user do not choice any file and click cancel
            else:
                self.video_player.load_video(self.video_path)
                self.label_handler.update_video_label(self.video_path)
        except Exception as e:
            print('Error in button_handler video_selection:', e)

    def use_default_model(self):
        """
        Exp: If user clicks use default model this method
        works and load default yolov5s.pt model
        Inputs: self.
        Returns: Nothing
        """
        try:
            self.video_player.stop_video()
            model_path = self.default_model_path
            self.yolo_processor.load_model(model_path)
            self.label_handler.update_model_label(model_path)
            self.video_player.load_video(self.video_path)
            self.video_player.update_frame()
        except Exception as e:
            print('Error in button_handler use_default_model:', e)


    def use_default_video(self):
        """
        Exp: If user clicks use default video this method
        works and load default video
        Inputs: self.
        Returns: Nothing
        """
        try:
            self.video_player.stop_video()
            self.video_path = self.default_video_path
            self.video_player.load_video(self.video_path)
            self.label_handler.update_video_label(self.video_path)
        except Exception as e:
            print('Error in button_handler use_default_video:', e)

