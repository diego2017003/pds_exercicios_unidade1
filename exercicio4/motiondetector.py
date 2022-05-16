import matplotlib.pyplot as plt
import cv2
import numpy as np


vid = cv2.VideoCapture(0)
bins = 32
ret, frame = vid.read()

numPixels = np.prod(frame.shape[:2])
(b, g, r) = cv2.split(frame)

histogramR = cv2.calcHist([r], [0], None, [bins], [0, 256])
histogramG = cv2.calcHist([r], [0], None, [bins], [0, 256])
histogramB = cv2.calcHist([r], [0], None, [bins], [0, 256])
while True:

    ret, frame = vid.read()

    numPixels = np.prod(frame.shape[:2])
    (b, g, r) = cv2.split(frame)

    old_red = histogramR
    old_green = histogramG
    old_blue = histogramB

    histogramR = cv2.calcHist([r], [0], None, [bins], [0, 256]) / numPixels
    histogramG = cv2.calcHist([g], [0], None, [bins], [0, 256]) / numPixels
    histogramB = cv2.calcHist([b], [0], None, [bins], [0, 256]) / numPixels

    bgr = cv2.merge([b, g, r])
    cv2.imshow("real", frame)
    dr = abs(histogramR - old_red)
    dg = abs(histogramG - old_green)
    db = abs(histogramB - old_blue)
    dif = sum([sum(dr), sum(dg), sum(dg)]) / 3

    if dif > 0.02:
        print("Danger Danger", dif)
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

vid.release()

cv2.destroyAllWindows()
