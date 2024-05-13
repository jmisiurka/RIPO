from ultralytics import YOLO

model = YOLO("runs/detect/tree5/weights/best.pt")

result = model.track(source='../videos/video1.mp4', show=True)