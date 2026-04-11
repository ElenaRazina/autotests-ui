from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
import pytest

@pytest.mark.regression
@pytest.mark.registration
class TestSuccessfulRegistration:

    @pytest.mark.parametrize("email, username, password", [("user.name@gmail.com", "username", "password")])

    def test_successful_registration1(self,registration_page:RegistrationPage, dashboard_page:DashboardPage, email:str, username:str, password:str):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        #registration_page.fill_registration_form(email, username, password)
        registration_page.fill_registration_form(email, username, password)
        registration_page.check_visible_registration_form(email, username, password)
        registration_page.click_registration_button()
        dashboard_page.check_visible_dashboard_title()

