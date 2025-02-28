# Import necessary libraries
import cv2
from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel

class VideoPlayer:
    def __init__(self, label, yolo_processor, playback_speed):
        """
        Exp: Video player class. PySide6 print frames 
        to QLabel coming from YOLO.

        Inputs: Related UI labels and yolo processor class

        Returns: Processed frames
        """
        try:
            self.label = label  # QLabel objesi
            self.yolo_processor = yolo_processor  # YOLO modelini işleyen sınıf
            self.cap = None  # VideoCapture objesi
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_frame)  # Zamanlayıcıya güncelleme fonksiyonunu bağla
            self.playback_speed = playback_speed
        except Exception as e:
            print('Error in VideoPlayer init:', e)
    
    def set_playback_speed(self, speed):
        try:
            self.playback_speed = speed
            self.timer.stop()  # Mevcut zamanlayıcıyı durdur
            self.timer.start(self.playback_speed)  # Yeni hızda zamanlayıcıyı başlat
        except Exception as e:
            print('Error in VideoPlayer set_playback_speed:', e)

    def load_video(self, video_path):
        """
        Exp: Upload new video file and starts processes.
        Input: Video path
        Returns: ????
        """
        try:
            if self.cap:
                self.cap.release()  # Eğer önceki video açıksa kapat

            self.cap = cv2.VideoCapture(video_path)
            if not self.cap.isOpened():
                print(f"❌ Video yüklenemedi: {video_path}")
                return
            
            self.timer.start(self.playback_speed)
            print(f"✅ Video uploaded: {video_path}")
        except Exception as e:
            print('Error in VideoPlayer load_video:', e)

    def update_frame(self):
        """
        Exp: Process frames with yolo then print it
        to UI label
        Inputs: self
        Returns: processed frame
        """

        try:
            if self.cap and self.cap.isOpened():
                ret, frame = self.cap.read()
                if ret:
                    frame = self.yolo_processor.process_frame(frame)  # YOLO çerçeveyi işlesin
                    # Eğer çerçeve BGR ise RGB'ye çevir
                    if frame.shape[2] == 3:
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    

                    # QLabel boyutunu alın
                    label_width = self.label.width()
                    label_height = self.label.height()

                    # Çerçeveyi QLabel'e uygun şekilde yeniden boyutlandırın
                    frame = cv2.resize(frame, (label_width, label_height))
                    height, width, _ = frame.shape
                    

                    # PySide6 için QImage oluştur
                    q_img = QImage(frame.data, width, height, frame.strides[0], QImage.Format.Format_RGB888)

                    if q_img.isNull():
                        print("❌ QImage failed!")
                        return

                    # QLabel'a QPixmap ekleme işlemi PySide6 için düzeltildi
                    pixmap = QPixmap.fromImage(q_img)

                    if pixmap.isNull():
                        print("❌ QPixmap failed!")
                        return

                    self.label.clear()  # Önceki içeriği temizle
                    self.label.setPixmap(pixmap)  # Yeni çerçeveyi QLabel'e bas

                else:
                    print("⚠️ Video finihed or error occurs")
                    self.cap.release()
                    self.timer.stop()
        except Exception as e:
            print('Error in VideoPlayer update_frame:', e)

    def stop_video(self):
        """
        Exp: Stop video and release the source
        Inputs: self
        Returns: Nothing
        """
        try:
            if self.cap:
                self.cap.release()
                self.cap = None
            self.timer.stop()
            self.label.clear()
            print("🛑 Video stopped.")
        except Exception as e:
            print('Error in VideoPlayer stop_video:', e)

    def is_playing(self):
        """
        Exp: Video play check (is video playing ?)
        Inputs: self
        Returns: True or False
        """
        return self.cap is not None and self.cap.isOpened()
