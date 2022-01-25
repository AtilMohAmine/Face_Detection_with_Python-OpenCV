import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

frame = cv2.imread('img.jpg')
	
gray_scaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
face_coordinates = trained_face_data.detectMultiScale(gray_scaled_img, scaleFactor=1.2,minNeighbors=5,minSize=(20,20))
	
for(x, y, w, h) in face_coordinates:
	cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 10)
		
output = cv2.resize(frame, (960, 540))
cv2.imshow('Face detector', output)
cv2.waitKey()
