from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
import pytest
import allure
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpics
from tools.allure.features import AllureFeatures
from tools.allure.stories import AllureStories
from allure_commons.types import Severity
from tools.routes import AppRoute

@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGISTRATION, AllureTag.REGRESSION)
@allure.epic(AllureEpics.LMS)
@allure.feature(AllureFeatures.AUTHENTICATION)
@allure.story(AllureStories.REGISTRATION)
@allure.parent_suite(AllureEpics.LMS)
@allure.suite(AllureFeatures.AUTHENTICATION)
@allure.sub_suite(AllureStories.REGISTRATION)
class TestSuccessfulRegistration:
    @pytest.mark.xdist_group(
        name="authorization-group")
    @allure.title("User registration with correct email, username and password")
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.parametrize("email, username, password", [("user.name@gmail.com", "username", "password")])
    #pytest.mark.parametrize("email, username, password", [("settings.test_user.email", "settings.test_user.username", "settings.test_user.password")])
    def test_successful_registration1(self,registration_page:RegistrationPage, dashboard_page:DashboardPage, email:str, username:str, password:str):
        #registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.visit(AppRoute.REGISTRATION)
        #registration_page.fill_registration_form(email, username, password)
        registration_page.fill_registration_form(email, username, password)
        registration_page.check_visible_registration_form(email, username, password)
        registration_page.click_registration_button()
        dashboard_page.check_visible_dashboard_title()

