from utils.driver_factory import get_driver
from pages.login_page import LoginPage


def test_valid_login():

    driver = get_driver()

    driver.get(
        "https://www.saucedemo.com/"
    )

    login = LoginPage(driver)

    login.enter_username(
        "standard_user"
    )

    login.enter_password(
        "secret_sauce"
    )

    login.click_login()

    assert "inventory" in driver.current_url

    driver.quit()


def test_invalid_login():

    driver = get_driver()

    driver.get(
        "https://www.saucedemo.com/"
    )

    login = LoginPage(driver)

    login.enter_username(
        "standard_user"
    )

    login.enter_password(
        "wrongpass"
    )

    login.click_login()

    assert "inventory" not in driver.current_url

    driver.quit()


def test_blank_username():

    driver = get_driver()

    driver.get(
        "https://www.saucedemo.com/"
    )

    login = LoginPage(driver)

    login.enter_password(
        "secret_sauce"
    )

    login.click_login()

    assert "inventory" not in driver.current_url

    driver.quit()


def test_blank_password():

    driver = get_driver()

    driver.get(
        "https://www.saucedemo.com/"
    )

    login = LoginPage(driver)

    login.enter_username(
        "standard_user"
    )

    login.click_login()

    assert "inventory" not in driver.current_url

    driver.quit()