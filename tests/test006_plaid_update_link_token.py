import unittest

from silasdk.users import User
from tests.test_config import *

class Test006PlaidUpdateLinkTokenTest(unittest.TestCase):
    def test_plaid_update_link_token_200(self):
        payload = {
            'user_handle': user_handle,
            'account_name': 'default_plaid'
        }
        response = User.plaid_update_link_token(app, payload)
        
        self.assertIsNotNone(response['status'])
        self.assertIsNotNone(response['message'])

if __name__ == '__main__':
    unittest.main()
