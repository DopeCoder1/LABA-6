class User:
    def __init__(self, id: int = 0, login: str = "", password: str = "", role: str = ""):
        self.id = id
        self.login = login
        self.password = password
        self.role = role

    def toString(self):
        return f"{self.id}) LOGIN:{self.login}      PASSWORD:{self.password}        ROLE:{self.role}"

    def set_id(self, id):
        self.id = id

    def set_login(self, login):
        self.login = login

    def set_password(self, password):
        self.password = password

    def set_role(self, role):
        self.role = role

    def get_id(self):
        return self.id

    def get_login(self):
        return self.login

    def get_password(self):
        return self.password

    def get_role(self):
        return self.role

