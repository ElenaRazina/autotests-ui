import re

from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.authentication.login_form_component import LoginFormComponent
from elements.button import Button
import allure

#сначала указываем конструктор такой же, как в BasePage,
# чтобы инициализировать супер-класс корректно
# Супер-класс нужен, чтобы вызвать родительский класс
class LoginPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page)
        #self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        #self.password_input = page.get_by_test_id('login-form-password-input').locator('input')

        #self.login_button = page.get_by_test_id('login-page-login-button')
        #self.registration_link = page.get_by_test_id('login-page-registration-link')
        #self.wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')

        self.login_button = Button(page, 'login-page-login-button', 'Login')
        self.registration_link = Link(page,'login-page-registration-link', 'Registration')
        self.wrong_email_or_password_alert = Text(page,'login-page-wrong-email-or-password-alert', 'Wrong email or password')

    #def fill_login_form(self, email:str, password:str):
    #    self.email_input.fill(email)
    #    self.password_input.fill(password)
    #    expect(self.email_input).to_have_value(email)
    #    expect(self.password_input).to_have_value(password)

    def fill(self, email:str, password:str):
        self.login_form.fill(email, password)

    def check_visible(self, email:str, password:str):
        self.login_form.check_visible(email, password)

    def click_login_button(self):
        self.login_button.click()

    def click_registration_link(self):
        self.registration_link.click()
        self.check_current_url(re.compile(".*/#/auth/registration"))

    @allure.step('Check visible wrong email or password alert')
    def check_visible_wrong_email_or_password_alert(self):
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_text("Wrong email or password")

        #expect(self.wrong_email_or_password_alert).to_be_visible()
        #expect(self.wrong_email_or_password_alert).to_have_text("Wrong email or password")