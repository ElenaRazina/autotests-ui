import pytest
from playwright.sync_api import Page
from pages.registration_page import RegistrationPage

@pytest.fixture
def registration_page(chromium_page:Page)->RegistrationPage:
    return RegistrationPage(chromium_page)