from ultralytics import YOLO
import cv2

# Load model once
model = YOLO("yolov8n.pt")


def detect_objects(frame):

    results = model(frame, verbose=False)

    objects = []

    for result in results:

        for box in result.boxes:

            cls = int(box.cls[0])

            name = model.names[cls]

            if name not in objects:
                objects.append(name)

    return objects