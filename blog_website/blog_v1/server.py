from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__, static_url_path='/static')

smtplib.SMTP("smtp.gmail.com", port=587)
load_dotenv()

# Get environment variables
SMTP_ADDRESS = os.environ.get("SMTP_ADDRESS")
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
RECIPIENT_EMAIL = EMAIL_ADDRESS

@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/3feaf12bdef2e945ddea")
    blog_posts = response.json()
    return render_template("index.html", blog_posts=blog_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Get form data
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        # Create email content
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = f"New Contact Form Submission from {name} who has email: {email}"

        body = f"""
        New contact form submission:
        
        Name: {name}
        Email: {email}
        Phone: {phone}
        
        Message:
        {message}
        """
        
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Create and connect SMTP session
            connection = smtplib.SMTP(SMTP_ADDRESS, port=587)
            connection.starttls()
            connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
            connection.send_message(msg)
            return render_template("success.html")
        except Exception as e:
            print(f"Error sending email: {e}")
            return "Error sending message. Please try again later.", 500
    else:
        return render_template("contact.html")

@app.route("/post/<id>")
def post(id):
    try:
        response = requests.get("https://api.npoint.io/3feaf12bdef2e945ddea")
        post = response.json()[int(id)-1]
        return render_template("post.html", post=post)
    except Exception as e:
        return f"Error: {str(e)}", 404

if __name__ == "__main__":
    app.run(debug=True)