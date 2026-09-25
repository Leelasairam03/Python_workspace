from typing_extensions import override
class WhatsApp1:
    def send_message(self):
        print("single tick")

class WhatsApp2(WhatsApp1):
    @override
    def send_message(self):
        super().send_message()
        print("double tick")
    
    def send_audio(self):
        print("audio")

class WhatsApp3(WhatsApp2):
    @override
    def send_message(self):
        super().send_message()
        print("blue tick")
    
    @override
    def send_audio(self):
        super().send_audio()
        print("audio updated")
    
    def send_vedio(self):
        print("vedio")

w=WhatsApp3()
w.send_message()
w.send_audio()
w.send_vedio()


