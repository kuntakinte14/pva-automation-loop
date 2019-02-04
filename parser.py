import dask.dataframe as dd
import subprocess
import time
import os
import datetime
import smtplib
import logging
import sys

FILENAME = 'data/data1.csv'
WAIT_TIME = 0
FROM = sys.argv[1]
TO = "" #set this variable with email at which you want to send emails to
PASSWORD = sys.argv[2]

logging.basicConfig(
        filename="logs.txt",
        filemode='a',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )
logger = logging.getLogger(__name__)


def parse_file():
    try:
        frames = dd.read_csv(FILENAME)
        return frames.compute()
    except Exception as e:
        logger.error(e)
        send_mail('data file not found, kindly check log.txt for more information.')
        sys.exit()


def loop_through_file(data):
    for fname, lname, email, cphone, company, proxy in \
            zip(data['fname'], data['lname'], data['email'], data['phone'], data['company'], data['proxy']):
        time.sleep(WAIT_TIME)
        try:
            subprocess.call(
                'echo "F@rzA1908!$" | sudo -S node pva/account_creation.js fname=[' + repr(fname) + '] lname=[' + repr(lname) + '] '
                'email=[' + repr(email) + '] cphone=[' + repr(cphone) + '] company=[' + repr(company) + '] '
                'proxy=[' + repr(proxy) + ']',shell=True
            )
        except Exception as e:
            logger.error(e)
            send_mail('Error Occured while Parsing the Data File, kindly check log.txt for more information.')
            sys.exit()


def rename_file():
    try:
        now = datetime.date.today()
        new_name = FILENAME + '-' + str(now) + '-' + 'DONE'
        print(new_name)
        os.rename(FILENAME, new_name)
    except Exception as e:
        logger.error(e)


def send_mail(msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(FROM, PASSWORD)
        server.sendmail(FROM, TO, msg)
        server.quit()
    except Exception as e:
        logger.error(e)


data = parse_file()
loop_through_file(data)
rename_file()
send_mail('Script is successfully Parsed Completely!!')

sys.exit()