Schema = [
    {"header_msg": {
        "header": {
            "reference": "",
            "created": "",
            "user_handle": "",
            "app_handle": "",
            "version": "0.2",
            "crypto": "ETH"
        },
        "message": "header_msg",
        "kyc_level": "",
        "entity_type": ""
    }},
    {"link_account_msg_plaid": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "message": "link_account_msg",
        "plaid_token": "",
        "account_name": "",
        "selected_account_id": "",
        "plaid_token_type": ""
    }},
    {"link_account_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "message": "link_account_msg",
        "account_number": "",
        "routing_number": "",
        "account_type": "",
        "account_name": "",
        "selected_account_id": ""
    }},
    {"account_name_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
        },
        "account_name": ""
    }},
    {"transfer_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "message": "transfer_msg",
        "amount": "",
        "destination": "",
        "destination_handle": "",
        "destination_wallet": "",
        "destination_address": "",
        "business_uuid": "",
        "descriptor": ""
    }},
    {"issue_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "message": "issue_msg",
        "amount": "",
        "account_name": "",
        "business_uuid": "",
        "descriptor": "",
        "processing_type": ""
    }},
    {"redeem_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "message": "redeem_msg",
        "amount": "",
        "account_name": "",
        "business_uuid": "",
        "descriptor": "",
        "processing_type": ""
    }},
    {"no_content_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        }
    }},
    {"update_wallet_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "nickname": "",
        "default": ""
    }},
    {"register_wallet_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "wallet_verification_signature": "",
        "wallet": {
            "blockchain_address": "",
            "blockchain_network": "ETH",
            "nickname": ""
        }
    }},
    {"get_wallets_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "search_filters": {
            "page": "",
            "per_page": "",
            "sort_ascending": "",
            "blockchain_network": "",
            "blockchain_address": "",
            "nickname": ""
        }
    }},
    {"get_accounts_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "message": "get_accounts_msg"
    }},
    {"sila_balance_msg": {
        "address": ""
    }},
    {"business_types_msg": {
        "header": {
            "created": "",
            "app_handle": ""
        }
    }},
    {"business_roles_msg": {
        "header": {
            "created": "",
            "app_handle": ""
        }
    }},
    {"naics_categories_msg": {
        "header": {
            "created": "",
            "app_handle": ""
        }
    }},
    {"entity_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "version": "0.2",
            "crypto": "ETH",
            "reference": None
        },
        "message": "entity_msg",
        "address": {
            "address_alias": None,
            "street_address_1": None,
            "city": None,
            "state": None,
            "country": None,
            "postal_code": None,
            "street_address_2": None
        },
        "identity": {
            "identity_alias": None,
            "identity_value": None
        },
        "contact": {
            "contact_alias": None,
            "phone": None,
            "email": None,
            "sms_opt_in": None
        },
        "crypto_entry": {
            "crypto_alias": None,
            "crypto_code": "ETH",
            "crypto_address": None
        },
        "entity": {
            "first_name": None,
            "last_name": None,
            "entity_name": None,
            "birthdate": None,
            "relationship": None,
            "type": None,
            "business_type": None,
            "business_type_uuid": None,
            "business_website": None,
            "doing_business_as": None,
            "naics_code": None
        },
        "device": {
            "device_fingerprint": None
        }
    }},
    {"link_business_member_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "business_handle": ""
        },
        "role": "",
        "details": "",
        "ownership_stake": ""
    }},
    {"unlink_business_member_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "business_handle": ""
        },
        "role": ""
    }},
    {"get_entity_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": ""
        }
    }},
    {"certify_beneficial_owner_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "business_handle": ""
        },
        "member_handle": "",
        "certification_token": ""
    }},
    {"certify_business_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "business_handle": ""
        }
    }},
    {'get_transaction_msg': {
        "header": {
            "created": '',
            "app_handle": "",
            "user_handle": "",
            "version": "",
            "crypto": "",
            "reference": ""
        },
        "message": "get_transactions_msg",
        "search_filters": {
            "transaction_id": "",
            "reference_id": "",
            "show_timelines": '',
            "sort_ascending": '',
            "max_sila_amount": '',
            "min_sila_amount": '',
            "statuses": [],
            "start_epoch": '',
            "end_epoch": '',
            "page": '',
            "per_page": '',
            "transaction_types": []
        }
    }},
    {'cancel_transaction_msg': {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "",
            "crypto": "",
            "reference": ""
        },
        "transaction_id": ""
    }},
    {"add_registration_data_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None
        },
        "email": None,
        "phone": None,
        "identity_alias": None,
        "identity_value": None,
        "address_alias": None,
        "street_address_1": None,
        "street_address_2": None,
        "city": None,
        "state": None,
        "postal_code": None,
        "country": None,
        "sms_opt_in": None,
        "device_fingerprint": None
    }},
    {"update_registration_data_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None
        },
        "uuid": None,
        "email": None,
        "phone": None,
        "identity_alias": None,
        "identity_value": None,
        "address_alias": None,
        "street_address_1": None,
        "street_address_2": None,
        "city": None,
        "state": None,
        "postal_code": None,
        "country": None,
        "first_name": None,
        "last_name": None,
        "entity_name": None,
        "birthdate": None,
        "business_type": None,
        "naics_code": None,
        "doing_business_as": None,
        "business_website": None,
        "sms_opt_in": None
    }},
    {"delete_registration_data_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None
        },
        "uuid": None
    }},
    {"documents_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "message": "",
        "name": "",
        "filename": "",
        "hash": "",
        "mime_type": "",
        "document_type": "",
        "identity_type": "",
        "description": ""
    }},
    {"list_documents_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "",
            "crypto": "",
            "reference": ""
        },
        "message": "",
        "start_date": "",
        "end_date": "",
        "doc_types": "",
        "search": "",
        "sort_by": ""
    }},
    {"get_document_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "",
            "crypto": "",
            "reference": ""
        },
        "document_id": ""
    }},
    {"document_types_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "version": "",
            "crypto": "",
            "reference": ""
        }
    }},
    {"plaid_link_token_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
        }
    }},
    {"delete_account": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "account_name": ""
    }},
    {
        "check_partner_kyc": {
            "header": {
                "created": "",
                "app_handle": "",
                "version": "0.2",
                "crypto": "ETH",
                "reference": ""
            },
            "query_app_handle": "",
            "query_user_handle": ""
        }
    },
    {
        "update_account": {
            "header": {
                "created": "",
                "app_handle": "",
                "user_handle": "",
                "version": "0.2",
                "crypto": "ETH",
                "reference": ""
            },
            "account_name": "",
            "new_account_name": ""
        }
    },
    {
        "plaid_update_link_token": {
            "header": {
                "created": "",
                "app_handle": "",
                "user_handle": "",
            },
            "account_name": "",
        }
    }
]
