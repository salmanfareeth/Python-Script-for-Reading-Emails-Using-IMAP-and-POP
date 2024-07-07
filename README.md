# Overview

This repository contains a Python script to read emails using IMAP and POP protocols. The script connects to a Gmail server, checks for unread messages, and processes them.

## Prerequisites

Before running the script, ensure you have Python installed on your system. This script is compatible with `Python 2.x`

## Getting Started

1. **Clone the Repository**

```sh
    git clone https://github.com/salmanfareeth/Python-Script-for-Reading-Emails-Using-IMAP-and-POP.git
```

2. **Navigate to the Project Directory:**

```sh
    cd read-mail-using-python
```

## Install Required Libraries

Ensure you have the necessary libraries. These are included in the standard library for `Python 2.x`

## Update Credentials

Open the script and update the `mailServer`, `imap_host`, `user_`, and `pass_` variables with your own details.

```sh
    mailServer = 'pop.gmail.com'
    imap_host = 'imap.gmail.com'
    user_ = 'your_email@gmail.com'
    pass_ = 'your_password'
```

## Running the Script

To run the script, use the following command:

```sh
    python readmail.py
```
    
## The script performs the following steps:

1. **Connect to Email Servers**

The script connects to the email servers using the `POP` and `IMAP` protocols.

```sh
    myEmailConnection = poplib.POP3_SSL(mailServer)
    imap = imaplib.IMAP4_SSL(imap_host)
    myEmailConnection.user(user_)
    myEmailConnection.pass_(pass_)
    imap.login(user_, pass_)
```

2. **Check for Unread Messages**
   
The script checks the status of the inbox for any unread messages.

```sh
    folderStatus, UnseenInfo = imap.status('INBOX', "(UNSEEN)")
    status, data = imap.select('INBOX')
    Process Mailbox
```

3. **The script processes the mailbox, fetches the unread messages, and prints their subject.**

```sh
    def process_mailbox(M):
      msg = []
      global Old
      rv, data = M.search(None, "ALL")
      if rv != 'OK':
          print "No messages found!"
          return
      NotReadCounter = int(UnseenInfo[0].split()[2].strip(').,]'))
      print "unread %d" % NotReadCounter
      if(NotReadCounter > 0):
        print("New mail received")
        for num in data[0].split():
          msg.append(int(num))
          print "!!!!!", msg
        rv, data = M.fetch(max(msg), '(RFC822)')
        if rv != 'OK':
          print "ERROR getting message", num
          return
        msg = email.message_from_string(data[0][1])
        print 'Message %s: %s' % (num, msg['Subject'])
        data = 'Message %s: %s' % (num, msg['Subject'])
        print data
        process_mailbox(imap)
```


## Educational Purpose Only

This project is created by `salmanfareeth` and is intended solely for educational purposes. Use it responsibly and modify it according to your needs.

## Privacy and Security

Be cautious about sharing your credentials and ensure they are stored securely. This script logs into your email account using your credentials, so handle your data with care.

## Legal Compliance

Ensure that your use of this script complies with the terms of service of your email provider and any relevant laws and regulations regarding automated email access.

## Disclaimer

Any damage or illegal usage resulting from this script is not my responsibility. 

## Troubleshooting

1. **Error While Logging In**
If you encounter an error while logging in, ensure that your email and password are correct and that the server addresses are accessible.

2. **Error While Fetching Messages** 
If an error occurs while fetching messages, check if you have the necessary permissions and that your mailbox is not empty.

## Contributing:

If you would like to contribute to this project, please fork the repository and create a pull request with your changes.
