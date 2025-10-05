import pandas as pd


# Load the data
diagnosis_data = r'data-non-errors.csv'
df = pd.read_csv(diagnosis_data)

def test_balance_amount():

    # Check if any balances are negative
    assert (df['BALANCE_AMOUNT'] >= 0).any()

def test_visit_date_format():
    # Check if all dates match the expected format YYYY-MM-DD
    assert df['VISIT_DATE'].str.match(r'^\d{4}/\d{2}/\d{2}$').any()

def test_visit_date_nulls():
    # Check for null Visit Dates
    assert df['VISIT_DATE'].isna().sum() == 0

def test_gender_blank_rows():
    # Check for blank gender values
    assert (df['GENDER'].str.strip() != '').any()

def test_currency_populated():
    # Check for missing currency values
    assert df['CURRENCY'].isna().sum() == 0

def test_total_charge_vs_payments():
    # Check for records with 0 total charge but populated INSURANCE_PAY and PATIENT_PAY
    condition = (df['TOTAL_CHARGE'] == 0) & df['INSURANCE_PAY'].notna() & df['PATIENT_PAY'].notna()
    assert condition.any()

def test_payment_method_provided():
    # Check for missing payment method
    assert df['PATIENT_PAYMENT_METHOD'].isna().sum() == 0

def test_patient_name_special_characters():
    # Check for special characters in patient names
    special_characters = ['$', '@', '%', '#']
    assert any(df['PATIENT_NAME'].str.contains(char).any() for char in special_characters)

