# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from src.white_box import is_even, divide, get_grade, is_triangle, validate_login
from src.white_box import celsius_to_fahrenheit, validate_url, calculate_shipping_cost
from src.white_box import VendingMachine, TrafficLight, UserAuthentication
from src.white_box import DocumentEditingSystem, ElevatorSystem
from src.white_box import BankAccount, BankingSystem, Product, ShoppingCart


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when
        C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater
        or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is greater
        or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")

    """
    Gloria: 6, 10, 14, 18
    Rodrigo: 7, 11, 15, 19
    Tellez: 8, 12, 16, 20
    Pablo: 9, 13, 17, 21

    Everyone 22 - 28
    """

    # 6 - validate login

    def test_validate_login_success(self):
        """
        Tests valid login credentials.
        """
        self.assertEqual(
            validate_login("validUser", "securePassword"), "Login Successful"
        )

    def test_validate_login_failed(self):
        """
        Tests username that is too short --> Fail
        """
        self.assertEqual(validate_login("user", "securePassword"), "Login Failed")

    # 10 - celsius to fahrenheit

    def test_celsius_to_fahrenheit_valid(self):
        """
        Tests valid Celsius to Fahrenheit conversion.
        """
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_celsius_to_fahrenheit_invalid(self):
        """
        Tests invalid Celsius temperature.
        """
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")

    # 14 - validate URL
    def test_validate_url_valid(self):
        """
        Tests valid URLs.
        """
        self.assertEqual(validate_url("http://example.com"), "Valid URL")
        self.assertEqual(validate_url("https://example.com"), "Valid URL")

    def test_validate_url_invalid(self):
        """
        Tests invalid URLs.
        """
        self.assertEqual(validate_url("invalid_url"), "Invalid URL")
        self.assertEqual(validate_url("ftp://example.com"), "Invalid URL")

    # 18 - calculat shipping costs

    def test_calculate_shipping_cost(self):
        self.assertEqual(calculate_shipping_cost(0.5, 5, 5, 5), 5)  # Case 1
        self.assertEqual(calculate_shipping_cost(3, 20, 20, 20), 10)  # Case 2
        self.assertEqual(calculate_shipping_cost(3, 40, 40, 40), 20)  # Case 3
        self.assertEqual(calculate_shipping_cost(2, 5, 5, 5), 20)  # Case 3


# Test 22 - Vending Machine
class TestVendingMachine(unittest.TestCase):
    # Sets up the VendingMachine instance.
    def setUp(self):
        self.vm = VendingMachine()

    # Tests that the initial state is 'Ready'.
    def test_initial_state(self):
        self.assertEqual(self.vm.state, "Ready")

    # Tests inserting coin when machine is 'Ready'
    def test_insert_coin_ready(self):
        self.assertEqual(self.vm.insert_coin(), "Coin Inserted. Select your drink.")

    # Tests Invalidity when inserting a coin when  machine is 'Dispensing'.
    def test_insert_coin_dispensing(self):
        self.vm.insert_coin()
        self.assertEqual(self.vm.insert_coin(), "Invalid operation in current state.")

    # Tests selecting a drink after a coin has been inserted
    def test_select_drink_dispensing(self):
        self.vm.insert_coin()
        self.assertEqual(self.vm.select_drink(), "Drink Dispensed. Thank you!")

    # Tests selecting a drink without inserting a coin.
    def test_select_drink_ready(self):
        self.assertEqual(self.vm.select_drink(), "Invalid operation in current state.")


# Test 23 - TrafficLight
class TestTrafficLight(unittest.TestCase):
    # Sets up the TrafficLight
    def setUp(self):
        self.traffic_light = TrafficLight()

    # Change states and check each transition
    def test_change_state_red_to_green(self):
        # Check initial state
        self.assertEqual(self.traffic_light.get_current_state(), "Red")

        # Check states and changes
        self.traffic_light.change_state()  # Red -> Green
        self.assertEqual(self.traffic_light.get_current_state(), "Green")
        self.traffic_light.change_state()  # Green -> Yellow
        self.assertEqual(self.traffic_light.get_current_state(), "Yellow")
        self.traffic_light.change_state()  # Yellow -> Red
        self.assertEqual(self.traffic_light.get_current_state(), "Red")


# Test 24 - User Authentication
class TestUserAuthentication(unittest.TestCase):
    # Sets up the UserAuthentication instance.
    def setUp(self):
        self.auth = UserAuthentication()

    # Tests that the initial state is 'Logged Out'
    def test_initial_state(self):
        self.assertEqual(self.auth.state, "Logged Out")

    # Tests logging in when the user is logged out
    def test_login_success(self):
        self.assertEqual(self.auth.login(), "Login successful")

    # Tests logging in when the user is already logged in
    def test_login_invalid(self):
        self.auth.login()
        self.assertEqual(self.auth.login(), "Invalid operation in current state")

    # Tests logging out when the user is logged in
    def test_logout_success(self):
        self.auth.login()
        self.assertEqual(self.auth.logout(), "Logout successful")

    # Tests logging out when the user is already logged out
    def test_logout_invalid(self):
        self.assertEqual(self.auth.logout(), "Invalid operation in current state")


# Test 25 - Document Editing System
class TestDocumentEditingSystem(unittest.TestCase):
    # Sets up the DocumentEditingSystem instance.
    def setUp(self):
        self.document = DocumentEditingSystem()

    # Tests that the initial state is 'Editing'
    def test_initial_state(self):
        self.assertEqual(self.document.state, "Editing")

    # Tests saving the document while in 'Editing' state
    def test_save_document_success(self):
        self.assertEqual(self.document.save_document(), "Document saved successfully")

    # Tests saving the document while already in 'Saved' state
    def test_save_document_invalid(self):
        self.document.save_document()
        self.assertEqual(
            self.document.save_document(), "Invalid operation in current state"
        )

    # Tests resuming editing from 'Saved' state
    def test_edit_document_success(self):
        self.document.save_document()
        self.assertEqual(self.document.edit_document(), "Editing resumed")

    # Tests editing the document while already in 'Editing' state
    def test_edit_document_invalid(self):
        self.assertEqual(
            self.document.edit_document(), "Invalid operation in current state"
        )


# Test 26 - Elevator System
class TestElevatorSystem(unittest.TestCase):
    def setUp(self):
        self.elevator = ElevatorSystem()

    # Tests that the initial state is 'Idle'
    def test_initial_state(self):
        self.assertEqual(self.elevator.state, "Idle")

    # Tests moving the elevator up from 'Idle' state
    def test_move_up_valid(self):
        self.assertEqual(self.elevator.move_up(), "Elevator moving up")

    # Tests moving the elevator up from NOT'Idle' state
    def test_move_up_invalid(self):
        self.elevator.move_down()
        result = self.elevator.move_up()
        self.assertEqual(result, "Invalid operation in current state")

    # Tests moving the elevator down from 'Idle' state
    def test_move_down(self):
        self.assertEqual(self.elevator.move_down(), "Elevator moving down")

    # Tests moving the elevator up from NOT'Idle' state
    def test_move_down_invalid(self):
        self.elevator.move_up()
        result = self.elevator.move_down()
        self.assertEqual(result, "Invalid operation in current state")

    # Tests stopping the elevator when it is moving up.
    def test_stop_valid(self):
        self.elevator.move_up()  # Change state to Moving Up
        self.assertEqual(self.elevator.stop(), "Elevator stopped")

    # Tests stopping the elevator when it is idle
    def test_stop_invalid(self):
        self.assertEqual(self.elevator.stop(), "Invalid operation in current state")


# Test 27 - Banking System
class TestBankAccount(unittest.TestCase):
    # Sets up the BankAccount instance.
    def setUp(self):
        self.account = BankAccount("123456", 1000)

    # Tests that the initial account number and balance are set correctly.
    def test_initial_account_details(self):
        self.assertEqual(self.account.account_number, "123456")
        self.assertEqual(self.account.balance, 1000)

    # Tests viewing the account details.
    def test_view_account(self):
        result = self.account.view_account()
        self.assertEqual(result, "The account 123456 has a balance of 1000")


class TestBankingSystem(unittest.TestCase):
    # Sets up the BankingSystem instance.
    def setUp(self):
        self.banking = BankingSystem()
        self.banking.logged_in_users = set()  # Ensure logged_in_users is a set

    # Tests successful user authentication.
    def test_authenticate_success(self):
        # Reset login state before testing
        self.banking.logged_in_users.clear()  # Reset to avoid 'already logged in'
        result = self.banking.authenticate("user123", "pass123")
        self.assertEqual(result, "User user123 authenticated successfully.")

    # Tests trying to log in an already logged-in user.
    def test_authenticate_already_logged_in(self):
        self.banking.authenticate("user123", "pass123")  # First login
        result = self.banking.authenticate("user123", "pass123")  # Second login
        self.assertEqual(result, "User already logged in.")

    # Tests failed authentication with incorrect password.
    def test_authenticate_fail(self):
        result = self.banking.authenticate("user123", "wrongpass")
        self.assertEqual(result, "Authentication failed.")

    # Test successful regular transfer
    def test_transfer_success_regular(self):
        self.banking.authenticate("user123", "pass123")  # Log the user in for this test
        result = self.banking.transfer_money("user123", "receiver123", 100, "regular")
        expected = (
            "Money transfer of $100 (regular transfer) from user123 "
            "to receiver123 processed successfully."
        )
        self.assertEqual(result, expected)

    # Tests an invalid transaction type.
    def test_transfer_invalid_transaction_type(self):
        self.banking.authenticate("user123", "pass123")  # Log the user in for this test
        result = self.banking.transfer_money("user123", "receiver123", 100, "invalid")
        self.assertEqual(result, "Invalid transaction type.")

    # Tests transfer failure due to insufficient funds.
    def test_transfer_insufficient_funds(self):
        self.banking.authenticate("user123", "pass123")  # Log the user in for this test
        result = self.banking.transfer_money("user123", "receiver123", 2000, "regular")
        self.assertEqual(result, "Insufficient funds.")

    # Tests transfer when sender is not authenticated.
    def test_transfer_sender_not_authenticated(self):
        result = self.banking.transfer_money("user123", "receiver123", 100, "regular")
        self.assertEqual(
            result, "Sender not authenticated."
        )  # Ensure the return message is correct


# Test 28 - Shopping Cart
class TestProduct(unittest.TestCase):
    # Sets up the Product instance.
    def setUp(self):
        self.product = Product("Item", 10)

    # Tests that the initial product name and price are set correctly.
    def test_initial_product_details(self):
        self.assertEqual(self.product.name, "Item")
        self.assertEqual(self.product.price, 10)

    # Tests viewing the product details.
    def test_view_product(self):
        result = self.product.view_product()
        expected = "The product Item has a price of 10"
        self.assertEqual(result, expected)


class TestShoppingCart(unittest.TestCase):
    # Sets up the ShoppingCart instance.
    def setUp(self):
        self.cart = ShoppingCart()
        self.product = Product("Item", 10)

    # Tests adding a product to the shopping cart.
    def test_add_product(self):
        self.cart.add_product(self.product, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["quantity"], 2)

    # Tests removing a product from the shopping cart.
    def test_remove_product(self):
        self.cart.add_product(self.product, 2)
        self.cart.remove_product(self.product, 1)
        self.assertEqual(self.cart.items[0]["quantity"], 1)

    # Tests viewing the cart contents.
    def test_view_cart(self):
        self.cart.add_product(self.product, 2)
        expected_output = [f"2 x {self.product.name} - ${self.product.price * 2}"]
        self.assertEqual(self.cart.view_cart(), expected_output)

    # Tests checking out the shopping cart.
    def test_checkout(self):
        self.cart.add_product(self.product, 2)
        expected_output = (
            f"Total: ${self.product.price * 2}\n"
            "Checkout completed. Thank you for shopping!"
        )
        self.assertEqual(self.cart.checkout(), expected_output)


if __name__ == "__main__":
    unittest.main()
