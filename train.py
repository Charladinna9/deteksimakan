from ultralytics import YOLO

# Load model YOLO11n
model = YOLO("yolo11n.pt")

results = model.train(
    data="dataset/data.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    patience=100,
    project="runs/detect",
    name="train_29class",
    pretrained=True,
    device="cpu"
)