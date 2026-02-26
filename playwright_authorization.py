from playwright.sync_api import sync_playwright,expect
"""Подключили нужные библиотеки"""


"""Запускаем контекстный менеджер"""
with sync_playwright() as playwright:
    """Запускаем браузер"""
    browser=playwright.chromium.launch(headless=False)
    """Создаем новую страницу"""
    page=browser.new_page()
    """Указываем, куда странице нужно перейти"""
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    """Проверяем, что поле заполнено значением user.name@gmail.com"""
    #email_input=page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    #password_input=page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    password_input = page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill('password')

    """Покажем, как можно использовать data-testid"""
    #login_button=page.locator('//button[@data-testid="login-page-login-button"]')
    login_button=page.get_by_test_id('login-page-login-button')
    login_button.click()

    wrong_email_or_password_allert=page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    expect(wrong_email_or_password_allert).to_be_visible()
    expect(wrong_email_or_password_allert).to_have_text("Wrong email or password")

    """Ожидание для демо"""
    #page.wait_for_timeout(5000)
