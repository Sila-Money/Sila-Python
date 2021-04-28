from .endpoints import endPoints
from silasdk import message
from silasdk.client import App
from silasdk.utils.url_parameters import UrlParameters
from typing import Optional
import warnings
import json
import requests


class User():
    def checkHandle(self, payload):
        """Check if the user handle is available.
        These endpoint returns the validity of a user handle
        Args:
        payload : Required user_handle to check if its available
        Returns:
        dict: response body (a confirmation message)
        """
        path = endPoints["checkHandle"]
        msg_type = "header_msg"
        response = message.postRequest(self, path, msg_type, payload)
        return response

    def register(self, payload):
        """Register a new user.
           This user will be kyced and ethereum address will be registered with sila 
        Args:
            payload : info about user like name,ssn, dob,ethereum address, ethereum handle etc
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["register"]
        msg_type = "entity_msg"
        response = message.postRequest(self, path, msg_type, payload)
        return response

    def requestKyc(self, payload, user_private_key, use_kyc_level=False):
        """Request kyc for a user by handle
           This user will be kyced and ethereum address will be registered with sila 
        Args:
            payload : info about user like name,ssn, dob,ethereum address, ethereum handle etc
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["requestKyc"]
        msg_type = "header_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def linkAccount(self, payload, user_private_key, plaid=False):
        """link the bank account of user using plad
           This users bank account will be linked  
        Args:
            payload : need user handle and plad token
            user_private_key: users ethereum private key 
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["linkAccount"]
        msg_type = ("link_account_msg" if (plaid is False)
                    else "link_account_msg_plaid")
        if payload.get('public_token') is not None:
            warnings.warn(
                'public_token is deprecated in favor of plaid_token', DeprecationWarning)
            payload.update({
                "plaid_token": payload.get('public_token')
            })
            payload.pop('public_token')
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def checkKyc(self, payload, user_private_key):
        """check if the user has been kyced.
            The user will be checked if the they have been kyced
        Args:
            payload : includes 
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["checkKyc"]
        msg_type = "header_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def addIdentity(self, payload, user_private_key):
        """change the info about user like change ssn, email ,etc.
            The used will be checked if the they have been kyced
        Args:
            payload : includes information to be edited and usee handle
            user_private_key: users ethereum private key 
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["addIdentity"]
        msg_type = "identity_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def getAccounts(self, payload, user_private_key):
        """get the accounts of users registered with sila
            The user will be checked if they have been kyced, along with app
        Args:
            user_hanlde: users handle registered with app
            user_private_key: user private key asscoicated with crypto address
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["getAccounts"]
        msg_type = "get_accounts_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def getAccountBalance(self, payload, user_private_key):
        """get the account balance of a user registered with sila
        Args:
            user_hanlde: users handle registered with app
            user_private_key: user private key asscoicated with crypto address
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["getAccountBalance"]
        msg_type = "account_name_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def getTransactions(app: App, payload: dict, user_private_key: str) -> dict:
        """get the users transactions registered with ur app
           The user will be checked if they have been kyced, along with app
        Args:
            user_hanlde: users handle registered with app
            user_private_key: user private key asscoicated with crypto address
        Returns:
            dict: response body (a confirmation message)
        """
        warnings.warn(
            'This method has been deprecated in favor of get_transactions', DeprecationWarning)
        return User.get_transactions(app, payload, user_private_key)

    @staticmethod
    def get_transactions(app: App, payload: dict, user_private_key: str = '') -> dict:
        if user_private_key != '':
            warnings.warn(
                'user_private_key is no longer needed, this will be removed in future versions.', DeprecationWarning)
        path = endPoints["getTransactions"]
        msg_type = "get_transaction_msg"
        response = message.postRequest(
            app, path, msg_type, payload)
        return response

    def silaBalance(self, address):
        """get sila balance of the addresses registered with sila
           The user will be checked if they have been kyced, along with app
        Args:
            address: requires valid ethereum address
        Returns:
            dict: response body (a confirmation message)
        """
        data = json.dumps({"address": str(address)})
        header = {'content-type': 'application/json'}
        if self.tier == "prod":
            endpoint = endPoints["silaBalanceProd"]
        elif self.tier == "sandbox":
            endpoint = endPoints["silaBalanceSandbox"]
        response = requests.post(endpoint, data=data, headers=header)
        return response.json()

    def getSilaBalance(self, address):
        """get sila balance of the addresses registered with sila
           The user will be checked if they have been kyced, along with app
        Args:
            address: requires valid ethereum address
        Returns:
            dict: response body (a confirmation message)
        """
        payload = {"address": str(address)}
        path = endPoints["getSilaBalance"]
        msg_type = "sila_balance_msg"
        response = message.postRequest(
            self, path, msg_type, payload)
        return response

    def getEntities(self, payload, per_page=None, page=None):
        """Return all end-user and legal entities (businesses) associated with a customer application.
            This endpoint allows the listing of all entities registered to an application.
        Args:
            payload: filters information
            per_page: pagination information
            page: pagination information
        Returns:
            dict: response body (entities list)
        """
        path = endPoints["getEntities"] + (('&per_page=' + str(per_page)) if per_page is not None else '') + (
            ('&page=' + str(page)) if page is not None else '')
        msg_type = "header_msg"
        response = message.postRequest(
            self, path, msg_type, payload)
        return response

    @staticmethod
    def getEntity(app: App, payload: dict, user_private_key: str, pretty_dates: Optional[bool] = None) -> dict:
        """
        Args:
            app (App): The current app configuration
            payload (dict): filters information
            user_private_key (str): The user's private key to sign the message
            pretty_dates (bool): Indicates if you want pretty dates in the response object
        Returns:
            dict: response body (entity information)
        """
        warnings.warn(
            'This method is deprecated in favor of get_entity', DeprecationWarning)
        return User.get_entity(app, payload, user_private_key)

    @staticmethod
    def get_entity(app: App, payload: dict, user_private_key: str, pretty_dates: Optional[bool] = None) -> dict:
        """
        Args:
            app (App): The current app configuration
            payload (dict): Filters information
            user_private_key (str): The user's private key to sign the message
            pretty_dates (bool): Indicates if you want pretty dates in the response object
        Returns:
            dict: response body (entity information)
        """
        path = endPoints["getEntity"]
        if pretty_dates:
            path += UrlParameters.add_query_parameter(
                "pretty_dates", "true")
        msg_type = "get_entity_msg"
        response = message.postRequest(
            app, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def addRegistrationData(app: App, registration_field: str, payload: dict, user_private_key: str) -> dict:
        """
        Args:
            payload: registration data
            user_private_key
        Returns:
            dict: response body (entity information)
        """
        warnings.warn(
            'This method has been deprecated in favor of add_registration_data', DeprecationWarning)
        return User.add_registration_data(app, registration_field, payload, user_private_key)

    @staticmethod
    def add_registration_data(app: App, registration_field: str, payload: dict, user_private_key: str) -> dict:
        path = endPoints["addRegistrationData"] + registration_field
        msg_type = "add_registration_data_msg"
        response = message.postRequest(
            app, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def updateRegistrationData(app: App, registration_field: str, payload: dict, user_private_key: str):
        """
        Args:
            app (App): The application configuration
            registration_field (str): The specific registration field to update
            payload (dict): registration data
            user_private_key (str): The user's private key to sign the message
        Returns:
            dict: response body (entity information)
        """
        warnings.warn(
            'This method has been deprecated in favor of update_registration_data', DeprecationWarning)
        return User.update_registration_data(app, registration_field, payload, user_private_key)

    @staticmethod
    def update_registration_data(app: App, registration_field: str, payload: dict, user_private_key: str) -> dict:
        path = endPoints["updateRegistrationData"] + registration_field
        msg_type = "update_registration_data_msg"
        response = message.postRequest(
            app, path, msg_type, payload, user_private_key)
        return response

    def deleteRegistrationData(self, registration_field, payload, user_private_key):
        """
        Args:
            payload: registration data
            user_private_key
        Returns:
            dict: response body (entity information)
        """
        path = endPoints["deleteRegistrationData"] + registration_field
        msg_type = "delete_registration_data_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def plaid_link_token(app: App, user_handle: str) -> dict:
        path = endPoints["plaid_link_token"]
        msg_type = "plaid_link_token_msg"
        payload = {"user_handle": user_handle}
        response = message.postRequest(
            app, path, msg_type, payload)
        return response

    @staticmethod
    def delete_account(app: App, payload: dict, user_private_key: str) -> dict:
        path = endPoints["delete_account"]
        msg_type = "delete_account"
        response = message.postRequest(
            app, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def check_partner_kyc(app: App, payload: dict) -> dict:
        path = "/check_partner_kyc"
        msg_type = "check_partner_kyc"
        response = message.postRequest(
            app, path, msg_type, payload)
        return response

    @staticmethod
    def update_account(app: App, payload: dict, user_private_key: str) -> dict:
        path = '/update_account'
        msg_type = "update_account"
        response = message.postRequest(
            app, path, msg_type, payload, user_private_key)
        return response

    @staticmethod
    def plaid_update_link_token(app: App, payload: dict) -> dict:
        path = endPoints["plaid_update_link_token"]
        msg_type = "plaid_update_link_token"
        response = message.postRequest(
            app, path, msg_type, payload)
        return response
