# read-mail-using-python
import imaplib
import poplib
import email
import datetime
import subprocess
mailServer = 'pop.gmail.com'
imap_host = 'imap.gmail.com'
user_ = 'username' 
pass_ = 'password'

myEmailConnection = poplib.POP3_SSL(mailServer)
imap = imaplib.IMAP4_SSL(imap_host)

myEmailConnection.user(user_)
myEmailConnection.pass_(pass_)

imap.login(user_, pass_)

folderStatus, UnseenInfo = imap.status('INBOX', "(UNSEEN)")

print folderStatus

status, data = imap.select('INBOX')

Old = 0
def process_mailbox(M):
  msg=[]
  global Old
  rv, data = M.search(None, "ALL")
  if rv != 'OK':
      print "No messages found!"
      return
  NotReadCounter = int(UnseenInfo[0].split()[2].strip(').,]'))
  print "unread %d" %NotReadCounter
  if(NotReadCounter > 0):
    print("New mail receved")
    for num in data[0].split():
      msg.append(int(num))
      print "!!!!!",msg
    rv, data = M.fetch(max(msg), '(RFC822)')
    if rv != 'OK':
      print "ERROR getting message", num
      return
    msg = email.message_from_string(data[0][1])
    print 'Message %s: %s' % (num, msg['Subject'])
    #print 'Raw Date:', msg['Date']
    #print msg
    data = 'Message %s: %s' % (num, msg['Subject'])
    print data

process_mailbox(imap)
