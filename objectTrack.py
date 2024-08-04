import cv2, imutils

#initialise tracker
tracker = cv2.TrackerCSRT_create()
# Set it to True for webcam, False for video
camera=False 

# Open video capture from webcam or from video file
if camera: 
	video  = cv2.VideoCapture(0)
else:
	video = cv2.VideoCapture('sample.mp4')
_,frame = video.read()
frame = imutils.resize(frame,width=720)
BB = cv2.selectROI(frame,False)
tracker.init(frame, BB)

#loop over frames in the video 
while True:
	# Read frame from the video 
	_,frame = video.read()
	# Resize frame for processing
	frame = imutils.resize(frame,width=720)
	# Update tracker
	track_success,BB = tracker.update(frame)
	# Draw rectangle around object being tracked
	if track_success:
		top_left = (int(BB[0]),int(BB[1]))
		bottom_right = (int(BB[0]+BB[2]), int(BB[1]+BB[3]))
		cv2.rectangle(frame,top_left,bottom_right,(0,255,0),5)
	# Display output frame
	cv2.imshow('Output',frame)
	# Press 'q' to close
	key  =  cv2.waitKey(1) & 0xff
	if key == ord('q'):
		break
video.release()
cv2.destroyAllWindows()