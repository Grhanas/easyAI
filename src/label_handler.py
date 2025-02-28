class LabelHandler:
    def __init__(self, selected_modal=None, selected_video_label=None):
        """
        QLabel'ları yöneten sınıf. Model ve video seçimlerini günceller.
        """
        self.selected_modal = selected_modal
        self.selected_video_label = selected_video_label

    def update_model_label(self, model_path):
        """
        Model seçildiğinde QLabel'e modelin adını yazdırır.
        """
        if self.selected_modal:  # QLabel atanmış mı kontrol et
            model_name = model_path.split("/")[-1].replace(".pt", "")  # Dosya adını al, uzantıyı kaldır
            self.selected_modal.setText(model_name)  # QLabel'e yazdır

    def update_video_label(self, video_path):
        """
        Video seçildiğinde QLabel'e video adını yazdırır.
        """
        if self.selected_video_label:  # QLabel atanmış mı kontrol et
            video_name = video_path.split("/")[-1]  # Sadece dosya adını al
            self.selected_video_label.setText(video_name)  # QLabel'e yazdır
