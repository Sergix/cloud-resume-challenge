import json

import pytest

from visitor_count import app


@pytest.fixture()
def apigw_get_event():
    """ Generates API GW Get Event"""

    return {
        "resource": "/visitor-count",
        "path": "/visitor-count",
        "httpMethod": "GET",
        "isBase64Encoded": "false",
        "queryStringParameters": {
            "action": "get"
        }
    }


def test_lambda_handler_get(apigw_get_event):
    ret = app.lambda_handler(apigw_get_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert data == 0


@pytest.fixture()
def apigw_increment_event():
    """ Generates API GW Increment Event"""

    return {
        "resource": "/visitor-count",
        "path": "/visitor-count",
        "httpMethod": "GET",
        "isBase64Encoded": "false",
        "queryStringParameters": {
            "action": "increment"
        }
    }


def test_lambda_handler_get(apigw_increment_event):
    ret = app.lambda_handler(apigw_increment_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert data == 1
