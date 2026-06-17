"""Tính năng có lỗi cố ý — pipeline phải chặn."""
import jwt


def find(db, uid):
    return db.execute(f"SELECT * FROM accounts WHERE uid = {uid}")  # SQL injection


def decode(token):
    return jwt.decode(token, algorithms=["none"])  # JWT alg none


def run(x):
    return eval(f"f({x})")  # eval injection
