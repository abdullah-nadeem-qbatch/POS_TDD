import unittest

class ProductTest(unittest.TestCase):
    def setUp(self):
        self.fixture = self._Fixture()


    def test_update_product(self):
        self.fixture.given_product_update(123, 'Biscuit', 25)
        self.fixture.when_update_operation_is_called()
        self.fixture.then_result_should_be(True)


    def test_is_price_positive_integer(self):
        self.fixture.given_product_update(234, 'Brownie', -100)
        self.fixture.when_update_operation_is_called()
        self.fixture.then_result_should_be(False)


    def test_valid_product_code(self):
        self.fixture.given_product_update(0000, 'Pastry', 50)
        self.fixture.when_update_operation_is_called()
        self.fixture.then_result_should_be(False)


    def test_product_availability(self):
        self.fixture.given_new_product(345, 'Doughnut', 75)
        self.fixture.when_product_availability_operation_is_called()
        self.fixture.then_result_should_be(True)


    def test_product_availability_failed(self):
        self.fixture.given_new_product(345, 'Cookie', 60)
        self.fixture.when_product_availability_operation_is_called()
        self.fixture.then_result_should_be(False)


    class _Fixture(unittest.TestCase):
        def __init__(self):
            self.product = Product()


        def given_new_product(self, code, name, price):
            self.code = code
            self.name = name
            self.price = price


        def given_product_update(self, code, name, price):
            self.code = code
            self.name = name
            self.price = price


        def when_update_operation_is_called(self):
            self.result = self.product.update(self.code, self.name, self.price)


        def when_product_availability_operation_is_called(self):
            self.result = self.product.is_available(self.code)


        def then_result_should_be(self, expected_result):
            self.assertAlmostEqual(self.result, expected_result)