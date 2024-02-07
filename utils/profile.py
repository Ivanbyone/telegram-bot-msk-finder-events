class Profile:

    def __init__(self, 
                 id: int, 
                 username: str, 
                 fullname: str, 
                 role: str, 
                 attempts: int) -> None:
        
        self.id = id
        self.username = username
        self.fullname = fullname
        self.role = role
        self.attempts = attempts
