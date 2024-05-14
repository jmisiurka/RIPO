from ultralytics import YOLO

def train():
    model = YOLO('yolov8n.pt')
    model.train(data="training/cars/data.yaml", name="cars")

train()