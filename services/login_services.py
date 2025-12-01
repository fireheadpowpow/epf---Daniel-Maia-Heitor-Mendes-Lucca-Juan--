from bottle import request
from config import Config
class LoginService:
     
    def secret_key(self, secretKeyDigitada):
            if(secretKeyDigitada != Config.SECRET_KEY):
                valid_session = False
                return valid_session
            else:
                valid_session = True
                return valid_session
                
            