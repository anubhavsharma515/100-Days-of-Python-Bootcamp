# SMTP = S[imple]M[ail]T[ransfer]P[rotocol]
# Mails go from client to sending server to receiver email server then to reciever client
# The rules that dictate this travel over different networks is SMTP

import smtplib
import os

# Didn't want to mistake having anything sensitive on GH, so passed things as env_vars
FROM_EMAIL = os.getenv('FROM_EMAIL')
PASS = os.getenv('PASS')
TO_EMAIL = os.getenv('TO_EMAIL')

if not(FROM_EMAIL or PASS or TO_EMAIL):
    raise ValueError('Could not find the required credentials')
else:
    # Taken from https://support.google.com/a/answer/176600?hl=en#:~:text=Dynamic%20IP%20addresses-,Setup%20steps,For%20TLS%2C%20enter%20587.
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as c:
        c.starttls()
        c.login(user=FROM_EMAIL, password=PASS)
        c.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAIL,
            msg="Subject:Test Email\n\nThis is a test email."
        )

