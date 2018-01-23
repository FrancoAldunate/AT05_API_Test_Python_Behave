# Tests for SMS_Store class functions

import unittest
from FrancoAldunate.sms_store.messages import SMS_Store


class SMS_Store_TestCase(unittest.TestCase):
    def test_add_new_arrival_returns_message(self):
        sms_store = SMS_Store()
        expected_result = (False, '1000', '18:45', 'Hello')
        actual_result = sms_store.add_new_arrival('1000', '18:45', 'Hello')
        self.assertEqual(expected_result, actual_result)

    def test_message_count_returns_number_of_messages(self):
        sms_store = SMS_Store()
        sms_store.add_new_arrival('1000', '18:45', 'Hello')
        sms_store.add_new_arrival('1001', '19:55', 'World')
        expected_result = 2
        actual_result = sms_store.message_count()
        self.assertEqual(expected_result, actual_result)

    def test_message_count_returns_zero(self):
        sms_store = SMS_Store()
        expected_result = 0
        actual_result = sms_store.message_count()
        self.assertEqual(expected_result, actual_result)

    def test_get_unread_indexes_returns_different_than_zero(self):
        sms_store = SMS_Store()
        sms_store.add_new_arrival('1000', '18:45', 'Hello')
        sms_store.add_new_arrival('1001', '19:55', 'World')
        sms_store.get_message(0)
        expected_result = [0]
        actual_result = sms_store.get_unread_indexes()
        self.assertEqual(expected_result, actual_result)

    def test_get_unread_indexes_returns_zero(self):
        sms_store = SMS_Store()
        sms_store.add_new_arrival('1000', '18:45', 'Hello')
        sms_store.add_new_arrival('1001', '19:55', 'World')
        sms_store.get_message(0)
        sms_store.get_message(0)
        expected_result = []
        actual_result = sms_store.get_unread_indexes()
        self.assertEqual(expected_result, actual_result)

    def test_get_delete_returns_true(self):
        sms_store = SMS_Store()
        sms_store.add_new_arrival('1000', '18:45', 'Hello')
        sms_store.add_new_arrival('1001', '19:55', 'World')
        self.assertTrue(sms_store.delete(1))

    def test_get_delete_returns_false(self):
        sms_store = SMS_Store()
        sms_store.add_new_arrival('1000', '18:45', 'Hello')
        self.assertFalse(sms_store.delete(1))

    def test_clear_returns_empty_list(self):
        sms_store = SMS_Store()
        sms_store.add_new_arrival('1000', '18:45', 'Hello')
        sms_store.add_new_arrival('1001', '19:55', 'World')
        expected_result = []
        actual_result = sms_store.clear()
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
