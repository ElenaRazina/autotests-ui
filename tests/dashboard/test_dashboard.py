from pages.dashboard.dashboard_page import DashboardPage
import pytest
import allure
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpics
from tools.allure.features import AllureFeatures
from tools.allure.stories import AllureStories
from allure_commons.types import Severity
from tools.routes import AppRoute

@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(AllureTag.DASHBOARD, AllureTag.REGRESSION)
@allure.epic(AllureEpics.LMS)
@allure.feature(AllureFeatures.DASHBOARD)
@allure.story(AllureStories.DASHBOARD)
@allure.parent_suite(AllureEpics.LMS)
@allure.suite(AllureFeatures.DASHBOARD)
@allure.sub_suite(AllureStories.DASHBOARD)
class TestDashboard:
    @allure.title("Check displaying of Dashboard page")
    @allure.severity(Severity.NORMAL)
    def test_dashboard_displaying(self,dashboard_page_with_state:DashboardPage):
        #dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
        dashboard_page_with_state.visit(AppRoute.DASHBOARD)
        # Добавили проверку Navbar компонента на странице Dashboard
        dashboard_page_with_state.check_visible_navbar()
        dashboard_page_with_state.check_visible_sidebar()
        dashboard_page_with_state.check_visible_dashboard_title()
        dashboard_page_with_state.check_visible_scores_chart()
        dashboard_page_with_state.check_visible_courses_chart()
        dashboard_page_with_state.check_visible_students_chart()
        dashboard_page_with_state.check_visible_activities_chart()
        dashboard_page_with_state.navbar.check_visible('username')
        dashboard_page_with_state.sidebar.check_visible('Logout')
        dashboard_page_with_state.sidebar.check_visible('Courses')
        dashboard_page_with_state.sidebar.check_visible('Dashboard')

        #dashboard_page_with_state.check_visible_dashboard_title()
        #dashboard_page_with_state.check_visible_scores_chart()
        #dashboard_page_with_state.check_visible_courses_chart()
        #dashboard_page_with_state.check_visible_students_chart()
        #dashboard_page_with_state.check_visible_activities_chart()
