from bs4 import BeautifulSoup
import requests
import json
from email.message import EmailMessage
import ssl
import smtplib


ACCEPT_LANGUAGE = 'en-US,en;q=0.5'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0'
AMAZON_LINK = 'https://www.amazon.com/Acer-SFX14-42G-R607-Creator-LPDDR4X-Backlit/dp/B09R8ZHZSD?ref_=Oct_DLandingS_D_2bfd7679_83&th=1'
WHAT_I_WANT_TO_PAY = 790.00
ACCURACY = 20



header_parameters = {
    'Accept-Language': ACCEPT_LANGUAGE,
    'User-Agent': USER_AGENT,
}

response = requests.get(AMAZON_LINK, headers=header_parameters)
html_page = response.text
soup = BeautifulSoup(markup=html_page, features="html.parser")
html_price_section = soup.find_all(name='span', class_='a-offscreen')

html_section_text = [price.getText() for price in html_price_section]
price_text = html_section_text[0]

floating_price_number = float(price_text[1:])
price_target = WHAT_I_WANT_TO_PAY + ACCURACY
deal = floating_price_number <= price_target


print(f"\nIs the product's current price under the discount ${price_target} "
      f"range?: {deal}")

if deal:
    print(f'\nEmail sent...')
    email_sender = 'ISS.notifier.andrea@gmail.com'
    sender_psw = 'jgbmoatatlpdrmpq'
    email_receiver = 'andreamusic.bergantin@gmail.com'

    subject = 'Amazon product to buy!'

    body = f"""\n
    {AMAZON_LINK}\n
    current price: {price_text}
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, sender_psw)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


