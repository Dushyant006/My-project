#Q1) Explore more regex patterns Eg. The regex pattern used to validate email addresses, mobile no, string, and more 
import re
email="yashdu2006@gmail.com"
pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")

phone="9876544411"
pattern = r"^[6-9]\d{9}$"
if re.match(pattern, phone):
    print("Valid phone number")
else:
    print("Invalid phone number")


pattern= r"^[A-Za-z]{5}[0-9]{4}$"
ragistration_number="ABCDE1234"
if re.match(pattern, ragistration_number):
    print("Valid registration number")
else:
    print("Invalid registration number")