#multi level
class Phone:
    def call(self):
        print("calling...")

class MobilePhone(Phone):
    def send_sms(self):
        print("sending sms...")

class SmartPhone(MobilePhone):
    def browse(self):
        print("browsing...")

sp=SmartPhone()
sp.call()
sp.send_sms()
sp.browse()
