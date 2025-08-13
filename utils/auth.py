import bcrypt
import pandas as pd
import os

USER_DB = "database/users.csv"

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def register_user(username, password, role="user"):
    if not os.path.exists("database"):
        os.makedirs("database")
    try:
        df = pd.read_csv(USER_DB)
        if username in df['username'].values:
            return False, "Username already exists"
    except FileNotFoundError:
        df = pd.DataFrame(columns=["username", "password", "role"])

    hashed = hash_password(password)
    new_row = pd.DataFrame([[username, hashed, role]])
    new_row.to_csv(USER_DB, mode='a', header=not os.path.exists(USER_DB), index=False)
    return True, "User registered successfully"

def authenticate_user(username, password):
    try:
        df = pd.read_csv(USER_DB)
        user = df[df['username'] == username]
        if len(user) == 1:
            if check_password(password, user.iloc[0]['password']):
                return True, user.iloc[0]['role']
    except:
        pass
    return False, None
