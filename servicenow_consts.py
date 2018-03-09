# --
# File: servicenow_consts.py
#
# Copyright (c) Phantom Cyber Corporation, 2014-2018
#
# This unpublished material is proprietary to Phantom Cyber.
# All rights reserved. The methods and
# techniques described herein are considered trade secrets
# and/or confidential. Reproduction or distribution, in whole
# or in part, is forbidden except by express written permission
# of Phantom Cyber Corporation.
#
# --

SERVICENOW_JSON_DEVICE_URL = "url"
SERVICENOW_JSON_USERNAME = "username"
SERVICENOW_JSON_PASSWORD = "password"
SERVICENOW_JSON_CLIENT_ID = "client_id"
SERVICENOW_JSON_CLIENT_SECRET = "client_secret"
SERVICENOW_JSON_MAX_RESULTS = "max_results"
SERVICENOW_JSON_TOTAL_TICKETS = "total_tickets"
SERVICENOW_JSON_SHORT_DESCRIPTION = "short_description"
SERVICENOW_JSON_DESCRIPTION = "description"
SERVICENOW_JSON_NEW_TICKET_ID = "created_ticket_id"
SERVICENOW_JSON_GOT_TICKET_ID = "queried_ticket_id"
SERVICENOW_JSON_UPDATED_TICKET_ID = "updated_ticket_id"
SERVICENOW_JSON_TICKET_ID = "id"
SERVICENOW_JSON_FIELDS = "fields"
SERVICENOW_JSON_TABLE = "table"
SERVICENOW_JSON_FILTER_QUERY = "filter_query"
SERVICENOW_JSON_FIRST_RUN_MAX_ITEMS = "first_run_max_items"
SERVICENOW_JSON_INGEST_MANNER = "ingest_manner"
SERVICENOW_JSON_MAX_ITEMS = "max_items"
SERVICENOW_JSON_VAULT_ID = "vault_id"

SERVICENOW_ERR_API_INITIALIZATION = "API Initialization failed"
SERVICENOW_ERR_CONNECTIVITY_TEST = "Connectivity test failed"
SERVICENOW_SUCC_CONNECTIVITY_TEST = "Connectivity test passed"
SERVICENOW_ERR_CREATE_TICKET_FAILED = "Ticket creation failed"
SERVICENOW_SUCC_TICKET_CREATED = "Created ticket with key: {key}"
SERVICENOW_ERR_LIST_TICKETS_FAILED = "Failed to get ticket listing"
SERVICENOW_ERR_SERVER_CONNECTION = "Connection failed"
SERVICENOW_ERR_FROM_SERVER = "API failed, Status code: {status}, Message: {message}, Detail: {detail}"
SERVICENOW_MSG_GET_INCIDENT_TEST = "Querying a single Incident to check credentials"
SERVICENOW_ERR_FIELDS_JSON_PARSE = "Unable to parse the fields parameter into a dictionary"
SERVICENOW_ERR_API_UNSUPPORTED_METHOD = "Unsupported method"
SERVICENOW_ERR_EMPTY_FIELDS = "The fields dictionary was detected to be empty"
SERVICENOW_ERR_ONE_PARAM_REQ = "Please specify at least one of the parameters short_description, description, or fields to create the ticket with"

SERVICENOW_CREATED_TICKET = "Created ticket"
SERVICENOW_USING_BASE_URL = "Using url: {base_url}"
SERVICENOW_ERR_JSON_PARSE = "Unable to parse reply as a Json, raw string reply: '{raw_text}'"

DEFAULT_MAX_RESULTS = 100
SERVICENOW_TICKET_FOOTNOTE = "Added by Phantom for container id: "
SERVICENOW_DEFAULT_TABLE = "incident"

SERVICENOW_MAX_COUNT_VALUE = 4294967295
SERVICENOW_INGEST_LATEST_ITEMS = "latest first"
SERVICENOW_INGEST_OLDEST_ITEMS = "oldest first"
