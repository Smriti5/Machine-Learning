#!/usr/bin/python3
import cv2
cap=cv2.VideoCapture(0)
while cap.isOpened() :
	status, frame=cap.read()
	cv2.imshow('live',frame)
	if cv2.waitKey(10) & 0xff == ord('q') :
		break

cv2.destroyAllWindows()
cap.release()
