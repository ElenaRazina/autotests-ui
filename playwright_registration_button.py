from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    """Запускаем браузер"""
    browser=playwright.chromium.launch(headless=False)
    page = browser.new_page()
    """Ждем, когда загрузится страница"""
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_button=page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.focus()
    for char in 'user.name@gmail.com':
        page.keyboard.type(char,delay=300)

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.focus()
    for char in 'username':
        page.keyboard.type(char, delay=300)

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.focus()
    for char in 'password':
        page.keyboard.type(char, delay=300)

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_enabled()

    page.wait_for_timeout(3000)