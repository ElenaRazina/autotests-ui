import pytest
from playwright.sync_api import Page
from pages.dashboard_page import DashboardPage

@pytest.fixture
def dashboard_page(chromium_page:Page)->DashboardPage:
    return DashboardPage(chromium_page)