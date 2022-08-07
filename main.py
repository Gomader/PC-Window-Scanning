import scanning
from cv2 import imread
from cv2 import circle, imshow, waitKey

if __name__ == '__main__':
    source = scanning.getScreenShot()
    icon = imread("./testForScanning/12.png", 0)
    center = scanning.imageMatching(source, icon)
    img = circle(source, center, 5, (0,0,255), 1)
    imshow('res', img)
    waitKey(0)