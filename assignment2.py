import pyautogui
import platform
import time


class WeChat:

    def check_system(self):
        return platform.platform()

    def is_login(self):
        login = pyautogui.locateOnScreen('qiehuan.png')
        if not login:
            return
        goto_login = pyautogui.center(login)
        pyautogui.moveTo(goto_login, duration=1)
        pyautogui.click()
        return True

    def search(self):
        sear = pyautogui.locateOnScreen('wx_search.png')
        if not sear:
            return
        goto_login = pyautogui.center(sear)
        pyautogui.moveTo(goto_login, duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.typewrite('wula')
        pyautogui.hotkey('enter')
        time.sleep(1)
        pyautogui.hotkey('enter')
        # pyautogui.typewrite('乌拉')
        return True

    def send_message(self):
        pyautogui.typewrite('hello')
        time.sleep(1)
        pyautogui.hotkey('enter')
        time.sleep(1)
        pyautogui.hotkey('enter')


    def wait_login(self):
        login = pyautogui.locateOnScreen('jiaoyan.png')
        if not login:
            return
        goto_login = pyautogui.center(login)
        pyautogui.moveTo(goto_login, duration=1)
        return True

    def run(self):
        if 'Windows' in self.check_system():
            pyautogui.hotkey('win', 'd')
            wx = pyautogui.locateOnScreen('window_wx.png')
            if not wx:
                return
            print(wx)
            goto_wx = pyautogui.center(wx)
            print(goto_wx)
            pyautogui.moveTo(goto_wx, duration=1)
            pyautogui.doubleClick()
        else:
            # pyautogui.hotkey('win', 'd')
            wx = pyautogui.locateOnScreen('mac_wx.png')
            print(wx)
            goto_wx = pyautogui.center(wx)
            if not goto_wx:
                return
            print(goto_wx)
            pyautogui.moveTo(goto_wx, duration=1)
            pyautogui.click()
        time.sleep(10)
        if self.is_login():
            time.sleep(3)
            while True:
                if not self.wait_login():
                    break
                time.sleep(3)
            # pyautogui.hotkey('Alt', 'Tab')
        time.sleep(2)
        if self.search():
            self.send_message()




if __name__ == '__main__':
    WeChat().run()