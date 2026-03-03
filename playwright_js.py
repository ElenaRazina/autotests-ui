from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    """Запускаем браузер"""
    browser=playwright.chromium.launch(headless=False)
    page = browser.new_page()
    """Ждем, когда загрузится страница"""
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login", wait_until="networkidle")

    """Запускаем скрипты - первый способ через строку"""
    #text='New Text'
    #page.evaluate(
    #    """
    #    const title = document.getElementById('authentication-ui-course-title-text')
    #    title.textContent='{text}'
    #   """
    #)
    """Запускаем скрипты - второй способ через безымянную функцию"""
    new_text='New Text'
    page.evaluate(
        """
        (text) => {
            const title = document.getElementById('authentication-ui-course-title-text')
            title.textContent = text
        }
        """,
        new_text
    )
    page.wait_for_timeout(3000)