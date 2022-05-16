import matplotlib.pyplot as plt
import cv2
import numpy as np

##Em desenvolvimento
vid = cv2.VideoCapture(0)
media = np.array(
    [[0.1111, 0.1111, 0.1111], [0.1111, 0.1111, 0.1111], [0.1111, 0.1111, 0.1111]]
)
gauss = np.array(
    [[0.0625, 0.125, 0.0625], [0.125, 0.25, 0.125], [0.0625, 0.125, 0.0625]]
)
horizontal = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
vertical = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
diagonal = np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]])
laplacian = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
boost = np.array([[0, -1, 0], [-1, 5.2, -1], [0, -1, 0]])
absolut = True
kernel = media
while True:

    ret, frame = vid.read()
    dst = cv2.filter2D(frame, -1, kernel)
    cv2.imshow("real", frame)
    cv2.imshow("transformado", dst)
    key = cv2.waitKey(10)
    if key == 27:
        break
    elif cv2.waitKey(1) & 0xFF == ord("a"):
        absolut = not absolut
        break
    elif cv2.waitKey(1) & 0xFF == ord("m"):
        kernel = media
        print(kernel)
        break
    elif cv2.waitKey(1) & 0xFF == ord("g"):
        kernel = gauss
        print(kernel)
        break
    elif cv2.waitKey(1) & 0xFF == ord("h"):
        kernel = horizontal
        print(kernel)
        break
    elif cv2.waitKey(1) & 0xFF == ord("v"):
        kernel = vertical
        print(kernel)
        break
    elif cv2.waitKey(1) & 0xFF == ord("l"):
        kernel = laplacian
        print(kernel)
        break
    # elif key == "b":
    ##    kernel = boost
    #   break
    else:
        break

vid.release()

cv2.destroyAllWindows()
