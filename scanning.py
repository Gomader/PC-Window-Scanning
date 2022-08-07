from win32gui import IsWindow, IsWindowEnabled, IsWindowVisible, GetWindowText, EnumWindows, FindWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImage
from sys import argv
from cv2 import cvtColor, COLOR_BGR2GRAY, imshow, waitKey, imread
from numpy import frombuffer, uint8
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
    
    

if __name__ == '__main__':
    getScreenShot()