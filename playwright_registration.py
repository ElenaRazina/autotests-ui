from playwright.sync_api import sync_playwright,expect
"""Подключили нужные библиотеки"""


"""Запускаем контекстный менеджер"""
with sync_playwright() as playwright:
    """Запускаем браузер"""
    browser=playwright.chromium.launch(headless=False)
    """Создаем новую страницу"""
    page=browser.new_page()
    """Указываем, куда странице нужно перейти"""
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    """Проверяем, что поле заполнено значением user.name@gmail.com"""
    #email_input=page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")
    page.wait_for_timeout(3000)

    username_input=page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill("username")
    page.wait_for_timeout(3000)

    #password_input=page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')
    page.wait_for_timeout(3000)

    """Покажем, как можно использовать data-testid"""
    #login_button=page.locator('//button[@data-testid="login-page-login-button"]')
    login_button=page.get_by_test_id('registration-page-registration-button')
    login_button.click()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    page.wait_for_timeout(3000)

    title=page.get_by_test_id('dashboard-toolbar-title-text')
    expect(title).to_have_text("Dashboard")

    """Ожидание для демо"""
    page.wait_for_timeout(3000)
