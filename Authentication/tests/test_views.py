from django.test import SimpleTestCase,TestCase
from Authentication.views import jobs,register,login
from django.urls import reverse,resolve


class UrlTest(SimpleTestCase):

    def check_if_login_test_is_resolved(self):
        assert 1==2