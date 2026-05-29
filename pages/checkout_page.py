from selenium.webdriver.common.by import By

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cart_icon = (
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    checkout_btn = (
        By.ID,
        "checkout"
    )

    first_name = (
        By.ID,
        "first-name"
    )

    last_name = (
        By.ID,
        "last-name"
    )

    postal_code = (
        By.ID,
        "postal-code"
    )

    continue_btn = (
        By.ID,
        "continue"
    )

    finish_btn = (
        By.ID,
        "finish"
    )

    success_msg = (
        By.CLASS_NAME,
        "complete-header"
    )

    def open_cart(self):
        self.driver.find_element(
            *self.cart_icon
        ).click()

    def click_checkout(self):
        self.driver.find_element(
            *self.checkout_btn
        ).click()

    def enter_details(
        self,
        fname,
        lname,
        pincode
    ):
        self.driver.find_element(
            *self.first_name
        ).send_keys(fname)

        self.driver.find_element(
            *self.last_name
        ).send_keys(lname)

        self.driver.find_element(
            *self.postal_code
        ).send_keys(pincode)

    def continue_checkout(self):
        self.driver.find_element(
            *self.continue_btn
        ).click()

    def finish_checkout(self):
        self.driver.find_element(
            *self.finish_btn
        ).click()

    def get_success_text(self):
        return self.driver.find_element(
            *self.success_msg
        ).text