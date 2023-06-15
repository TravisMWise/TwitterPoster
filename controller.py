import webbrowser # To launch default browser
import time # To create little delays between keys
import win32com.client # To establish shell

class Controller:
    def __init__(self, link="https://twitter.com") -> None:
        webbrowser.open(link)
        self.shell = win32com.client.Dispatch("WScript.Shell")
        time.sleep(5)
    def sendTweet(self, text="test"):
        self.shell.SendKeys("n", 0)
        time.sleep(1)
        self.shell.SendKeys(text, 0)
        time.sleep(1)
        self.shell.SendKeys("^{ENTER}", 0)
        time.sleep(1)