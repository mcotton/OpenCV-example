import cv2
import os
import glob

def detect(path):
    img = cv2.imread(path)
    cascade = cv2.CascadeClassifier("../haarcascade_frontalface_alt.xml")
    rects = cascade.detectMultiScale(img, 1.2, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))

    if len(rects) == 0:
        return [], img
    rects[:, 2:] += rects[:, :2]
    return rects, img

def box(rects, img, output):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)
    cv2.imwrite(output, img);

os.chdir('src')

for preview in glob.glob('*.jpeg'):
    rects, img = detect(preview)
    box(rects, img, "../done/" + preview)
