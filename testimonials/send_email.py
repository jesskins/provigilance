from __future__ import print_function
import sys
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from dotenv import load_dotenv 
import os

# Load environment variables from .env file
load_dotenv()

# Ensure the correct number of arguments
if len(sys.argv) != 3:
    print("Usage: python send_email.py <recipient_email> <recipient_name>")
    sys.exit(1)

recipient_email = sys.argv[1]
recipient_name = sys.argv[2]

# Fetch API key from environment variable
api_key = os.getenv('SENDINBLUE_API_KEY')
if not api_key:
    raise ValueError("SENDINBLUE_API_KEY environment variable is not set")

# Print the API key to confirm it's being loaded correctly (optional, for debugging)
print(f"API Key: {api_key}")

# Configure API key authorization: api-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = api_key

# Create an instance of the API class
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

# Create the email object
send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
    to=[{"email": recipient_email, "name": recipient_name}],
    sender={"email": "provigilancetestimonial@gmail.com", "name": "Provigilance"},
    subject="Thank you for your Testimonial Submission",
    html_content=f"<html><body><p>Dear {recipient_name},</p><p>Thank you for submitting your testimonial! We appreciate your feedback.</p><p>Best Regards,<br>Your Company</br></p></body></html>"
)

try:
    # Send the email
    api_response = api_instance.send_transac_email(send_smtp_email)
    print("Email sent successfully:", api_response)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->send_transac_email: %s\n" % e)
