import json
import os
from dataclasses import dataclass, asdict
from typing import List

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class User:
    def __init__(self, id, name, email, birthdate, password):
        self.id = id
        self.name = name
        self.email = email
        self.birthdate = birthdate
        self.password = self.set_password(password)

    
    def get_password(self):
        return self.password

   
    def set_password(self, newPassword):
     
            if not newPassword or len(str(newPassword).strip()) == 0:
                
                print("Favor preencher campo 'senha")
        
                return
    
            try:
                newPasswordToUpper = newPassword.upper()
                newPasswordReplaced = newPasswordToUpper.replace('A', 'Dsa')
                newPasswordReplaced2 = newPasswordReplaced.replace('E', '31C2as')
                newPasswordReplaced3 = newPasswordReplaced2.replace('I', 'ZAds')
                newPasswordReplaced4 = newPasswordReplaced3.replace('O', '0')
                newPasswordReplaced5 = newPasswordReplaced4.replace('U', 'au')
                newPasswordReplaced6 = newPasswordReplaced5.replace('@', 'l').replace('!', '21').replace('.', '/').replace('c', '.2')

                return newPasswordReplaced6

            except Exception as e:
                print(f"Erro inesperado ao processar senha: {e}")    


    def __repr__(self):
        return (f"User(id={self.id}, name='{self.name}', email='{self.email}',  password= '{self.password}', "
                f"birthdate='{self.birthdate}'")


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'birthdate': self.birthdate,
            'password': self.get_password()
        }


    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            name=data['name'],
            email=data['email'],
            birthdate=data['birthdate'],
            password=data['password']
        )


class UserModel:
    FILE_PATH = os.path.join(DATA_DIR, 'users.json')

    def __init__(self):
        self.users = self._load()


    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [User(**item) for item in data]


    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4, ensure_ascii=False)


    def get_all(self):
        return self.users


    def get_by_id(self, user_id: int):
        return next((u for u in self.users if u.id == user_id), None)


    def add_user(self, user: User):
        self.users.append(user)
        self._save()


    def update_user(self, updated_user: User):
        for i, user in enumerate(self.users):
            if user.id == updated_user.id:
                self.users[i] = updated_user
                self._save()
                break


    def delete_user(self, user_id: int):
        self.users = [u for u in self.users if u.id != user_id]
        self._save()