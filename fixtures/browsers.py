import pytest
from playwright.sync_api import sync_playwright, Page, Playwright
from pages.authentication.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest
#from allure_commons.types import AttachmentType
import allure
from tools.playwright.pages import initialize_playwright_page




#@pytest.fixture
#def chromium_page() ->Page:
#    with sync_playwright() as playwright:
#        browser=playwright.chromium.launch(headless=False)
#        yield browser.new_page()
#        browser.close()

#После установки плагина pytest-playwrigt можно использовать встроенную фикстуру, которая позволит создать объект Page
#Для этого не будет нужен модуль sync_playwright
@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright)->Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name)
    #browser=playwright.chromium.launch(headless=False)
    #context=browser.new_context(record_video_dir='./videos')
    #context = browser.new_context()
    #context.tracing.start(screenshots=True, snapshots=True, sources=True)
    #yield context.new_page()
    #context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    #browser.close()
    #allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
    #allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)
    #allure.attach.file(page.video.path(), name='video', attachment_type=AttachmentType.WEBM)

@pytest.fixture
def initialize_browser_state(playwright: Playwright)->None:
    browser=playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
    registration_page.click_registration_button()

    #page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    #email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    #email_input.fill('user.name@gmail.com')
    #username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    #username_input.fill('username')
    #password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    #password_input.fill('password')
    #registration_button = page.get_by_test_id('registration-page-registration-button')
    #registration_button.click()

    context.storage_state(path='browser-state-3.json')
    browser.close()


@pytest.fixture
def chromium_page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright,test_name=request.node.name,storage_state="browser-state-3.json")
    #browser = playwright.chromium.launch(headless=False)
    #context = browser.new_context(storage_state='browser-state-3.json',record_video_dir='./videos')
    #context.tracing.start(
    #    screenshots=True,
    #    snapshots=True,
    #    sources=True)
    #page = context.new_page()
    #yield page
    #context.tracing.stop(
    #    path=f'./tracing/{request.node.name}.zip')
    #browser.close()
    #allure.attach.file(
    #    f'./tracing/{request.node.name}.zip',
    #    name='trace',
    #    extension='zip')
    #allure.attach.file(
    #    page.video.path(),
    #    name='video',
    #    attachment_type=allure.attachment_type.WEBM)