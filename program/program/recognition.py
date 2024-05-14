from ultralytics import YOLO

model = YOLO("runs/detect/cars/weights/best.pt")

result = model.track(source='../videos/video1.mp4', show=True)