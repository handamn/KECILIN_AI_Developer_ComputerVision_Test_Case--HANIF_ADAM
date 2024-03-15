import cv2
from ultralytics import YOLO

def video_detection(yolo_model, video_path, label):
    video_capture = cv2.VideoCapture(video_path)

    while video_capture.isOpened():
        success, frame = video_capture.read()

        if success:
            detection_results = yolo_model(frame, classes = label)
            annotated_frame = detection_results[0].plot()
            cv2.imshow("Truck Ambulance YOLOv8", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break

    video_capture.release()
    cv2.destroyAllWindows()

def image_detection(yolo_model, image_path, label):
    detection_results = yolo_model(image_path, classes = label)
    annotated_frame = detection_results[0].plot()
    cv2.imshow("Truck Ambulance YOLOv8", annotated_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    detection_results.save(filename ="1")


if __name__ == "__main__":
    yolo_model = YOLO('.\\best.pt')

    print(" ")
    print("========================================================")
    print("========================================================")
    print("KECILIN - AI Developer (Computer Vision) Test Case")
    print("by Hanif Adam")
    print("Menu :")
    print("1. Inference Truck")
    print("2. Inference only Ambulance")
    print(" ")
    question = input("Choose The Question (only input the number) : ")
    print(" ")

    if int(question) == 1:
        print("========================================================")
        print("Choose Footage : ")
        print("1. Truck Video")
        print("2. Ambulance Video")
        print("3. Truck Image")
        print("4. Ambulance Image")
        print(" ")
        footage = input("Choose The Footage (only input the number) : ")
        print("========================================================")
        print("========================================================")
        print(" ")

        if int(footage) == 1:
            video_path = ".\\stock_footage\\Truck.mp4"
            video_detection(yolo_model, video_path, None)
        
        elif int(footage) == 2:
            video_path = ".\\stock_footage\\Ambulance.mp4"
            video_detection(yolo_model, video_path, None)
        
        elif int(footage) == 3:
            image_source = ".\\stock_footage\\Truck2.jpg"
            image_detection(yolo_model, image_source, None)
        
        else :
            image_source = ".\\stock_footage\\Ambulance2.jpg"
            image_detection(yolo_model, image_source, None)

    else :
        print("Choose Footage : ")
        print("1. Truck")
        print("2. Ambulance")
        print("3. Truck Image")
        print("4. Ambulance Image")
        print(" ")
        footage = input("Choose The Footage (only input the number) : ")
        print(" ")

        if int(footage) == 1:
            video_path = ".\\stock_footage\\Truck2.jpg"
            video_detection(yolo_model, video_path, 0)
        
        elif int(footage) == 2:
            video_path = ".\\stock_footage\\Ambulance.mp4"
            video_detection(yolo_model, video_path, 0)
        
        elif int(footage) == 3:
            image_source = ".\\stock_footage\\Truck2.jpg"
            image_detection(yolo_model, image_source, 0)
        
        else :
            image_source = ".\\stock_footage\\Ambulance2.jpg"
            image_detection(yolo_model, image_source, 0)
