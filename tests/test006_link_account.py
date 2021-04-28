import unittest
import silasdk

from tests.test_config import (
    app, eth_private_key, eth_private_key_4, instant_ach_handle, user_handle)


class Test006LinkAccountTest(unittest.TestCase):
    def test_link_account_200(self):
        payload = {
            "user_handle": user_handle,
            "account_name": "default",
            "account_number": "123456789012",
            "routing_number": "123456789",
            "account_type": "CHECKING",
        }

        response = silasdk.User.linkAccount(
            app, payload, eth_private_key, False)
        
        self.assertEqual(response["status"], "SUCCESS")
        
        payload = {
            "user_handle": user_handle,
            "account_name": "unlink",
            "account_number": "123456789013",
            "routing_number": "123456780",
            "account_type": "CHECKING",
        }

        response = silasdk.User.linkAccount(
            app, payload, eth_private_key, False)
        
        self.assertEqual(response["status"], "SUCCESS")

        payload = {
            "user_handle": user_handle,
            "account_name": "forupdate",
            "account_number": "123456789013",
            "routing_number": "123456780",
            "account_type": "CHECKING",
        }

        response = silasdk.User.linkAccount(
            app, payload, eth_private_key, False)
        
        self.assertEqual(response["status"], "SUCCESS")

    def test_link_account_instant_ach(self):
        payload = {
            "user_handle": instant_ach_handle,
            "account_name": "default_plaid",
            "plaid_token": "sandbox"
        }

        response = silasdk.User.linkAccount(
            app, payload, eth_private_key_4, True)
        
        self.assertEqual(response["status"], "SUCCESS")

    def test_link_account_plaid_200(self):
        options = {
            "public_key": "fa9dd19eb40982275785b09760ab79",
            "initial_products": ["transactions"],
            "institution_id": "ins_109508",
            "credentials": {
                "username": "user_good",
                "password": "pass_good"
            }
        }

        plaid_response = app.postPlaid(
            "https://sandbox.plaid.com/link/item/create", options)
        payload = {
            "user_handle": user_handle,
            "account_name": "default_plaid",
            "public_token": plaid_response["public_token"],
            "selected_account_id": plaid_response["accounts"][0]["account_id"],
            "message": "link_account_msg"
        }

        response = silasdk.User.linkAccount(
            app, payload, eth_private_key, True)

        
        self.assertEqual(response["status"], "SUCCESS")
        self.assertIsNotNone(response['account_owner_name'])

        plaid_response = app.postPlaid(
            "https://sandbox.plaid.com/link/item/create", options)
        payload = {
            "user_handle": user_handle,
            "account_name": "default_plaid2",
            "plaid_token": plaid_response["public_token"],
            "message": "link_account_msg",
            "plaid_token_type": "legacy"
        }

        response = silasdk.User.linkAccount(
            app, payload, eth_private_key, True)

        
        self.assertEqual(response["status"], "SUCCESS")
        self.assertIsNotNone(response['account_owner_name'])

    def test_link_account_400(self):
        payload = {
            "account_name": "default",
            "plaid_token": ""
        }

        response = silasdk.User.linkAccount(app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")


if __name__ == '__main__':
    unittest.main()
