import unittest

class LineItemTest(unittest.TestCase):
    def setUp(self):
        self.fixture = self._Fixture()


    def test_total_balance(self):
        self.fail()


    def test_is_quantity_positive_integer(self):
        self.fixture.given_quantity_of_line_item(-10)
        self.fixture.when_update_quantity_of_line_item_operation_is_called()
        self.fixture.then_result_should_be(False)


    def test_add_quantity(self):
        self.fail()

    
    def test_update_quantity(self):
        self.fixture.given_quantity_of_line_item(20)
        self.fixture.when_update_quantity_of_line_item_operation_is_called()
        self.fixture.then_result_should_be(True)


    def test_void_line_item(self):
        self.fixture.given_line_item()
        self.fixture.when_void_line_item_operation_is_called()
        self.fixture.then_result_should_be(True)


    def test_show_voided_products(self):
        self.fixture.given_line_item()
        self.fixture.when_show_voided_products_operation_is_called()
        self.fixture.then_result_should_be(True)
    

    def test_total_balance(self):
        self.fixture.given_line_item()
        self.fixture.when_calculate_total_balance_operation_is_called()
        self.fixture.then_result_should_be(1000)


    class _Fixture(unittest.TestCase):
        def __init__(self):
            self.line_item = Line_item()

        
        def given_line_item(self):
            pass


        def given_quantity_of_line_item(self, quantity):
            self.quantity = quantity


        def when_update_quantity_of_line_item_operation_is_called(self):
            self.result = self.line_item.update_quantity_of_line_item()


        def when_calculate_total_balance_operation_is_called(self):
            self.result = self.line_item.calculate_total_balance(self.line_item)

        
        def when_void_line_item_operation_is_called(self):
            self.result = self.line_item.void_line_item()


        def when_show_voided_products_operation_is_called(self):
            self.result = self.line_item.show_voided_products()


        def then_result_should_be(self, expected_result):
            self.assertAlmostEqual(self.result, expected_result)