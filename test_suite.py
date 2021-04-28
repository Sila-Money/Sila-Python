import coverage
import os
import unittest
import xmlrunner

from tests.test001_check_handle import Test001CheckHandleTest
from tests.test001_get_business_types import Test001GetBusinessTypesTest
from tests.test001_get_business_roles import Test001GetBusinessRolesTest
from tests.test001_get_naics_categories import Test001GetNaicsCategoriesTest
from tests.test002_get_entities import Test002GetEntitiesTest
from tests.test002_register import Test002RegisterTest
from tests.test003_0_register_registration_data import Test003RegistrationDataTests
from tests.test003_check_handle_failure import Test003CheckHandleFailTest
from tests.test003_link_business_member import Test003LinkBusinessMemberTest
from tests.test003_unlink_business_member import Test003UnlinkBusinessMemberTest
from tests.test004_request_kyc import Test004RequestKycTest
from tests.test005_check_kyc import Test005CheckKycTest
from tests.test005_check_partner_kyc import Test005CheckPartnerKycTest
from tests.test005_get_entity import Test005GetEntityTest
from tests.test005_z_documents import Test005ZDocuments
from tests.test006_certify_beneficial_owner import Test006CertifyBeneficialOwnerTest
from tests.test006_certify_business import Test006CertifyBusinessTest
from tests.test006_link_account import Test006LinkAccountTest
from tests.test006_plaid_link_token import Test006PlaidLinkTokenTest
from tests.test006_plaid_update_link_token import Test006PlaidUpdateLinkTokenTest
from tests.test007_get_accounts import Test007GetAccountsTest
from tests.test007_delete_account import Test007DeleteAccountTest
from tests.test007_update_account import Test007UpdateAccountTest
from tests.test008_get_account_balance import Test008GetAccountBalanceTest
from tests.test009_issue_sila import Test009IssueSilaTest
from tests.test010_transfer_sila import Test010TrasferSilaTest
from tests.test011_cancel_transaction import Test011CancelTransactionTest
from tests.test011_redeem_sila import Test011RedeemSilaTest
from tests.test012_get_transactions import Test012GetTransactionsTest
from tests.test013_plaid_same_day_auth import Test013PlaidSameDayAuthTest
from tests.test014_register_wallet import Test014RegisterWalletTest
from tests.test015_get_wallets import Test015GetWalletsTest
from tests.test016_get_wallet import Test016GetWalletTest
from tests.test017_update_wallet import Test017UpdateWalletTest
from tests.test018_delete_wallet import Test018DeleteWalletTest
from tests.test019_sila_balance import GetSilaBalanceTest


def create_suite(classes):
    suite = unittest.TestSuite()
    for _class in classes:
        _object = _class()
        for function_name in dir(_object):
            if function_name.lower().startswith("test"):
                suite.addTest(_class(function_name))
    return suite


def run_unit_tests():
    cov = coverage.Coverage()
    cov.start()
    results = os.path.abspath('./test-results.xml')
    with open(results, 'wb') as output:
        runner = xmlrunner.XMLTestRunner(output=output, verbosity=2)
        classes = [
            Test001CheckHandleTest,
            Test001GetBusinessTypesTest,
            Test001GetBusinessRolesTest,
            Test001GetNaicsCategoriesTest,
            Test002GetEntitiesTest,
            Test002RegisterTest,
            Test003RegistrationDataTests,
            Test003CheckHandleFailTest,
            Test003LinkBusinessMemberTest,
            Test003UnlinkBusinessMemberTest,
            Test004RequestKycTest,
            Test005GetEntityTest,
            Test005CheckKycTest,
            Test005CheckPartnerKycTest,
            Test005ZDocuments,
            Test006CertifyBeneficialOwnerTest,
            Test006CertifyBusinessTest,
            Test006LinkAccountTest,
            Test006PlaidUpdateLinkTokenTest,
            Test007DeleteAccountTest,
            Test007UpdateAccountTest,
            Test007GetAccountsTest,
            Test008GetAccountBalanceTest,
            Test009IssueSilaTest,
            Test010TrasferSilaTest,
            Test011CancelTransactionTest,
            Test011RedeemSilaTest,
            Test012GetTransactionsTest,
            Test013PlaidSameDayAuthTest,
            Test014RegisterWalletTest,
            Test015GetWalletsTest,
            Test016GetWalletTest,
            Test017UpdateWalletTest,
            Test018DeleteWalletTest,
            GetSilaBalanceTest
        ]
        runner.run(create_suite(classes))
    cov.stop()
    cov.save()

    cov.xml_report()


if __name__ == "__main__":
    run_unit_tests()
