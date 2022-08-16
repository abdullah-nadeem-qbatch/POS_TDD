import unittest

class TransactionTest(unittest.TestCase):
    def setUp(self):
        self.fixture = self._Fixture()


    def test_add_transaction(self):
        self.fixture.given_transaction()
        self.fixture.when_display_total_of_transaction_operation_is_called()
        self.fixture.then_result_should_be(True)


    def test_add_line_item(self):
        self.fixture.given_line_item()
        self.fixture.when_add_line_item_operation_is_called()
        self.fixture.then_result_should_be(True)


    def test_get_list_of_line_items(self):
        self.fixture.given_transaction()
        self.fixture.when_get_list_of_line_items_operation_is_called()
        self.fixture.then_result_should_be(True)


    def test_display_total_of_transaction(self):
        self.fixture.given_transaction()
        self.fixture.when_display_total_of_transaction_operation_is_called()
        self.fixture.then_result_should_be(True)

    
    def test_display_voided_line_items(self):
        self.fixture.given_transaction()
        self.fixture.when_display_voided_items_operation_is_called()
        self.fixture.then_result_should_be(True)


    def test_transaction_start(self):
        self.fixture.given_transaction()
        self.fixture.when_start_new_transaction_operation_is_called()
        self.fixture.then_result_should_be(True)


    def test_transaction_start_failed(self):
        self.fixture.given_transaction()
        self.fixture.when_start_new_transaction_operation_is_called()
        self.fixture.then_result_should_be(False)


    def test_transaction_closed(self):
        self.fixture.given_transaction()
        self.fixture.when_close_transaction_operation_is_called()
        self.fixture.then_result_should_be(True)


    def test_transaction_closed_failed(self):
        self.fixture.given_transaction()
        self.fixture.when_close_transaction_operation_is_called()
        self.fixture.then_result_should_be(False)


    class _Fixture(unittest.TestCase):
        def __init__(self):
            self.transaction = Transaction()


        def given_transaction(self):
            pass


        def given_line_item(self, line_item):
            self.line_item = line_item
            self.transaction.line_items.append(self.line_item)

        
        def when_add_line_item_operation_is_called(self):
            self.result = self.transaction.add_line_item_in_transaction(self.line_items)


        def when_display_total_of_transaction_operation_is_called(self):
            self.result = self.transaction.display_total_of_transaction()


        def when_get_list_of_line_items_operation_is_called(self):
            self.result = self.transaction.get_list_of_line_items()


        def when_display_voided_items_operation_is_called(self):
            self.result = self.transaction.display_voided_items()


        def when_start_new_transaction_operation_is_called(self):
            self.result = self.transaction.start_new_transaction()


        def when_close_transaction_operation_is_called(self):
            self.result = self.transaction.close_transaction()


        def then_result_should_be(self, expected_result):
            self.assertAlmostEqual(self.result, expected_result)
