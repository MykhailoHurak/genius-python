from abc import ABC, abstractclassmethod

class MakeCall(ABC):

    @abstractclassmethod
    def make_call(self):
        pass

class SendSms(ABC):

    @abstractclassmethod
    def make_call(self):
        pass

class GetInternet(ABC):

    @abstractclassmethod
    def get_internet(self):
        pass

class MobilePhone(MakeCall, SendSms, GetInternet):

    def make_call(self):
        print("Callint to abonent...")

    def send_sms(self):
        print("Sending SMS to abonent...")

    def get_internet(self):
        print("Getting connect to Internet...")

class StacionarPhone(MakeCall):

    def make_call(self):
        print("Callint to abonent...")

phone_01 = MobilePhone()
phone_01.make_call()
phone_01.send_sms()
phone_01.get_internet()

phone_02 = StacionarPhone()
phone_02.make_call()