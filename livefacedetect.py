import cv2

cap = cv2.VideoCapture(0)
findFace = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
		ret, photo = cap.read()
		face_coord = findFace.detectMultiScale(photo)
		
		if face_coord is ():
			pass
		else:
			x = face_coord[0][0]
			y = face_coord[0][1]
			w = face_coord[0][2]
			h = face_coord[0][0]
			rectPhoto = cv2.rectangle(photo, (x,y), (x+w, y+h), (0,255,0), 5)	
			cv2.imshow('Live Video', photo)
			if cv2.waitKey(1) == 13:
				break
	
cv2.destroyAllWindows()
cap.release()
