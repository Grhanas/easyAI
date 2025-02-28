from ultralytics import YOLO
import cv2

class YOLOProcessor:
    """
    Exp: Just processes coming frames
    with YOLO then put labels on frame
    and returns them.

    Inputs: Frames.
    
    Returns: Processed frames.
    """
    def __init__(self):
        self.model = None
        
    def load_model(self, model_path):
        try:
            self.model = YOLO(model_path)
            print('Model loaded')
        except Exception as e:
            print('Error in YOLOProcessor load_model:', e)
    
    def process_frame(self, frame):
        try:
            if self.model is None:
                return frame
            
            results = self.model(frame)
            for result in results:
                for box in result.boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    conf = box.conf[0]
                    cls = int(box.cls[0])

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
                    label = f"{self.model.names[cls]} {conf:.2f}"
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

            return frame
        except Exception as e:
            print('Error in YOLOProcessor process_frame:', e)