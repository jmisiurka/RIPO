from ultralytics import YOLO

model = YOLO("./railing.pt")

result = model.track(source='../videos/video1.mp4', show=True)