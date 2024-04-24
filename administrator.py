class Administrator:
    """
    This class represents an adminstrator
    :Gregory Calderon
    :version 1.0
    """
    def __init__(self, n_adminName=None, n_adminEmail=None, n_hashPass=None):
 
        """
        Constructs a administrator

        :param n_name: (Optional) The name of the administrator.
        :type n_name: str
        :param n_email: (Optional) The email address of the administrator.
        :type n_email: str
        :param n_hashPass: (Optional) The hashed password of the administrator. 
        :type n_hashPass: str
        """

        self.__adminName = n_adminName
        self.__adminEmail = n_adminEmail
        self.__hashPass = n_hashPass 

    @property
    def adminName(self):
        """str: The name of the administrator."""
        return self.__adminName

    @adminName.setter
    def setAdminName(self, n_name):
        """
        Sets the administor's name.
        :param n_name: administrator's name.
        :type n_name: str
        """
        self.__adminName = n_name


    @property
    def adminEmail(self):
        """str: The email of the administrator."""
        return self.__adminEmail

    @adminEmail.setter
    def adminEmail(self, n_email):
        """
        Sets the administor's email.
        :param n_email: administrator's email.
        :type n_email: str
        """
        self.__adminEmail = n_email

    @property
    def hashPass(self):
        """str: The hashPass."""
        return self.__hashPass

    @hashPass.setter
    def hashPass(self, n_hashPass):
        """
        Sets the administor's hashPass.
        :param n_hashPass: administrator's hashPass.
        :type n_hashPass: str
        """
        self.__hashPass = n_hashPass