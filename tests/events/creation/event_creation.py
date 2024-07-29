import time

from appium.webdriver.common.appiumby import AppiumBy

from core.ui.main_page.main_page import MainPage
from core.utils.readers import EnvManager
import logging
import pytest

logger = logging.getLogger(__name__)


@pytest.mark.smoke
@pytest.mark.event_creation
def test_event_creation_via_plus_button(driver):
    main_page: MainPage = MainPage(driver)

    logger.info("Step 0. Preconditions.")
    logger.info("Open Google Calendar.")
    button = main_page.get_next_button()
    button.click()
    button.click()
    main_page.get_done_button().click()
    assert main_page.get_settings_drawer_button().is_displayed(), "Google Calendar is not opened."

    logger.info("Select month events show type.")
    main_page.get_settings_drawer_button().click()
    main_page.get_settings_drawer_list()[5].click()

    logger.info("User can see calendar grid.")
    assert main_page.get_calendar_grid().is_displayed(), "Calendar month grid is not opened."

    logger.info("There are no events in the grid.")
    assert True  # todo: automate getting grid info

    logger.info("Step 1. Press plus button.")
    main_page.get_plus_button().click()
    logger.info("User can see screen with next buttons: Reminder, Event, Goal.")
    assert main_page.get_reminder_button().is_displayed(), "Reminder button is not visible."
    assert main_page.get_event_button().is_displayed(), "Event button is not visible."
    assert main_page.get_goal_button().is_displayed(), "Goal button is not visible."

    logger.info("Step 2. Press event button.")
    main_page.get_event_button().click()
    logger.info("Event creation screen is opened.")
    assert main_page.get_title_input().is_displayed()

    logger.info("Step 3. Fill name field with 'TestEvent' string.")
    main_page.get_title_input().send_keys("TestEvent")
    driver.hide_keyboard()
    logger.info("Done.")
    assert main_page.get_title_input().text == "TestEvent", "Text is not inserted."

    logger.info("Step 4. Select current date and time.")
    # todo: need more time to automate
    logger.info("Done.")
    assert True  # todo: util for time checking

    logger.info("Step 5. Press 'Does not repeat' button and select 'Every day' option in dialog.")
    main_page.get_does_not_repeat_button().click()
    main_page.get_does_not_repeat_list()[1].click()
    logger.info("Dialog is closed. 'Does not repeat' button changed text to 'Every day'.")
    assert True  # todo: need more time to automate dialog close check
    assert main_page.get_does_not_repeat_button_text() == "Every day", "Text of button is changed."

    logger.info("Step 6. Add a guest using 'test_guest@gmail.com' email.")
    main_page.get_add_people_button().click()
    main_page.get_add_people_input().send_keys(EnvManager.get_variable("my_email"))
    people_list = main_page.get_add_people_list()
    assert len(people_list) > 0, "At least 1 person was found."
    people_list[0].click()
    main_page.get_add_people_done_button().click()
    driver.hide_keyboard()
    driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollForward();'
    )
    logger.info("User can see the list of guests. "
                "User can see that video google conference info is added.")
    # assert main_page.get_people_list_field().is_displayed(), "There are no people added." xpath problem
    assert main_page.get_conference_info_text_field().text == "Hangouts Meet"

    logger.info("Step 7. Press 'Add rooms or location' button and select Odessa, Ukraine.")
    # todo: need more time to automate
    logger.info("User can see location info.")
    assert True  # todo: need more time to automate

    logger.info("Step 8. Add new notification 'in 20 minutes'.")
    # todo: need more time to automate
    logger.info("User can see notification 'in 20 minutes' in the notifications list.")
    assert True  # todo: need more time to automate

    logger.info("Step 9. Select Banana color of event.")
    # todo: need more time to automate
    logger.info("User can see that event color text is 'Banana'.")
    assert True  # todo: need more time to automate

    logger.info("Step 10. Add description text 'Text123'.")
    # todo: need more time to automate
    logger.info("User can see 'Text123' in the field.")
    assert True  # todo: need more time to automate

    logger.info("Step 11. Attach a file.")
    # todo: util for file attachment
    logger.info("User can see attached file in the attachments list.")
    assert True  # todo: need more time to automate

    logger.info("Step 12. Press Save button.")
    main_page.get_save_button().click()
    logger.info("Alert with text 'Send to guests...' and 'Send', "
                "'Don\'t send' and 'Cancel' options is appeared.")
    assert main_page.get_alert_save_send_button().is_displayed(), "Send button is not visible."
    assert main_page.get_alert_save_dont_send_button().is_displayed(), "Don\'t send button is not visible."
    assert main_page.get_alert_save_cancel_button().is_displayed(), "Cancel button is not visible."

    logger.info("Step 13. Press 'Don\'t send' button.")
    main_page.get_alert_save_dont_send_button().click()
    logger.info("Event creation screen is closed. "
                "User can see calendar grid with event icon in current date cell. "
                "Toast with text 'Saved...' is appeared.")
    assert True  # todo: need more time to automate dialog close check
    assert True  # todo: automate getting grid info
    assert True  # todo: automate toast reading


def test_event_copy():
    ...
