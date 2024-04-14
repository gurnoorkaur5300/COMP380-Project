class Administrator:
    def __init__(self, n_adminName=None, n_adminEmail=None, n_hashPass=None):
        self.__adminName = n_adminName
        self.__adminEmail = n_adminEmail
        self.__hashPass = n_hashPass 

    @property
    def adminName(self):
        return self.__adminName

    @adminName.setter
    def setAdminName(self, n_name):
        self.__adminName = n_name


    @property
    def adminEmail(self):
        return self.__adminEmail

    @adminEmail.setter
    def adminEmail(self, n_email):
        self.__adminEmail = n_email

    @property
    def hashPass(self):
        return self.__hashPass

    @hashPass.setter
    def hashPass(self, n_hashPass):
        self.__hashPass = n_hashPass
