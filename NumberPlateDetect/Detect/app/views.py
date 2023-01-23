import cv2
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import numpy as np



@require_http_methods(["GET","POST"])
@csrf_exempt
def detect_numberplate(request):
    print("Inside the numberplate detection method")
    try:
        print("Inside the numberplate detection method")
        # Load the cascade
        plate_cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
        
        # To capture video from webcam. 
        cap = cv2.VideoCapture(0)
        # To use a video file as input 
        # cap = cv2.VideoCapture('filename.mp4')
        print("Video is about to start")
        while True:
            # Read the frame
            _, img = cap.read()
        
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
            # Detect the faces
            nplate= plate_cascade.detectMultiScale(gray, 1.1, 4)
        
            for (x, y, w, h) in nplate:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
        
            cv2.imshow("plate",img)
            k = cv2.waitKey(30) & 0xff
            if k==27:
                break
            

        # Release the VideoCapture object
        cap.release()
        
    except:
        print("Error occured")
    return render(request, 'platedetection.html')    
        
        