# NoWhatsapp
If you can't have an android phone, but still want to receive whatsapp text messages, (all personal and group messages), then 
NoWhatsapp is for you ! 

###Introduction

NoWhatsapp is a Whatsapp-Bot that will receive all the messages sent to you and will forward them to you via SMS on your mobile. Your friends get to know that message has reached you by the blue-ticks(as usual). 

###Requirements

1. Python2.7 or Python3.4

2. Way2SMS account(www.way2sms.com)

3. Install yowsup2 by: 

            $ sudo pip install yowsup2

###QuickStart

  1.Setting up Whatsapp Account

  (a) Request for Code through sms
  
            $ yowsup-cli registration --requestcode sms --phone <YOUR-PHONE-NUMBER> --cc <country-code>
    
          Eg: $yowsup-cli registration --requestcode sms --phone 919569252871 --cc 91
  
  (b) After receiving confirmation code through sms on <YOUR-PHONE-NUMBER> ,
  
             $yowsup-cli registration --register xxx-xxx --phone <YOUR-PHONE-NUMBER> --cc <country-code>
              
          Eg: yowsup-cli registration --register 594-816 --phone 919569252871 --cc 91
          
You will get your LOGIN(which will be the number you entered) and PASSWORD as the output. 

Copy your password, we'll need that later!


2.Create NewDirectory nowhatsapp and copy the project: 

          $ mkdir ~/nowhatsapp && cd ~/nowhatsapp
          
          $ git clone https://github.com/goru001/nowhatsapp.git
          
3.Configure:

          $ python start.py
          
          
You will be asked about :

(a). WhatsappLogin -----> YOUR-PHONE-NUMBER      

          Login-----> 919569252871

(b). WhatsappPassword -----> PASSWORD      

          Password -----> pt9idIEzfW0GP/LfGGXjpSrmxGI=

(c). Way2SMSLogin -----> WAY2SMS-LOGIN                  

          Way2SMSLogin ----->  9569252871

(d). Way2SMSPassword -----> WAY2SMS-PASSWORD            

          Way2SMSPassword -----> goru
          

###Usage

1. Whenever you'll execute:

        $ python run.py
        
  you will receive all the pending messages as sms! 
