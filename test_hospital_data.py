import pandas as pd
import unittest


diagnosis_data = r'.\Diagnosis_Dataset\Diagnosis_Data.csv'

df = pd.read_csv(diagnosis_data)


class TestDataValidation(unittest.TestCase):

    def test_balance_amount(self):
        # Test if there are 0 balances
        self.assertEqual((df['BALANCE_AMOUNT'] == 0).all(), True)

        # Test if there are negative balances
        self.assertEqual((df['BALANCE_AMOUNT'] < 0).any(), True)

    def test_visit_date(self):
        # Test for invalid dates
        # invalid_dates = ['1500-02-01', '1900/02/04', '9999/01/05', '9999/02/07']
        for date in df['VISIT_DATE']:
            self.assertNotRegex(date, r'^\d{4}-\d{2}-\d{2}$')

        # Test for null Visit Date but time is populated
        self.assertTrue(df['VISIT_DATE'].isna().sum() == 0)

    def test_gender(self):
        # Test for blank rows for gender
        self.assertEqual((df['GENDER'] == ' ').any(), True)

    def test_currency(self):
        # Test if currency was not populated for records
        self.assertEqual(df['CURRENCY'].isna().sum(), 0)

    def test_total_charge(self):
        # Test for records with 0 total charge but INSURANCE_PAY and PATIENT_PAY amounts
        self.assertTrue(((df['TOTAL_CHARGE'] == 0) & (~df['INSURANCE_PAY'].isna()) & (~df['PATIENT_PAY'].isna())).any())

    def test_patient_payment_method(self):
        # Test if payment method was not provided for records
        self.assertEqual(df['PATIENT_PAYMENT_METHOD'].isna().sum(), 0)

    def test_patient_name(self):
        # Test for special characters in patient names
        special_characters = ['$', '@', '%', '#']
        for char in special_characters:
            self.assertTrue(df['PATIENT_NAME'].str.contains(char).any())

if __name__ == '__main__':
    unittest.main()
