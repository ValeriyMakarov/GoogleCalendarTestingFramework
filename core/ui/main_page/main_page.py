from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver import WebElement

from core.utils.readers import POMManager
from core.utils.singleton import Singleton


class MainPage(Singleton):
    def __init__(self, driver):
        if not self.initialized:
            self.fields = POMManager(__file__)
            self.driver = driver

    def get_settings_drawer_button(self) -> WebElement:
        return self.driver.find_element(
            by=AppiumBy.XPATH,
            value=self.fields["settings_drawer_button"]
        )

    def get_settings_drawer_list(self) -> list[WebElement]:
        return self.driver.find_elements(
            by=AppiumBy.XPATH,
            value=self.fields["drawer_list"]
        )

    def get_does_not_repeat_list(self) -> list[WebElement]:
        return self.driver.find_elements(
            by=AppiumBy.XPATH,
            value=self.fields["does_not_repeat_list"]
        )

    def get_people_list_field(self) -> WebElement:
        return self.driver.find_elements(
            by=AppiumBy.XPATH,
            value=self.fields["people_list_field"]
        )

    def get_add_people_list(self) -> list[WebElement]:
        return self.driver.find_elements(
            by=AppiumBy.XPATH,
            value=self.fields["add_people_list"]
        )

    def get_next_button(self) -> WebElement:
        return self.driver.find_element(
            by=AppiumBy.XPATH,
            value=self.fields["next_button"]
        )

    def get_done_button(self) -> WebElement:
        return self.driver.find_element(
            by=AppiumBy.XPATH,
            value=self.fields["done_button"]
        )

    def get_calendar_grid(self) -> WebElement:
        return self.driver.find_element(
            by=AppiumBy.XPATH,
            value=self.fields["calendar_grid"]
        )

    def get_plus_button(self) -> WebElement:
        return self.driver.find_element(
            by=AppiumBy.XPATH,
            value=self.fields["plus_button"]
        )

    def get_event_button(self) -> WebElement:
        return self.driver.find_element(
            by=AppiumBy.XPATH,
            value=self.fields["event_button"]
        )

    def get_reminder_button(self) -> WebElement:
        return self.driver.find_element(
            by=AppiumBy.XPATH,
            value=self.fields["reminder_button"]
        )

    def get_goal_button(self) -> WebElement:
        return self.driver.find_element(
            by=AppiumBy.XPATH,
            value=self.fields["goal_button"]
        )

    def get_title_input(self) -> WebElement:
        return self.driver.find_element(
            by=AppiumBy.XPATH,
            value=self.fields["title_input"]
        )

    def get_add_people_input(self) -> WebElement:
        return self.driver.find_element(
            by=AppiumBy.XPATH,
            value=self.fields["add_people_input"]
        )

    def get_does_not_repeat_button(self) -> WebElement:
        return self.driver.find_element(
            by=AppiumBy.XPATH,
            value=self.fields["does_not_repeat_button"]
        )

    def get_add_people_done_button(self) -> WebElement:
        return self.driver.find_element(
            by=AppiumBy.XPATH,
            value=self.fields["add_people_done_button"]
        )

    def get_add_people_button(self) -> WebElement:
        return self.driver.find_element(
            by=AppiumBy.XPATH,
            value=self.fields["add_people_button"]
        )

    def get_does_not_repeat_button_text(self) -> str:
        text_relative_path = "/android.widget.LinearLayout/android.widget.TextView"
        return self.driver.find_element(
            by=AppiumBy.XPATH,
            value=f"{self.fields['does_not_repeat_button']}{text_relative_path}"
        ).text

    def get_conference_info_text_field(self) -> WebElement:
        return self.driver.find_element(
            by=AppiumBy.XPATH,
            value=self.fields['conference_info_text_field']
        )

    def get_alert_save_cancel_button(self) -> WebElement:
        return self.driver.find_element(
            by=AppiumBy.XPATH,
            value=self.fields['alert_save_cancel_button']
        )

    def get_alert_save_dont_send_button(self) -> WebElement:
        return self.driver.find_element(
            by=AppiumBy.XPATH,
            value=self.fields['alert_save_dont_send_button']
        )

    def get_alert_save_send_button(self) -> WebElement:
        return self.driver.find_element(
            by=AppiumBy.XPATH,
            value=self.fields['alert_save_send_button']
        )

    def get_save_button(self) -> WebElement:
        return self.driver.find_element(
            by=AppiumBy.XPATH,
            value=self.fields['save_button']
        )

