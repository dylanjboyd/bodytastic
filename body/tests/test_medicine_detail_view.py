from django.urls import reverse
from body.tests.login_test_case import LoginTestCase
from django.utils.timezone import make_aware, timedelta, datetime, localtime

from body.tests.model_helpers import (
    create_consumption,
    create_ledger_entry,
    create_medicine,
    create_schedule,
)
from body.urls.medication import MEDICINE_DETAIL_ROUTE
from freezegun import freeze_time


@freeze_time(make_aware(datetime(2022, 3, 1)))
class MedicineDetailViewTests(LoginTestCase):
    def test_shows_last_five_consumptions(self):
        """
        Given a medicine with six consumptions,
        then only five should be shown in the summary view.
        """
        medicine = create_medicine(self.user, current_balance=6)
        for _ in range(6):
            create_consumption(medicine)

        response = self.client.get(reverse(MEDICINE_DETAIL_ROUTE, args=[medicine.pk]))
        self.assertContains(response, "2:25 p.m.", count=5)

    def test_shows_last_five_consumptions(self):
        """
        Given a medicine with six refills,
        then only five should be shown in the summary view.
        """
        medicine = create_medicine(self.user, current_balance=6)
        for _ in range(6):
            create_ledger_entry(medicine, 2)

        response = self.client.get(reverse(MEDICINE_DETAIL_ROUTE, args=[medicine.pk]))
        self.assertContains(response, "2 (2 left)", count=5)

    def test_with_refills(self):
        """
        Given a medicine with refills,
        then those refills should show in a table.
        """
        medicine = create_medicine(self.user, current_balance=1)
        create_ledger_entry(medicine, 5)
        response = self.client.get(reverse(MEDICINE_DETAIL_ROUTE, args=[medicine.pk]))
        self.assertContains(response, "5 (5 left)")

    def test_with_consumptions(self):
        """
        Given that a consumption exists for a medicine, it should be shown in the view.
        """
        medicine = create_medicine(self.user, current_balance=1)
        create_consumption(medicine)
        response = self.client.get(reverse(MEDICINE_DETAIL_ROUTE, args=[medicine.pk]))
        self.assertContains(response, "1 Jan 2022")
        self.assertContains(response, "2:25 p.m.")

    def test_with_schedule(self):
        medicine = create_medicine(self.user)
        create_schedule(
            medicine,
            localtime() - timedelta(days=1),
            localtime() + timedelta(days=1),
        )
        response = self.client.get(reverse(MEDICINE_DETAIL_ROUTE, args=[medicine.pk]))
        self.assertContains(response, "Every one day")
        self.assertContains(response, "Next:")
        self.assertContains(response, "2:25 p.m.")

    def test_with_schedule_without_end_date(self):
        medicine = create_medicine(self.user)
        create_schedule(
            medicine,
            localtime() - timedelta(days=1),
            None,
        )
        response = self.client.get(reverse(MEDICINE_DETAIL_ROUTE, args=[medicine.pk]))
        self.assertContains(response, "Every one day")
        self.assertContains(response, "Next:")
        self.assertContains(response, "2:25 p.m.")

    def test_with_schedule_in_past(self):
        medicine = create_medicine(self.user)
        create_schedule(
            medicine,
            localtime() - timedelta(days=2),
            localtime() - timedelta(days=1),
        )
        response = self.client.get(reverse(MEDICINE_DETAIL_ROUTE, args=[medicine.pk]))
        self.assertNotContains(response, "Next:")

    def test_with_schedule_in_future(self):
        medicine = create_medicine(self.user)
        create_schedule(
            medicine,
            localtime() + timedelta(days=1),
            localtime() + timedelta(days=2),
        )
        response = self.client.get(reverse(MEDICINE_DETAIL_ROUTE, args=[medicine.pk]))
        self.assertNotContains(response, "Next:")

    def test_shows_more_schedules_with_future(self):
        medicine = create_medicine(self.user)
        create_schedule(
            medicine,
            localtime() + timedelta(days=1),
            localtime() + timedelta(days=2),
        )
        response = self.client.get(reverse(MEDICINE_DETAIL_ROUTE, args=[medicine.pk]))
        self.assertContains(response, "More Schedules")

    def test_shows_more_schedules_with_past(self):
        medicine = create_medicine(self.user)
        create_schedule(
            medicine,
            localtime() - timedelta(days=2),
            localtime() - timedelta(days=1),
        )
        response = self.client.get(reverse(MEDICINE_DETAIL_ROUTE, args=[medicine.pk]))
        self.assertContains(response, "More Schedules")

    def test_doesnt_show_more_schedules_with_present(self):
        medicine = create_medicine(self.user)
        for _ in range(5):
            create_schedule(
                medicine,
                localtime() - timedelta(days=2),
                None,
            )
        response = self.client.get(reverse(MEDICINE_DETAIL_ROUTE, args=[medicine.pk]))
        self.assertContains(response, "Next:", count=5)
        self.assertNotContains(response, "More Schedules")

    def test_shows_more_schedules_with_gt_five_present(self):
        medicine = create_medicine(self.user)
        for _ in range(6):
            create_schedule(
                medicine,
                localtime() - timedelta(days=2),
                None,
            )
        response = self.client.get(reverse(MEDICINE_DETAIL_ROUTE, args=[medicine.pk]))
        self.assertContains(response, "Next:", count=5)
        self.assertContains(response, "More Schedules")
