from django import forms
from django.forms import ModelForm
from .models import CookieStand


class CustomForm(ModelForm):
    class Meta:
        model = CookieStand
        fields = ('location', 'owner', 'description', 'hourly_sales', 'maximum_customers_per_hour', 'minimum_customers_per_hour', 'average_cookies_per_sale')
        widgets = {
            'location': forms.TextInput(attrs={'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg"
                                                    " focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "
                                                    "dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 "
                                                    "dark:text-white dark:focus:ring-blue-500 "
                                                    "dark:focus:border-blue-500"}),
            'owner': forms.Select(attrs={'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm "
                                                     "rounded-lg focus:ring-blue-500 focus:border-blue-500 "
                                                     "block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 "
                                                     "dark:placeholder-gray-400 dark:text-white "
                                                     "dark:focus:ring-blue-500 dark:focus:border-blue-500"}),
            'description': forms.TextInput(attrs={'class': "block w-full p-4 text-gray-900 border border-gray-300 "
                                                           "rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 "
                                                           "focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600"
                                                           " dark:placeholder-gray-400 dark:text-white "
                                                           "dark:focus:ring-blue-500 dark:focus:border-blue-500"}),
        }
