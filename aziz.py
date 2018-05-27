#!usr/bin/bin

import smtplib
#content=' I am SHadhin'
message='i ama kasjdhioasjdlksah jdha sdioshdh asd'
aziz=['email1','email2','email3']
for i in aziz:

	mail = smtplib.SMTP('smtp.gmail.com',587)
	mail.ehlo()
	mail.starttls()
	mail.login('your_email_that_you_from','pass_from')
	mail.sendmail('your_email_that_you_from',i,message)
	mail.close()


