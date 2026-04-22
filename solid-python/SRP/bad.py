class UserManager:
    def create_user(self, username: str, email: str):
        # Validation logic
        if not username or not email:
            raise ValueError("Username and email are required")

        if "@" not in email:
            raise ValueError("Invalid email format")

        # Save to database (simulated)
        print(f"Saving user {username} to database")

        # Send welcome email
        print(f"Sending welcome email to {email}")