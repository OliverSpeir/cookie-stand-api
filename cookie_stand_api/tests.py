from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import CookieStand


class ItemTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_item = CookieStand.objects.create(
            location="somewhere",
            description="stand",
            hourly_sales=[23],
            minimum_customers_per_hour= 1,
            maximum_customers_per_hour=2,
            average_cookies_per_sale=1.0,
            owner=testuser1
        )
        test_item.save()

    def setUp(self):
        self.client.login(username="testuser1", password="pass")

    def test_item_model(self):
        item = CookieStand.objects.get(id=1)
        actual_owner = str(item.owner)
        actual_location = str(item.location)
        actual_description = str(item.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_location, "somewhere")
        self.assertEqual(
            actual_description, "stand"
        )

    def test_get_item_list(self):
        url = reverse("list_api")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        items = response.data
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["location"], "somewhere")

    def test_get_item_by_id(self):
        url = reverse("detail_api", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        item = response.data
        self.assertEqual(item["location"], "somewhere")

    def test_create_item(self):
        url = reverse("list_api")
        data = {"owner": 1, "location": "somewhere else", "description": "another stand"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        items = CookieStand.objects.all()
        self.assertEqual(len(items), 2)
        self.assertEqual(CookieStand.objects.get(id=2).location, "somewhere else")

    def test_update_item(self):
        url = reverse("detail_api", args=(1,))
        data = {
            "location": "somewhere new",
            "description": "stand",
            "hourly_sales": [23],
            "minimum_customers_per_hour": 1,
            "maximum_customers_per_hour": 2,
            "average_cookies_per_sale": 1.0,
            "owner": 1
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        item = CookieStand.objects.get(id=1)
        self.assertEqual(item.location, data["location"])
        self.assertEqual(item.owner.id, data["owner"])
        self.assertEqual(item.description, data["description"])

    def test_delete_item(self):
        url = reverse("detail_api", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        items = CookieStand.objects.all()
        self.assertEqual(len(items), 0)

    # added to template
    def test_authentication_required(self):
        self.client.logout()
        url = reverse("list_api")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
