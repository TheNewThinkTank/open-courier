
# import getpass
# from dotenv import load_env
import smtplib
import ssl


def send_email(msg, sender_email, password, receiver_email) -> None:
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    message = """\
    Subject: Test Subject!

    {}""".format(
        msg
    ).encode(
        "utf-8"
    )
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


def main() -> None:

    # msg = "A test message!"
    # sender_email = "someone@gmail.com" # input("sender-email:")
    # password = getpass.getpass(prompt="password:")
    # receiver_email = emails["Me"] # input("receiver-email:")

    # receiver_emails = [get_mail(person) for person in people]

    # send_email(msg, sender_email, password, receiver_email)
    ...


if __name__ == "__main__":
    main()
