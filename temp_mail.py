#EternalChaos - 06/03/2020
#Author: Shi0n

import requests
import json
import random
import hashlib


ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
chars = ascii_lowercase + digits
#ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#ascii_letters = ascii_lowercase + ascii_uppercase
#punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

class TempMail():
    def __init__(self):
        self.generate_new_email()

    def set_email(self, email: str):
        domains = self.get_available_domains()
        if email[email.index("@"):] in domains:
            email_hash = hashlib.md5(email.encode("utf-8")).hexdigest()
            
            self.actual_email = email
            self.actual_email_hash = email_hash

    def get_available_domains(self) -> list:
        """List all available domains"""

        response = requests.get("https://api4.temp-mail.org/request/domains/format/json", headers={"User-Agent": "okhttp/3.12.6"})
        domains = json.loads(response.text)
        
        return list(domains)

    def generate_new_email(self):
        """Generate an new temp-email"""

        domains = self.get_available_domains()
        email = "".join([random.choice(ascii_lowercase) for x in range(12)])+random.choice(domains)
        email_hash = hashlib.md5(email.encode("utf-8")).hexdigest()
        self.actual_email = email
        self.actual_email_hash = email_hash
    
    def check_inbox(self) -> "json":
        """Check if you have a new email"""
        
        response = requests.get(f"https://api4.temp-mail.org/request/mail/id/{self.actual_email_hash}/format/json", headers={"User-Agent": "okhttp/3.12.6"})
        response = json.loads(response.text)

        try:
            if "error" in response.keys(): #json with emails is a list
                return response
        except AttributeError:
            emails_json = json.loads('{"emails":[]}')
            for i in response:
                json_to_append = json.loads(json.dumps({"from":i["mail_from"], "subject":i["mail_subject"], "mail_text":i["mail_text"]}))
                emails_json["emails"].append(json_to_append)
            return emails_json


            
