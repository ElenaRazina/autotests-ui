from playwright.sync_api import expect,Page
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
def test_wrong_email_or_password_authorization(chromium_page:Page, email:str, password:str):
        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        """Проверяем, что поле заполнено значением user.name@gmail.com"""
        # email_input=page.locator('//div[@data-testid="login-form-email-input"]//div//input')
        email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill(email)

        # password_input=page.locator('//div[@data-testid="login-form-password-input"]//div//input')
        password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
        password_input.fill(password)

        """Покажем, как можно использовать data-testid"""
        # login_button=page.locator('//button[@data-testid="login-page-login-button"]')
        login_button = chromium_page.get_by_test_id('login-page-login-button')
        login_button.click()

        wrong_email_or_password_allert = chromium_page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
        expect(wrong_email_or_password_allert).to_be_visible()
        expect(wrong_email_or_password_allert).to_have_text("Wrong email or password",timeout=1000)