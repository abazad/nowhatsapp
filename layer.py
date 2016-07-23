from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity
# For sms
import urllib2
import cookielib
import imaplib
import datetime
import re
#For converting unicode strings to ascii 
import unicodedata

class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over

        if True:
            receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())
            msg = messageProtocolEntity.getBody()
            msg = unicodedata.normalize('NFKD', msg).encode('ascii','ignore')
            fo = open("WAY2SMS_LOGIN.txt","r")
            WAY2SMS_LOGIN= fo.read()
            fo.close()
            fo = open("WAY2SMS_PASSWORD.txt","r")
            WAY2SMS_PASSWORD= fo.read()
            fo.close()
            fo = open("PhoneNumber.txt","r")
            PhoneNumber= fo.read()
            fo.close()
            username = WAY2SMS_LOGIN
            passwd = WAY2SMS_PASSWORD
            number = PhoneNumber
            message = 'From:%s'%(messageProtocolEntity.getFrom())+'\n'+msg
            url ='http://site24.way2sms.com/Login1.action?'
            data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
            cj= cookielib.CookieJar()
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
            usock =opener.open(url, data)
            jession_id =str(cj).split('~')[1].split(' ')[0]
            send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
            send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
            opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
            sms_sent_page = opener.open(send_sms_url,send_sms_data)
            #SMS has been sent
            message = messageProtocolEntity.getBody()
            message = str(message)
            message = message.strip()
            reply = 'I have replied you through sms, Please see!'
            if message.lower() == 'hi' or message.lower() == 'hello':
				reply = 'Hello, Kaise ho aap '
            outgoingMessageProtocolEntity = TextMessageProtocolEntity(reply,to = messageProtocolEntity.getFrom())
            self.toLower(receipt)
            self.toLower(outgoingMessageProtocolEntity)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
        self.toLower(ack)
