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

    def show_permissions(self):
        print(f"Admin User: {self.username}, Email: {self.email}, Permissions: {self.permissions}")

user1 = User("Joe Joestar", "jjoestar@uenr.com") # Creating instances of User and AdminUser
user1.describe()
admin1 = AdminUser("admin_user", "admin@uenr.com", ["add_user", "delete_user"])
admin1.describe()
admin1.show_permissions()