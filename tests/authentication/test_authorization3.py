from fixtures.pages import login_page
from pages.authentication.login_page import LoginPage
import pytest
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.login_page import LoginPage
import re
import allure
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpics
from tools.allure.features import AllureFeatures
from tools.allure.stories import AllureStories
from allure_commons.types import Severity

@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTag.AUTHORIZATION, AllureTag.REGRESSION)
@allure.epic(AllureEpics.LMS)
@allure.feature(AllureFeatures.AUTHENTICATION)
@allure.story(AllureStories.AUTHORIZATION)
class TestAuthorization:
    @allure.title("User login with correct email and password")
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(self, dashboard_page:DashboardPage, registration_page:RegistrationPage, login_page:LoginPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill(email="user.name@gmail.com", password="password", username="username")
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible('username')
        dashboard_page.sidebar.check_visible('Logout')
        dashboard_page.sidebar.click_logout()

        registration_page.page.wait_for_timeout(2000)

        login_page.login_form.fill(email='user.name@gmail.com',password='password')
        login_page.click_login_button()

        registration_page.page.wait_for_timeout(2000)

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible('username')
        dashboard_page.sidebar.check_visible('Logout')

        registration_page.page.wait_for_timeout(2000)



    @pytest.mark.parametrize(
        "email, password",
        [
            ("user.name@gmail.com", "password"),
            ("user.name@gmail.com", "  "),
            ("  ", "password"),
        ]
    )
    @allure.title("User login with wrong email or password")
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.severity(Severity.CRITICAL)
    def test_wrong_email_or_password_authorization1(self,login_page: LoginPage, email: str, password: str):
        #allure.dynamic.title(f"User login with wrong email or password: {email}")
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.fill(email, password)
        login_page.check_visible(email, password)
        # login_page.fill_login_form(email, password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()


    @allure.title("Navigate from login page to registration page")
    @allure.tag(AllureTag.NAVIGATION)
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_authorization_to_registration(self, login_page: LoginPage, registration_page: RegistrationPage):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.click_registration_link()
        registration_page.check_current_url(re.compile(".*#/auth/registration"))
        registration_page.registration_form.check_visible(email="", username="", password="")

#@pytest.mark.parametrize(
#    "email, password",
#    [
#        ("user.name@gmail.com", "password"),
#        ("user.name@gmail.com", "  "),
#        ("  ", "password"),
#    ]
#)
#@pytest.mark.regression
#@pytest.mark.authorization
#def test_wrong_email_or_password_authorization1(login_page:LoginPage, email:str, password:str):
#def test_wrong_email_or_password_authorization1(chromium_page:Page, email:str, password:str):
#   login_page = LoginPage(chromium_page)

#    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
#    login_page.fill(email, password)
#    login_page.check_visible(email, password)
    #login_page.fill_login_form(email, password)
#    login_page.click_login_button()
#    login_page.check_visible_wrong_email_or_password_alert()


    #код до использования Page Object
    #chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    #"""Проверяем, что поле заполнено значением user.name@gmail.com"""
    # email_input=page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    #email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    #email_input.fill(email)
    #chromium_page.wait_for_timeout(2000)

    # password_input=page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    #password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    #password_input.fill(password)
    #chromium_page.wait_for_timeout(2000)

    #"""Покажем, как можно использовать data-testid"""
    # login_button=page.locator('//button[@data-testid="login-page-login-button"]')
    #login_button = chromium_page.get_by_test_id('login-page-login-button')
    #login_button.click()
    #chromium_page.wait_for_timeout(2000)

    #wrong_email_or_password_allert = chromium_page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    #expect(wrong_email_or_password_allert).to_be_visible()
    #expect(wrong_email_or_password_allert).to_have_text("Wrong email or password",timeout=1000)

