import webbrowser # To launch default browser
import time # To create little delays between keys
import win32com.client # To establish shell

shell = win32com.client.Dispatch("WScript.Shell")
tweet = """Hello World @World #Coding #Python"""
webbrowser.open("https://twitter.com")
time.sleep(5)

# Start a new tweet
shell.SendKeys("n", 0)
time.sleep(1)

# Type the tweet
shell.SendKeys(tweet, 0)
time.sleep(1)

shell.SendKeys("^{ENTER}", 0)
time.sleep(1)
