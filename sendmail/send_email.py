import smtplib
import os
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

def send_email(subject, body, to, attachment=[]):

    try:  

        from_email_address="sirajul@atilimited.net"
        from_email_password="AtiLtd@1993#"   # Put YOUR password here


        to_email_addresses=to
        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = from_email_address
        message['To'] = ','.join(to_email_addresses)
        # message['Cc'] = ''
        # message['Date'] = formatdate(localtime = True)
        message.preamble = subject
        message_txt = ("<html>"
                    "<head></head>"
                    "<body>"
                        "<h1 style='color:red'>%s</h1>"
                    "</body>"
                "</html>" % body)

        message.attach(MIMEText(message_txt, 'html'))
        
        
        if len(attachment)!=0 and os.path.exists(attachment[0]+attachment[1]):
            path = attachment[0]
            file_name = attachment[1]
            email_attachment = path+file_name
            logFile = open(email_attachment,"rb") # Open the file as binary mode
            attach_file = MIMEBase('application', 'octet-stream')
            attach_file.set_payload((logFile).read())
            encoders.encode_base64(attach_file) #encode the attachment
            #add payload header with filename
            attach_file.add_header('Content-Disposition', 'attachment', filename=file_name)
            message.attach(attach_file)


        smtp_conn = smtplib.SMTP("mail.atilimited.net", 587,timeout=3000)
        smtp_conn.starttls()
        smtp_conn.ehlo_or_helo_if_needed()
        smtp_conn.login(from_email_address, from_email_password)
        smtp_conn.sendmail(from_email_address, to_email_addresses, message.as_string())
        # smtp.sendmail(send_from, send_to.split(',') + msg['Cc'].split(','), msg.as_string())
        smtp_conn.quit()
    except Exception as e:
        pass

if __name__ == "__main__":
    send_email("Test","pthone test mail",["sirajul@atilimited.net"],[])

