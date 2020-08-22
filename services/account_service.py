
from repo.user_repo import UserRepo
from services.service import Service
from utils import generate_uuid, timestamp, password_hash, password_verify
import traceback


class AccountService(Service):
    def signin(self, email, raw_password):
        try:
            user_repo = UserRepo()
            user_detail = user_repo.signin(email)
            if user_detail is None:
                return None
            else:
                if password_verify(raw_password, user_detail["password"]):
                    return user_detail["user"]
                else:
                    return None
        except Exception as e:
            traceback.print_exc()
            return None

    def signup(self, user_register):
        user = user_register.user
        password = password_hash(user_register.password)
        user.user_id = generate_uuid()
        user.created_at = timestamp()
        try:
            user_repo = UserRepo()
            if user_repo.save(user, password):
                return user
        except Exception as e:
            traceback.print_exc()
            return None
