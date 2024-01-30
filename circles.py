import cv2
import numpy as np


def detect_circles(image_path, min_radius=10, max_radius=50):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detect circles with ``HoughCircles``
    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=10,
        param1=50,
        param2=9,
        minRadius=min_radius,
        maxRadius=max_radius,
    )

    if circles is not None:
        # convert coords to integers
        circles = np.uint16(np.around(circles))

        count = 0
        coords = []
        for i in circles[0, :]:
            cv2.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 2)
            cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
            coords.append({"x": i[0], "y": i[1]})
            count += 1
        print(coords)
    else:
        print("No circles detected")
