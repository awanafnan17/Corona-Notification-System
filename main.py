from plyer import notification
import requests
from bs4 import BeautifulSoup


def notifyMe(title, message):
    # Function to send notifications
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\Afnan Awan\\Desktop\\Corona Notification System\\icon.ico",
        timeout = 10
    )
    
def getData(url):
    r = requests.get(url)
    return r.text

if __name__=="__main__":
    # notifyMe("Afnan", "Let's eat Mighty Zinger")
    myData = getData('https://www.worldometers.info/coronavirus/')
    myDataStr = ""

    soup = BeautifulSoup(myData, 'html.parser')

    for tr in soup.find_all('tbody')[1].find_all('tr'):
        myDataStr += tr.getText()
    
    itemList = myDataStr.split("\n\n")
    
    for item in itemList:
        print(item)