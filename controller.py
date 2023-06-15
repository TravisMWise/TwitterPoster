import webbrowser # To launch default browser
import time # To create little delays between keys
import win32com.client # To establish shell

class Controller:
    """Controller class for sending automatic tweets to twitter"""
    def __init__(self, link="https://twitter.com") -> None:
        """Initialize the program by opening the website sent in,
        if no website is sent then open twitter's homepage."""
        webbrowser.open(link) 
        self.shell = win32com.client.Dispatch("WScript.Shell")
        time.sleep(5)
    def sendTweet(self, text="test"):
        """Send a tweet with the text passed in, 
        if no text is passed send 'test'."""
        self.shell.SendKeys("n", 0)
        time.sleep(1)
        self.shell.SendKeys(text, 0)
        time.sleep(1)
        self.shell.SendKeys("^{ENTER}", 0)
        time.sleep(1)