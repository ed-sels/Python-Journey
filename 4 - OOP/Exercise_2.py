class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

        def describe(self):
            print(f"User: {self.username}, Email: {self.email}")

class AdminUser(User):
    def __init__(self, username, email, permissions):
        super().__init__(username, email)
        self.permissions = permissions

    def describe(self):
        print(f"Admin User: {self.username}, Email: {self.email}, Permissions: {self.permissions}")