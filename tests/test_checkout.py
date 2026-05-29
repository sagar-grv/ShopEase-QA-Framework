from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


def login(driver):

    login_page = LoginPage(driver)

    login_page.enter_username(
        "standard_user"
    )

    login_page.enter_password(
        "secret_sauce"
    )

    login_page.click_login()


def test_successful_checkout():

    driver = get_driver()

    driver.get(
        "https://www.saucedemo.com/"
    )

    login(driver)

    inventory = InventoryPage(driver)

    inventory.add_product()

    checkout = CheckoutPage(driver)

    checkout.open_cart()

    checkout.click_checkout()

    checkout.enter_details(
        "Sagar",
        "Gurav",
        "425405"
    )

    checkout.continue_checkout()

    checkout.finish_checkout()

    assert (
        checkout.get_success_text()
        == "Thank you for your order!"
    )

    driver.quit()


def test_blank_checkout_form():

    driver = get_driver()

    driver.get(
        "https://www.saucedemo.com/"
    )

    login(driver)

    inventory = InventoryPage(driver)

    inventory.add_product()

    checkout = CheckoutPage(driver)

    checkout.open_cart()

    checkout.click_checkout()

    checkout.continue_checkout()

    assert "checkout-step-one" in driver.current_url

    driver.quit()