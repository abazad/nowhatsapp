YOUR_PHONE_NUMBER = raw_input("PhoneNumber -----> ")
fo = open("YOUR_PHONE_NUMBER.txt","w")
fo.write(YOUR_PHONE_NUMBER)
fo.close()

PASSWORD= raw_input("WhatsappPassword -----> ")
fo = open("PASSWORD.txt","w")
fo.write(PASSWORD)
fo.close()

WAY2SMS_LOGIN = raw_input("Way2SMSLogin -----> ")
fo = open("WAY2SMS_LOGIN.txt","w")
fo.write(WAY2SMS_LOGIN)
fo.close()

WAY2SMS_PASSWORD= raw_input("Way2SMSPassword -----> ")
fo = open("WAY2SMS_PASSWORD.txt","w")
fo.write(WAY2SMS_PASSWORD)
fo.close()

PhoneNumber= raw_input("PhoneNumber -----> ")
fo = open("PhoneNumber.txt","w")
fo.write(PhoneNumber)
fo.close()

print "\nThankyou"
