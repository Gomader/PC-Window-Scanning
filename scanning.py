from win32gui import IsWindow, IsWindowEnabled, IsWindowVisible, GetWindowText, EnumWindows, FindWindow
from PyQt5.QtWidgets import QApplication
from sys import argv
from cv2 import cvtColor, COLOR_BGR2GRAY, matchTemplate, TM_CCOEFF_NORMED
from numpy import where
from qimage2ndarray import rgb_view


'''
    Get all windows' name
    return->dict {hwnd:title}
'''
def getWindowsName():

    class Hwnd():
        def get_hwnd_dic(self, hwnd, hwnd_title):
            if (IsWindow(hwnd)
                    and IsWindowEnabled(hwnd)
                    and IsWindowVisible(hwnd)
                    and GetWindowText(hwnd)):
                hwnd_title[f"{hwnd}"] = GetWindowText(hwnd)

        def get_hwnd(self):
            '''
            :return: {hwnd:title}
            '''
            hwnd_title = {}
            EnumWindows(self.get_hwnd_dic, hwnd_title)
            return hwnd_title

    return Hwnd().get_hwnd()



'''
    Get screen shot
    return Gray scale (ndarray)
'''
def getScreenShot(windowname):

    handle = FindWindow(None,windowname)
    app = QApplication(argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(handle).toImage()

    img = rgb_view(img)

    img_gray = cvtColor(img, COLOR_BGR2GRAY)

    return img_gray
    
    
'''
    Image matching function
    return a center point position (x,y)
'''
def imageMatching(source, icon):
    h, w = icon.shape[:2]
    res = matchTemplate(source, icon, TM_CCOEFF_NORMED)
    loc = where(res >= 0.6)
    for pt in zip(*loc[::-1]):
        center = (pt[0] + int(w/2), pt[1] + int(h/2))
        return center
        