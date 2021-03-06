from body.tests.login_test_case import LoginTestCase
from body.tests.model_helpers import create_ledger_entry, create_medicine
from freezegun import freeze_time
from django.utils.timezone import make_aware, datetime


@freeze_time(make_aware(datetime(2022, 3, 1)))
class MedicineTests(LoginTestCase):
    def test_ledger_recalculates(self):
        """
        Recalculating the current balance of a medicine correctly uses ledger entries to do so.
        """
        medicine = create_medicine(self.user)
        create_ledger_entry(medicine, 4)
        create_ledger_entry(medicine, -1)
        medicine.recalculate_balance_from_ledger()
        self.assertEqual(medicine.current_balance, 3)
