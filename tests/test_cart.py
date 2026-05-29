from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def login(driver):

    login_page = LoginPage(driver)

    login_page.enter_username(
        "standard_user"
    )

    login_page.enter_password(
        "secret_sauce"
    )

    login_page.click_login()


def test_add_product_to_cart():

    driver = get_driver()

    driver.get(
        "https://www.saucedemo.com/"
    )

    login(driver)

    inventory = InventoryPage(driver)

    inventory.add_product()

    assert inventory.get_cart_count() == "1"

    driver.quit()


def test_remove_product_from_cart():

    driver = get_driver()

    driver.get(
        "https://www.saucedemo.com/"
    )

    login(driver)

    inventory = InventoryPage(driver)

    inventory.add_product()

    inventory.remove_product()

    badge = driver.find_elements(
        *inventory.cart_badge
    )

    assert len(badge) == 0

    driver.quit()