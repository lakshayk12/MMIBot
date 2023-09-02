from bs4 import BeautifulSoup
import requests
import smtplib
import ssl
from email.message import EmailMessage
import schedule


class Bot:
    def __init__(self, url, notifier_email, notifier_email_app_pswd, client_email):
        self.url = url
        self.client_email = client_email
        self.notifier_email = notifier_email
        self.pswd = notifier_email_app_pswd
        self.mmi_number = -1

    def email_alert(self):
        # Setup port number and server name
        smtp_port = 587  # Standard secure SMTP port
        smtp_server = "smtp.gmail.com"  # Google SMTP Server

        # content of message
        msg = EmailMessage()

        email_body = f"""
        Hey Buddy,
        
        Current Indian Market Mood Index is {self.mmi_number}.
        Visit {self.url} for more information.

        Cheers,
        Lakshay
        """
        msg.set_content(email_body)
        msg['subject'] = "Current Indian MMI: " + str(self.mmi_number)
        msg['to'] = self.client_email
        msg['from'] = self.notifier_email

        # Create context
        simple_email_context = ssl.create_default_context(cafile='cacert-2023-08-22.pem')

        try:
            # Connect to the server
            print("Connecting to server...")
            TIE_server = smtplib.SMTP(smtp_server, smtp_port)
            TIE_server.starttls(context=simple_email_context)
            TIE_server.login(self.notifier_email, self.pswd)
            print("Connected to server :-)")

            # Send the actual email
            print(f"Sending email to - {self.client_email}")
            TIE_server.sendmail(self.notifier_email, self.client_email, msg.as_string())
            print(f"Email successfully sent to - {self.client_email}")

        # If there's an error, print it out
        except Exception as e:
            print(e)

        # Close the port
        finally:
            TIE_server.quit()

    def check_market_mood(self):
        # Send an HTTP GET request to the webpage
        response = requests.get(self.url)

        # Create a BeautifulSoup object with the page content
        soup = BeautifulSoup(response.content, "html.parser")

        try:
            self.mmi_number = float(soup.find(class_='number').getText())
            print("Market Mood Index:", self.mmi_number)
            if self.mmi_number < 20:
                self.email_alert()
                print("Alert sent!")
            else:
                print("Market is not in Extreme Fear Zone!")
        except:
            print("Try Again!")

    def send_weekly_market_mood(self):
        # Schedule the task to run every Saturday evening at 6:00 PM
        schedule.every().saturday.at("18:00").do(self.check_market_mood)  # 18:00 is 6:00 PM

        # runs every 1 min: for testing...
        # schedule.every(1).minutes.do(self.check_market_mood)
        while True:
            schedule.run_pending()
