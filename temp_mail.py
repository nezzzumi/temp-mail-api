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

class TempMail:
    def __init__(self):
        self.gen_new_email()
    
    @property
    def actual_email(self) -> str:
        """return the actual email address"""
        return self.__actual_email

    def set_email(self, email: str):
        """set a new email"""
        domains = self.get_available_domains()
        if email[email.index("@"):] in domains:
            email_hash = hashlib.md5(email.encode("utf-8")).hexdigest()
            
            self.__actual_email = email
            self.__actual_email_hash = email_hash
        else:
            raise Exception(f"TempMail: {email[email.index('@'):]} doesn't exist.")
    
    @property
    def available_domains(self) -> list:
        """List all available domains"""

        response = requests.get("https://api4.temp-mail.org/request/domains/format/json", headers={"User-Agent": "okhttp/3.12.6"})
        domains = json.loads(response.text)
        
        return list(domains)
    
    def gen_new_email(self):
        """Generate an new temp-email"""

        domains = self.get_available_domains()
        email = "".join([random.choice(ascii_lowercase) for x in range(12)])+random.choice(domains)
        email_hash = hashlib.md5(email.encode("utf-8")).hexdigest()
        self.__actual_email = email
        self.__actual_email_hash = email_hash
    
    def check_inbox(self) -> list:
        """Check if you have a new email"""
        
        response = requests.get(f"https://api4.temp-mail.org/request/mail/id/{self.__actual_email_hash}/format/json", headers={"User-Agent": "okhttp/3.12.6"})
        response = json.loads(response.text)

        try:
            if "error" in response.keys(): #json with emails is a list
                return []
        except AttributeError:
            emails = []
            for i in response:
                emails.append(Email(i["mail_from"], i["mail_subject"], i["mail_text"]))
            
            return emails


class Email:
    def __init__(self, _from: str, subject: str, body: str):
        self.__from = _from
        self.__subject = subject
        self.__body = body


    @property
    def sender(self) -> str:
        """return who sent the email"""
        
        return self.__from

    @property
    def subject(self) -> str:
        """return email's subject"""
        
        return self.__subject

    @property
    def body(self) -> str:
        """return email's body"""
        
        return self.__body

    @property
    def all_info(self) -> dict:
        """return email's infos in a dict"""
        
        return {"from":self.__from, "subject": self.__subject, "body": self.__body}