from playwright.sync_api import expect,Page

from fixtures.pages import login_page
from pages.login_page import LoginPage
from components.authentication.login_form_component import LoginFormComponent
import pytest

@pytest.mark.parametrize(
    "email, password",
    [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),
        ("  ", "password"),
    ]
)
@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization1(login_page:LoginPage, email:str, password:str):
#def test_wrong_email_or_password_authorization1(chromium_page:Page, email:str, password:str):
#   login_page = LoginPage(chromium_page)

    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_page.fill(email, password)
    login_page.check_visible(email, password)
    #login_page.fill_login_form(email, password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()


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