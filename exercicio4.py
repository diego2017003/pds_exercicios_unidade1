# import the opencv library
from operator import index
from turtle import width
import matplotlib.pyplot as plt
import cv2
import numpy as np

bins = 32
lw = 3
alpha = 0.5
vid = cv2.VideoCapture(0)
fig, ax = plt.subplots(3, 1, figsize=(4, 5))
ax1, ax2, ax3 = ax
# ax.set_title("Histogram (RGB)")
(lineR,) = ax1.plot(
    np.arange(bins),
    np.zeros((bins,)),
    c="r",
    lw=lw,
    alpha=alpha,
)
(lineG,) = ax2.plot(
    np.arange(bins),
    np.zeros((bins,)),
    c="g",
    lw=lw,
    alpha=alpha,
)
(lineB,) = ax3.plot(
    np.arange(bins),
    np.zeros((bins,)),
    c="b",
    lw=lw,
    alpha=alpha,
)

ax1.set_xlim(0, bins - 1)
ax2.set_xlim(0, bins - 1)
ax3.set_xlim(0, bins - 1)
ax1.set_ylim(0, 1)
ax2.set_ylim(0, 1)
ax3.set_ylim(0, 1)
plt.ion()
plt.show()

while True:

    ret, frame = vid.read()

    numPixels = np.prod(frame.shape[:2])
    (b, g, r) = cv2.split(frame)
    r = cv2.equalizeHist(r)
    g = cv2.equalizeHist(g)
    b = cv2.equalizeHist(b)

    histogramR = cv2.calcHist([r], [0], None, [bins], [0, 256]) / numPixels
    histogramG = cv2.calcHist([g], [0], None, [bins], [0, 256]) / numPixels
    histogramB = cv2.calcHist([b], [0], None, [bins], [0, 256]) / numPixels
    lineR.set_ydata(histogramR)
    lineG.set_ydata(histogramG)
    lineB.set_ydata(histogramB)

    fig.canvas.draw()
    fig.canvas.flush_events()
    bgr = cv2.merge([b, g, r])
    cv2.imshow("equalized", bgr)
    cv2.imshow("real", frame)

    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

vid.release()

cv2.destroyAllWindows()
