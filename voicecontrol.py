import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import webbrowser as wb
import pyautogui as pg
import os
import pywhatkit as kit
import uuid
#import pyttsx3
import psutil
from random import randint
import keyboard
import time
import warnings
import smtplib
import random
import subprocess

mac = str(uuid.getnode())
print("Id:",mac)

#engine = pyttsx3.init()

a = {
  "type": "service_account",
  "project_id": "jarvisforwindows",
  "private_key_id": "6687f62ff6426abd234bce8f8b23e0d06dcc5eb8",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCIr6xJeqt2mQPH\nTlCkBOXoNNA24kKj2zaH70UQUp7DobBM86Vnwe/TCWKaV1VvHwB1xmoFHFY2gOxo\nCjGkDBcWIG2+K/EhWseqY/VOGxY7ICpirrLGnncwdEQ29mQReop/OgosFj0vuxRl\nJr9Ky29mJd5WE1PJZv6hqJJyQUh4V2py9An3juAuc9Kf8r+wzNbX0eP8Sge1yXhv\naQQTXdbWTUtOq8O0uHnrsVUdId94nEb8ATaqMMZCK3UJwWDTi/ilt4ORAhe2+Fbz\nfQeT5pe+rW62qnOtbad6AjIPzrA4Fnkw1pc+VvGPMdXBi+WzqQfI9LR+pD8ic0FW\noGzaCuoFAgMBAAECggEAPjyC/YgR53PfoRHbLPuf9V2Kytq2DibDyxxavYZpDNmj\nzT4JO9e1y8kTsQP//hNHIdlAr+gJp1KHkg3GMZRhtKz6WyNl7VKI5GAUM0apFi3c\nrsct1rsTuSfPYZlJ0h2ST0DNnepYXNHZhP8iDbvYktG+TUIKngM8AL6hQ83O4h/9\nBxwFAZ7HQxp2Sc3yTMFwLOJq22LwTPkt2T3bbYJaAQkDlUVRb7/FsvD9YRSdB25f\n2GIuuSAvJCo1RAJqynhHsR661ybz9yPpo6ODVCfg7yU9Av2JYhx8RFarkzfWgy0W\nWCXOLptdTVLACxYspiEZ9tOFSdN69b+LnKGPuqtpVwKBgQDAtxZzVPjQzAXAP6bJ\na+m8WWRzBVAeAoOE32gLbSqM8W74qy6SMoO/sNWHN6VYlOsDBkfZGZdOVcOZMTHF\nHTN5B6ZJffNL9vJ0RADSZX8IbDxe5xo33Wxr/IrRbJLdDliLCriekfBizMgnaZVt\n7i/aIGCptpjOE0VoffF+NwgjdwKBgQC1kmuYPhGKyhH9mH24DqCmzdRCAnPK17Ma\nVNmnDCVVusnftm+9ZXTFDOh9YwAw+r/Koluio83jRwJco8gfruPWGkc5GyUtZ0Zc\nyO3U9D7/ccDZULx1jUU0VASHEWalCcntgOKkD2Ag5m9zlnredXAv00e1wKW3+Iw7\n2sDvsKMlYwKBgGzxE0fvaRjfvQCI+wgycNeA0UAUaM4OLbsXcAHFnKBAe7MnUhRj\nagcbOBpQYrBIvvHeww7/YIFwCjq3jKMZdtecc2xoPvlaiIUhTDWkGsPwK9CaZD/g\ndEI3aWIqNnuweG1hiixZ48J2cU+WaFrUo0hztTE7f/Y+/qWrTLFE+tzRAoGAP4Rf\nGzzrSg/yRzJnGFIVpQRv8j+FXjoir11rXmKDVQAoype5cxngxWYElohhcsDlAu/U\n+oou5gjbLKkmwt6dWTKMI8/5K27rUF4BxPNEbnvOqLbzlnO699lEVDOkIqvP9cOW\nhSnTyO6Tom3LwbJ3cmOIvG4OCtNpyy51O+Qgzl0CgYEAlELfD3Yhi04A+rWsQ/xC\nbVtvSIRY6Mk7InFHKDKBzk2d8qswCHKfJszy1k9JK4jrohhyXxq3zAiOLbHadwQ2\nPAtYL4Pn4ARhmBSm4UOTtyx0q4wjJ/JASMopUVuOQnLbWveJ9bXCJb7dKrkeO24S\nDv8MuX8hNhRAyXT/+2ZrT7Y=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-l03aj@jarvisforwindows.iam.gserviceaccount.com",
  "client_id": "107855943164914987915",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-l03aj%40jarvisforwindows.iam.gserviceaccount.com"
}


cred = credentials.Certificate(a)

firebase_admin.initialize_app(cred, {
    "databaseURL": "https://jarvisforwindows-default-rtdb.firebaseio.com/"
})

ref = db.reference('/App/')

def sendOtp(email):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to the SMTP server
    server.login('systemcontrol910@gmail.com','mbqjhjyfgzizowaz')

    # Send the email
    otp = random.randint(1000,9999)
    msg = "Hello, Your otp is "+str(otp)
    server.sendmail('systemcontrol910@gmail.com', email, msg)

    # Disconnect from the SMTP server
    server.quit()
    return otp


def speak(text):
    pass

def setResponse(text):
    text = text.replace(" ", "_")
    ref.update({
        'resp': text
    })

def execute(cmd):
    if "type" in cmd:
        cmd = cmd.replace("type ", " ")   
        pg.typewrite(cmd)
    elif "open youtube" in cmd:
        wb.open("https://www.youtube.com/")
        setResponse("Done!")
    elif "refresh" in cmd:
        pg.hotkey("ctrl","r")
    elif "skip" in cmd:
        pg.click(x=124,y=984)
        time.sleep(0.5)
        pg.click(x=605,y=626)
        time.sleep(0.5)
        pg.click(x=1257,y=760)
    elif "open google" in cmd:
        wb.open("https://www.google.com/")
        setResponse("Done!")
    elif "open facebook" in cmd:
        wb.open("https://www.facebook.com/")
        setResponse("Done!")
    elif "open instagram" in cmd:
        wb.open("https://www.instagram.com/")
        setResponse("Done!")
    elif "open twitter" in cmd:
        wb.open("https://www.twitter.com/")
        setResponse("Done!")
    elif "open github" in cmd:
        wb.open("https://www.github.com/")
        setResponse("Done!")
    elif "open stackoverflow" in cmd:
        wb.open("https://www.stackoverflow.com/")
        setResponse("Done!")
    elif "open linkedin" in cmd:
        wb.open("https://www.linkedin.com/")
        setResponse("Done!")
    elif "open gmail" in cmd:
        wb.open("https://mail.google.com/")
        setResponse("Done!")
    elif "open gdrive" in cmd:
        wb.open("https://drive.google.com/")
        setResponse("Done!")
    elif "lock" in cmd:
        os.system("rundll32.exe user32.dll,LockWorkStation")
        setResponse("Done!")
    elif "open notepad" in cmd:
        subprocess.Popen(["notepad.exe"])
        setResponse("Done!")
    elif "open calculator" in cmd:
        os.system("calc")
        setResponse("Done!")
    elif "open paint" in cmd:
        os.system("mspaint")
        setResponse("Done!")
    elif "open word" in cmd:
        os.system("start winword")
        setResponse("Done!")
    elif "shutdown" in cmd:
        os.system("shutdown /s /t 1")
        setResponse("Done!")
    elif "restart" in cmd:
        os.system("shutdown /r /t 1")
        setResponse("Done!")
    elif "youtube" in cmd:
        cmd = cmd.replace("youtube ", "")
        kit.playonyt(cmd)
        setResponse("Done!")
    elif "sleep" in cmd:
        # python code to sleep the windows
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        setResponse("Done!")
    elif "battery level" in cmd:
        per = psutil.sensors_battery().percent
        resp = "Battery Level is " + str(per) + " percent"
        setResponse(resp)
        speak(resp)
    elif "take screenshot" in cmd:
        pg.screenshot("C:\\Users\\Ganesh\\OneDrive\\Pictures\\Screenshots\\"+str(randint(10000000, 99999999)) + ".png")
        setResponse("Done!")
    elif "mute" in cmd:
        pg.press("volumemute")
        setResponse("Done!")
    elif "increase volume" in cmd:
        pg.press("volumeup")
        setResponse("Done!")
    elif "decrease volume" in cmd:
        pg.press("volumedown")
        setResponse("Done!")
    elif "open code" in cmd:
        os.system("code")
        setResponse("Done!")
    elif "open command prompt" in cmd:
        os.system("cmd")
        setResponse("Done!")
    elif "search" in cmd:
        cmd = cmd.replace("search ", "")
        kit.search(cmd)
        setResponse("Done!")
    elif "close" in cmd:
        pg.hotkey("ctrl", "w")
        setResponse("Done!")
    elif "minimize" in cmd:
        pg.hotkey("win", "m")
        setResponse("Done!")
    elif "maximize" in cmd:
        pg.hotkey("win", "m")
        setResponse("Done!")
    elif "open file manager" in cmd or "open explorer" in cmd:
        pg.hotkey("win", "e")
        setResponse("Done!")
    elif "type my speech" in cmd:
        pg.hotkey("win", "h")
        setResponse("Done!")
    elif "select all" in cmd:
        pg.hotkey("ctrl", "a")
        setResponse("Done!")
    elif "copy" in cmd:
        pg.hotkey("ctrl", "c")
        setResponse("Done!")
    elif "paste" in cmd:
        pg.hotkey("ctrl", "v")
        setResponse("Done!")
    elif "cut" in cmd:
        pg.hotkey("ctrl", "x")
        setResponse("Done!")
    elif "undo" in cmd:
        pg.hotkey("ctrl", "z")
        setResponse("Done!")
    elif "redo" in cmd:
        pg.hotkey("ctrl", "y")
        setResponse("Done!")
    elif "show desktop" in cmd:
        pg.hotkey("win", "d")
        setResponse("Done!")
    elif "switch window" in cmd:
        pg.hotkey("alt", "tab")
        setResponse("Done!")
    elif "go back" in cmd:
        pg.hotkey("alt", "left")
        setResponse("Done!")
    elif "go forward" in cmd:
        pg.hotkey("alt", "right")
        setResponse("Done!")
    
    
def main():
    x = ref.get()
    if mac + "-e" in x:
        print("User: "+x[mac+"-e"])
        otp = sendOtp(x[mac+"-e"])
        print("Otp has been sent. It should be entered in your phone.")
        ref.update({
            mac+"-o": str(otp)
        })
    else:
        email = input("Enter your email: ")
        otp = sendOtp(email)
        userOtp = int(input("Enter Otp: "))
        if otp == userOtp:
            print("OTP Verification Success")
            ref.update({
                mac+"-e" : email,
                mac+"-o" : "null",
                mac+"-c" : "null",
            })
            print("Update success")
        else:
            print("Incorrect OTP")
        main()
    while True:
        k = ref.get()[mac+"-c"].lower()
        if k!="null":
            ref.update({
                mac+"-c": "null"
            })
            k = k[1:-1]
            print(k)
            execute(k)

main()