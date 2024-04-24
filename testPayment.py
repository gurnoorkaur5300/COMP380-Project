import unittest
from paymentClass import PaymentClass

class TestPayment(unittest.TestCase):
    def test_payment_creation(self):
        """
        This class represents the account page.
            :author: Martin Gallegos Cordero
            :version: 2.0
        """
        payment = PaymentClass(n_cardName = "Freddy Mercury", n_cardNumber= 1234567812345678, n_expirationDate = "03-24", n_hashCode = 123, n_clientAddress = "234 Bohemia Rapsody", n_zipCode=45321, n_cityName="London" )
        self.assertEqual(payment.name, "Freddy Mercury")
        self.assertEqual(payment.number, 1234567812345678)
        self.assertEqual(payment.date, "03-24")
        self.assertEqual(payment.code, 123)
        self.assertEqual(payment.address,"234 Bohemia Rapsody")
        self.assertEqual(payment.zip,45321)
        self.assertEqual(payment.city,"London")


    def test_payment_creation_with_defaults(self):
        payment = PaymentClass()
        self.assertIsNone(payment.name)
        self.assertIsNone(payment.number)
        self.assertIsNone(payment.date)
        self.assertIsNone(payment.code)
        self.assertIsNone(payment.address)
        self.assertIsNone(payment.zip)
        self.assertIsNone(payment.city)

    def test_setters(self):
        payment = PaymentClass
        payment.name = "Freddy Mercury" 
        self.assertEqual(payment.name, "Freddy Mercury")

        payment.number = 1234567812345678  
        self.assertEqual(payment.number, 1234567812345678)


        payment.date = "03-24"  
        self.assertEqual(payment.date, "03-24")


        payment.code = 123  
        self.assertEqual(payment.code, 123)

        payment.address = "234 Bohemia Rapsody"  
        self.assertEqual(payment.address, "234 Bohemia Rapsody")

        payment.zip = 45321  
        self.assertEqual(payment.zip, 45321)

        payment.city = "London"  
        self.assertEqual(payment.city, "London")


if __name__ == "__main__":
    unittest.main()