import pyttsx3
from googlesearch import search
from twilio.rest import Client
import cv2
import numpy as np
import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.text import MIMEText
import time
from datetime import datetime
from instagrapi import Client
import time
import psutil


print()
print("\t\t\t\t---------------------------------------------------------------------------")
print("\t\t\t\t-------------------------welcome to menu tool------------------------------")
print("\t\t\t\t---------------------------------------------------------------------------")
print()

def speaker() :
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50) 
    text=input("enter the sentence you want to spell by your system:  ")
    engine.say(text)
    engine.runAndWait()
    
def search_query():
    query = input("enter the word: ")

    # Search for top 5 results
    results = search(query, num=5, stop=5)

    # Print the URLs
    for result in results:
      print(result)
    
def whatsapp():
    account_sid = 'AC844e4e18de113b549745e761930e0f83'
    auth_token = '0474d1a5fea2db8386bc42a7699e8e99'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body='Hello preety',
    from_='whatsapp:+14155238886',
    to='whatsapp:+918709554389'
)

    print(message.sid)
    print("message sent successfully!!")
    
def message():
    account_sid = 'AC844e4e18de113b549745e761930e0f83'
    auth_token = '0474d1a5fea2db8386bc42a7699e8e99'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body='Hello preety, this is a test sms!',
    from_='+12054059248',
    to='+918709554389'
)

    print(message.sid)
    print("message sent successfully!!")
    
def call():
    account_sid = 'AC844e4e18de113b549745e761930e0f83'
    auth_token = '0474d1a5fea2db8386bc42a7699e8e99'
    client = Client(account_sid, auth_token)
    call = client.calls.create(
    twiml='<Response><Say>Hello, this is a test call from Twilio!</Say></Response>',
    from_='+1 205 405 9248',
    to='+918709554389'
)

    print(call.sid)
    print("calling....")
    
    
    
def photo():
    cap = cv2.VideoCapture(0)
    status , photo = cap.read()
    cv2.imshow("preety Photo" , photo)
    print("your photo!!")
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    
    

def image():
    # Create a blank image (height, width, channels)
    height = 500
    width = 500
    channels = 3  # For RGB
    image = np.zeros((height, width, channels), dtype=np.uint8)

    # Define colors
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Draw a red rectangle
    cv2.rectangle(image, (50, 50), (200, 200), red, -1)  # -1 to fill the rectangle

    # Draw a green circle
    cv2.circle(image, (300, 300), 50, green, -1)  # -1 to fill the circle

    # Draw a blue line
    cv2.line(image, (0, 0), (500, 500), blue, 5)

    # Put some text
    cv2.putText(image, 'Hello, Numpy!', (100, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)

    # Display the image
    cv2.imshow('Custom Image', image)
    print("here is your custom image!!")
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

    # Save the image
    cv2.imwrite('custom_image.png', image)
    
    
    
    
def email():

    # Replace the following with your details
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'preetyprincess2212@gmail.com'
    sender_password = 'xsum hgtk poqm font'
    recipient_email = 'preety04fe@gmail.com'
    subject = 'Subject of the Email'
    body = 'This is the body of the email.'

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)  # Login to the email server
    
        # Send the email
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
    
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
    finally:
        server.quit()
        
        
        
        
def schedule_email():

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'preetyprincess2212@gmail.com'
    sender_password = 'xsum hgtk poqm font'
    recipient_email = 'preety04fe@gmail.com'
    subject = 'Subject of the Email'
    body = 'This is the body of the email.'

    # Create the email
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # Set the time to send the email
    send_time = datetime(2024, 7, 23, 12, 0, 5)  # Year, Month, Day, Hour, Minute, Second

    # Calculate the delay in seconds
    delay = (send_time - datetime.now()).total_seconds()

    # Wait until the specified time
    time.sleep(max(0, delay))

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
    
        print("email sent successfully!!")
        
 



def filter_image():
    def capture_photo():
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                print("Error: Could not open webcam.")
                return
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame from webcam.")
                return
            cap.release()
            return frame
    def apply_filter(image):
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 100, 200)
            return edges
    def main():
            photo = capture_photo()
            if photo is None:
                return
            filtered_photo = apply_filter(photo)
            cv2.imshow('Original Photo', photo)
            cv2.imshow('Filtered Photo', filtered_photo)
            print("here is your filtered")
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    if __name__ == "__main__":
                main()
            
            
            
def insta():
    USERNAME = 'cloud.learner'
    PASSWORD = 'Preety@123'
    IMAGE_PATH = r'C:\Users\HP\Downloads\world.jpeg'
    CAPTION = 'I posted this image using python'

    cl = Client()

    # Login to Instagram
    print("Logging in to Instagram...")
    try:
        cl.login(USERNAME, PASSWORD)
    except Exception as e:
        print(f"Login failed: {e}")
        return

    # Try uploading the photo with retries in case of errors
    max_retries = 5
    retry_delay = 5  # seconds
    for attempt in range(max_retries):
        try:
            # Post the image with a caption
            print("Uploading photo to Instagram...")
            media = cl.photo_upload(IMAGE_PATH, CAPTION)
            print("Photo uploaded successfully.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("Max retries exceeded. Photo upload failed.")

    # Logout from Instagram
    cl.logout()
    print("Logged out from Instagram.")
    
    
    
    
def ram_read():
    # Get the total memory
    total_memory = psutil.virtual_memory().total

    # Get the available memory
    available_memory = psutil.virtual_memory().available

    # Get the used memory
    used_memory = psutil.virtual_memory().used

    # Get the percentage of used memory
    memory_percent = psutil.virtual_memory().percent

    print(f"Total Memory: {total_memory / (1024 ** 3):.2f} GB")
    print(f"Available Memory: {available_memory / (1024 ** 3):.2f} GB")
    print(f"Used Memory: {used_memory / (1024 ** 3):.2f} GB")
    print(f"Memory Usage: {memory_percent}%")



    

print("press 1: to Print any text and have it spoken aloud.")
print("""press 2: to Search for the top 5 results on Google.
press 3: to Send a WhatsApp message.
press 4: to Send a text message.
press 5: to Make a phone call.
press 6: to Post on Instagram.
press 7: to click a photo.
press 8: to Create a custom image.
press 9: to send an email.
press 10: to Schedule an email to be sent at a specific time.
press 11: to click a photo and apply filters in it.
press 12: to read the ram.
press any key to exit""")
while True:
    opt=int(input("enter the option: "))
    if opt==1 :
        speaker()
    elif opt==2 :
        search_query()
    elif opt==3 :
        whatsapp()
    elif opt==4 :
        message()
    elif opt==5 :
        call()
    elif opt==6 :
        insta()
    elif opt==7 :
        photo()
    elif opt==8 :
        image()
    elif opt==9 :
        email()
    elif opt==10 :
        schedule_email()
    elif opt==11 :
        filter_image()
    elif opt==12 :
        ram_read()
    else:
        break