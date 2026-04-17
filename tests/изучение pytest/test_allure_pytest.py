import allure

#этот декоратор вешается один на одну функцию. Т.е. нельзя указать несколько декораторов со step
@allure.step('Opening browser')
def open_browser():
    with allure.step('Get browser'):
        pass

    with allure.step('Start browser'):
        with allure.step('Get browser'):
            pass
        pass

@allure.step("Creating course with title '{title}'")
def create_course(title:str):
    #with allure.step(f'Creating course with title {title}'):
        #pass
    pass

@allure.step('Closing browser')
def close_browser():
    pass

#def test_feature():
#    with allure.step("Opening browser"):
#        pass
#    with allure.step("Creating course"):
#        pass
#    with allure.step("Closing browser"):
#        pass

def test_feature():
    open_browser()
    create_course(title="Locust")
    create_course(title="Pytest")
    create_course(title="Selenium")
    create_course(title="Playwright")
    close_browser()
