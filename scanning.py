import win32gui


class Hwnd():
    def get_hwnd_dic(self, hwnd, hwnd_title):
        if (win32gui.IsWindow(hwnd)
                and win32gui.IsWindowEnabled(hwnd)
                and win32gui.IsWindowVisible(hwnd)
                and win32gui.GetWindowText(hwnd)):
            hwnd_title[f"{hwnd}"] = win32gui.GetWindowText(hwnd)

    def get_hwnd(self):
        '''
        :return: {hwnd:title}
        '''
        hwnd_title = {}
        win32gui.EnumWindows(self.get_hwnd_dic, hwnd_title)
        return hwnd_title


hwnd = Hwnd()
print(hwnd.get_hwnd())