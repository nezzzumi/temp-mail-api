## How to import

```
>>> from temp_mail import TempMail

>>> t = TempMail()
```

## To get the actual email

```
>>> t.get_actual_email()
dxngoaiileax@sweatmail.com
```

## To get available domains
```
>>> t.get_available_domains()
['@upcmaill.com', '@hxqmail.com', '@mailernam.com', '@mailezee.com', '@sweatmail.com', '@emailnube.com', '@remailsky.com', '@mrisemail.com', '@newe-mail.com', '@provamail.com']
```

## To set a new email

```
>>> t.set_email("example@upcmaill.com")
```

## To generate a new email

```
>>> t.get_actual_email()
'dxngoaiileax@sweatmail.com' # before gen a new email

>>> t.generate_new_email()

>>> t.get_actual_email()
'dotkaacxmfgc@mrisemail.com' # after gen a new email
```

## To check the inbox

```
>>> emails = t.check_inbox()
>>> emails
[<temp_mail.Email object at 0x7f55be059b10>, <temp_mail.Email object at 0x7f55be066ad0>] # two emails
```

## Reading the email

```
>>> email_1 = emails[0] # saving the first email into the variable

>>> email_1.get_sender()
'"Sr. Example" <example@example.com>'

>>> email_1.get_subject()
'This is the subject of the email.'

>>> email_1.get_text()
'This is the body of the email.'

>>> email_1.get_all()
{'from': '"Sr. Example" <example@example.com>', 'subject': 'This is the subject of the email.', 'body': 'This is the body of the email.'}

```
