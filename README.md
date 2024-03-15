# KECILIN_AI_Developer_ComputerVision_Test_Case--HANIF_ADAM
 
This Repository created for answer of KECILIN_AI_Developer_ComputerVision_Test_Case
The [Detection Result](https://drive.google.com/drive/folders/1gKJ2X2w0a9zLqJVwNxasE26d9DHz9sik?usp=sharing)

Guide for using this repo write down below :

### Clone this repository

### Make sure Ultralytics was installed
```
pip install ultralytics
```
---
---

## 1. Answer Create an inference solution using YOLOv8 for truck detection
1. Open Terminal inside repo
2. Type
```
python yolo.py
```
3. Menu Appear, then choose the menu (input number 1 for inference Truck)
4. Then Choose Footage (can use the Video or Image for inference)
5. Inference appear and show that script can inference the truck and ambulance, depend on footage chosen
>[!important]
>The inference show that model and script can inference the truck and ambulance
6. Wait until inference finish or can terminate by using
```
ctrl+c
```

## 2. Answer Modify to detect an ambulance instead of a truck
1. Open Terminal inside repo
2. Type
```
python yolo.py
```
3. Menu Appear, then choose the menu (input number 2 for inference Ambulance)
4. Then Choose Footage (can use the Video or Image for inference)
5. Inference appear and show that script can inference the truck and ambulance, depend on footage chosen but only detect the ambulance only
>[!important]
>The inference show that model and script can inference the truck and ambulance but only the ambulance
6. Wait until inference finish or can terminate by using
```
ctrl+c
```
