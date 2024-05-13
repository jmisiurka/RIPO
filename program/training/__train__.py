from ultralytics import YOLO

def train():
    model = YOLO('yolov8n.pt')
    model.train(data="training/tree/data.yaml", epochs=5, name="tree")

train()