class Owner:
    def __init__(self, firstName, lastName, address, email, password):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.email = email
        self.password = password
        
    def printOwnerInfo(self):
        print(self.firstName)
        print(self.lastName)
        print(self.address)
        print(self.email)
        print(self.password)
    
    def getEmail(self):
        return self.email
        