import os
from datetime import datetime

from send_email import send_email

if __name__ == "__main__":
    try:    
        today = datetime.now().strftime("%d-%m-%Y")
        file_name = "IP7_HEALTH_CHECK_REPORT.html"
        path = "/var/www/html/"
        log_file = path+file_name
        subject = "Kisu ekta den"
        body = "Likhen apne nijer moto kora"
        mail_recipients_system_team = ["sirajul@atilimited.net","foyez@atilimited.net"]
        send_email(subject,body,mail_recipients_system_team,[path,file_name])
    except Exception as e:
	print(e)
        pass
