import speech_recognition as sr
import pyttsx3
import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import wikipedia
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def respond(text):
    engine.say(text)
    engine.runAndWait()
def get_weather(city):
    api_key = "your_openweather_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data.get('cod') == 200:
        temp = data['main']['temp']
        return f"The current temperature in {city} is {temp}°C."
    return "Sorry, I couldn't fetch the weather data."
def send_email(subject, body, to_email):
    """Send an email with the given subject and body."""
    from_email = "your_email@example.com"
    password = "your_password"
    smtp_server = "smtp.example.com"
    smtp_port = 587  # SMTP port for TLS
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
    return "Email sent successfully!"
def main():
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio).lower()
            print(f"Command received: {command}")

            if "hello" in command:
                respond("Hi there! How can I help you today?")

            elif "what time is it" in command:
                now = datetime.now()
                respond(f"The time is {now.strftime('%H:%M:%S')}")

            elif "what is the date" in command:
                now = datetime.now()
                respond(f"Today's date is {now.strftime('%Y-%m-%d')}")

            elif "search for" in command:
                query = command.replace("search for", "").strip()
                result = wikipedia.summary(query, sentences=1)
                respond(result)

            elif "weather in" in command:
                city = command.replace("weather in", "").strip()
                weather = get_weather(city)
                respond(weather)

            elif "send email" in command:
                respond("What is the subject of the email?")
                with sr.Microphone() as source:
                    audio = recognizer.listen(source)
                    subject = recognizer.recognize_google(audio)

                respond("What is the body of the email?")
                with sr.Microphone() as source:
                    audio = recognizer.listen(source)
                    body = recognizer.recognize_google(audio)

                respond("Who is the recipient?")
                with sr.Microphone() as source:
                    audio = recognizer.listen(source)
                    to_email = recognizer.recognize_google(audio)

                response = send_email(subject, body, to_email)
                respond(response)

            elif "stop" in command:
                respond("Goodbye!")
                break


if __name__ == "__main__":
    main()
