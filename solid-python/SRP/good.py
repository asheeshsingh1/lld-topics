class UserValidator:
    def validate(self, username: str, email: str):
        if not username or not email:
            raise ValueError("Username and email are required")

        if "@" not in email:
            raise ValueError("Invalid email format")
        
class UserRepository:
    def save(self, username: str, email: str):
        print(f"Saving user {username} to database")

class EmailService:
    def send_welcome_email(self, email: str):
        print(f"Sending welcome email to {email}")


class UserService:
    def __init__(self):
        self.validator = UserValidator()
        self.repository = UserRepository()
        self.email_service = EmailService()

    def create_user(self, username: str, email: str):
        self.validator.validate(username, email)
        self.repository.save(username, email)
        self.email_service.send_welcome_email(email)