import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtplib.SMTP("smtp.gmail.com", port=587)
load_dotenv()

SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}
response = requests.get("https://www.amazon.com/Briefcase-Organizer-Expandable-Resisatant-Briefcases/dp/B06XJPQV74/ref=pd_ci_mcx_mh_mcx_views_0_image?pd_rd_w=gXlpA&content-id=amzn1.sym.bb21fc54-1dd8-448e-92bb-2ddce187f4ac%3Aamzn1.symc.40e6a10e-cbc4-4fa5-81e3-4435ff64d03b&pf_rd_p=bb21fc54-1dd8-448e-92bb-2ddce187f4ac&pf_rd_r=QN2ABBGF0MF4QYTKEE9R&pd_rd_wg=kVnQR&pd_rd_r=54042ddf-78d2-4739-a098-e77caf96ed0b&pd_rd_i=B06XJPQV74&th=1", headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
soup.prettify()

price = soup.find(name="span", class_="a-price-whole").get_text()
price += soup.find(name="span", class_="a-price-fraction").get_text()
print(price)

if float(price) < 22:
    # Create email with proper headers and encoding
    email_message = MIMEMultipart()
    email_message["From"] = EMAIL_ADDRESS
    email_message["To"] = "rchhatre15@gmail.com"
    email_message["Subject"] = "Messenger Bag Price Alert!"

    # Create the message body
    message = f"Ytonet Laptop Bag, Expandable Laptop Briefcases for Men Fits 17.3 Inch Laptop Case Computer Bags, Water Resistant Multi Compartments Mens Laptop Work Bag with Luggage Strap for Bussiness Travel, Black is now {price}\n"
    message += "https://www.amazon.com/Briefcase-Organizer-Expandable-Resisatant-Briefcases/dp/B06XJPQV74/ref=pd_ci_mcx_mh_mcx_views_0_image?pd_rd_w=gXlpA&content-id=amzn1.sym.bb21fc54-1dd8-448e-92bb-2ddce187f4ac%3Aamzn1.symc.40e6a10e-cbc4-4fa5-81e3-4435ff64d03b&pf_rd_p=bb21fc54-1dd8-448e-92bb-2ddce187f4ac&pf_rd_r=QN2ABBGF0MF4QYTKEE9R&pd_rd_wg=kVnQR&pd_rd_r=54042ddf-78d2-4739-a098-e77caf96ed0b&pd_rd_i=B06XJPQV74&th=1"
    
    email_message.attach(MIMEText(message, "plain"))

    with smtplib.SMTP(SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs="rchhatre15@gmail.com",
            msg=email_message.as_string()
        )
     