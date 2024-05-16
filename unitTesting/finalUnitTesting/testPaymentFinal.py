import unittest
from payment import PaymentClass


class TestPaymentClass(unittest.TestCase):

    """
    Tests the Payment class to ensure proper functionality
    :author: Arameh Baghdasarian
    :version: 1.0
    """
      
    def setUp(self):
        self.payment = PaymentClass(
            n_cardName="John Doe",
            n_cardNum="1234567890123456",
            n_securityCode="123",
            n_clientAddress="123 Main St",
            n_cityName="Anytown",
            n_zipCode="12345",
            n_expDate="12/24",
            n_currentDate="05/15/2024",
            n_paidAmount=100.0
        )

    def testSetAndGetName(self):
        self.payment.setName("Jane Doe")
        self.assertEqual(self.payment.name, "Jane Doe")

    def testSetAndGetCardNumber(self):
        self.payment.setcardNumber("6543210987654321")
        self.assertEqual(self.payment.number, "6543210987654321")

    def testSetAndGetSecurityCode(self):
        self.payment.setcardCode("321")
        self.assertEqual(self.payment.code, "321")

    def testSetAndGetAddress(self):
        self.payment.setAddress("456 Elm St")
        self.assertEqual(self.payment.address, "456 Elm St")

    def testSetAndGetCity(self):
        self.payment.setcityName("Othertown")
        self.assertEqual(self.payment.city, "Othertown")

    def testSetAndGetZipCode(self):
        self.payment.setzipCode("54321")
        self.assertEqual(self.payment.zip, "54321")

    def testSetAndGetExpireDate(self):
        self.payment.setExpireDate("01/25")
        self.assertEqual(self.payment.expireDate, "01/25")

    def testSetAndGetCurrentDate(self):
        self.payment.setcurrentDate("06/01/2024")
        self.assertEqual(self.payment.currentDate, "06/01/2024")

    def testSetAndGetPaidAmount(self):
        self.payment.__paidAmount = 200.0 
        self.assertEqual(self.payment.paidAmount, 200.0)

    def testSetAndGetPaymentId(self):
        self.payment.setPaymentId("abc123")
        self.assertEqual(self.payment.paymentId, "abc123")

if __name__ == '__main__':
    unittest.main()
