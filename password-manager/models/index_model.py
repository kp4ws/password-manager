'''
Primary Author: Kent Pawson
Contributor(s): Azita Saleh
'''

class IndexModel:
    def __init__(self):
        self.captcha_completed = False
    
    def get_captcha_completed(self) -> bool:
        return self.captcha_completed
    
    def set_captcha_completed(self, captcha_completed) -> None:
        self.captcha_completed = captcha_completed