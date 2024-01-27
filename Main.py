import os, pickle
import pandas as pd

WORKDIR = os.path.dirname(os.path.abspath(__file__))
USERS = pd.DataFrame(columns=["Users"])

class User:
    def __init__(self, name: str = "", 
                 firstname: str = "",
                 saldo: float = 0.0,
                 email: str = "",
                 status: bool = True) -> None:
        self.name= name
        self.firstname = firstname
        self.saldo = saldo
        self.email = email
        self.status = status
    
    def get_user_name(self):
        return (self.name, self.firstname)
    
    def get_status(self):
        return self.status
    
    def set_status(self, value: bool):
        self.status = value
    
    def get_email(self):
        return self.email
    
    def get_saldo(self):
        return self.saldo
    
    def change_saldo(self, amount: float):
        self.saldo += amount
    
def safe_data(input):
    input.to_pickle(f"{WORKDIR}/USERS.pkl")

def load_data():
    data = pd.read_pickle(f"{WORKDIR}/USERS.pkl")
    return data

def createUser(name: str, firstname: str, saldo: float, email: str, status: bool):
    initUser = User(name, firstname, saldo, email, status)
    return initUser








for i in [1,2,3]:
    lenUSERS = len(USERS)
    USERS.loc[lenUSERS] = createUser(f"{i}", f"{i}", i, f"{i}@{i}", True)
    print(USERS)

safe_data(USERS)
USERS_loaded = load_data()

for user in USERS["Users"]:
    print(f"ORIGINAL: {user.get_email()}")
for user_loaded in USERS_loaded["Users"]:
    print(f"LOADED:   {user_loaded.get_email()}")