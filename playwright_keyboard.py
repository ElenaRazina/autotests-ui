from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    """Запускаем браузер"""
    browser=playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    """Поставим фокус в поле"""
    email_input.focus()

    """Заполним с клавиатуры поле email"""
    for char in 'user@gmail.com':
        page.keyboard.type(char, delay=300)

    """Нажимаем комбинацию клавиш для выделения текста в поле"""
    page.keyboard.press("ControlOrMeta+A")

    page.wait_for_timeout(3000)