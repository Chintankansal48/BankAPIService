from django.test import TestCase
from .models import Bank, Branch

class BankAPITestCase(TestCase):
    def setUp(self):
        bank = Bank.objects.create(name="Test Bank")
        Branch.objects.create(bank=bank, name="Test Branch", ifsc="TEST0001", city="Test City")

    def test_bank_list(self):
        response = self.client.get('/api/banks/')
        self.assertEqual(response.status_code, 200)

    def test_branch_detail(self):
        response = self.client.get('/api/branches/TEST0001/')
        self.assertEqual(response.status_code, 200)
