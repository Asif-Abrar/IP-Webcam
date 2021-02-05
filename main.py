import cv2

cam = cv2.VideoCapture(0)
address = "https://192.168.0.101:8080/video"
cam.open(address)

while cam.isOpened():
    ret, frame = cam.read()
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('IP Webcam', frame)

cam.release()
cv2.destroyAllWindows()
