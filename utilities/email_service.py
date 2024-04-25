import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from utilities.read_env import get_env



def send_email(to, message="", subject="", html_content=""):
    print(get_env('EMAIL'))
    EMAIL = 'appgainapp@outlook.com'
    PASSWORD = 'Appgainpassword1.'
    # Create a multipart message
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = EMAIL
    msg['To'] = to

    # Attach plain text part
    msg.attach(MIMEText(message, 'plain'))

    # Attach HTML part if provided
    if html_content:
        msg.attach(MIMEText(html_content, 'html'))

    try:
        # Connect to the server
        server = smtplib.SMTP("smtp.office365.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        # Login
        server.login(EMAIL, PASSWORD)

        # Send the message
        server.sendmail(EMAIL, to, msg.as_string())
        print('Email Sent')
        
        # Close connection
        server.quit()
    except Exception as e:
        print("Error sending email:", str(e))

def send_order_confirmation_email(product_name, quantity, price , to, address, customer_name, order_id):     

    price = "$" + str(price)
    shipping_details = {
        "customer_name": customer_name,
        "address": address,
        "order_id":order_id, 
        "country": "Egypt"
    }

    # Inject variables into the HTML content using string formatting
    order_confirmation_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Order Confirmation</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }}

            .container {{
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background-color: #fff;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}

            h1, h2 {{
                color: #333;
                text-align: center;
            }}

            p {{
                color: #666;
                line-height: 1.6;
                margin-bottom: 20px;
            }}

            .thank-you {{
                font-size: 24px;
                font-weight: bold;
                text-align: center;
                margin-bottom: 30px;
            }}

            .order-details {{
                border-top: 1px solid #ccc;
                padding-top: 20px;
            }}

            .order-details table {{
                width: 100%;
                border-collapse: collapse;
            }}

            .order-details th, .order-details td {{
                padding: 10px;
                text-align: left;
                border-bottom: 1px solid #ccc;
            }}

            .order-details th {{
                background-color: #f9f9f9;
            }}

            .footer {{
                margin-top: 30px;
                text-align: center;
                color: #999;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Order Confirmation</h1>
            <p class="thank-you">Thank you for your purchase!</p>
            
            <div class="order-details">
                <h2>Order Details</h2>
                <table>
                    <tr>
                        <th>Product</th>
                        <th>Quantity</th>
                        <th>Price</th>
                    </tr>
                    <tr>
                        <td>{product_name}</td>
                        <td>{quantity}</td>
                        <td>{price}</td>
                    </tr>
                </table>
            </div>

            <p>Your order will be shipped to: {shipping_details.get('address')}, {shipping_details.get('country')}</p>
            <p>Order ID : {shipping_details['order_id']}<br>           
            

            
            <p class="footer">For any questions, please contact support@example.com</p>
        </div>
    </body>
    </html>
    """
    send_email(to=to, subject='Order Completion',html_content=order_confirmation_html)
    





