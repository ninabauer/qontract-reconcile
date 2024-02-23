from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture

from reconcile.utils.aws_api_typed.iam import AWSApiIam

if TYPE_CHECKING:
    from mypy_boto3_iam import IAMClient
else:
    IAMClient = object


@pytest.fixture
def iam_client(mocker: MockerFixture) -> IAMClient:
    return mocker.Mock()


@pytest.fixture
def aws_api_iam(iam_client: IAMClient) -> AWSApiIam:
    return AWSApiIam(client=iam_client)


def test_aws_api_typed_iam_create_access_key(
    aws_api_iam: AWSApiIam, iam_client: MagicMock
) -> None:
    iam_client.create_access_key.return_value = {
        "AccessKey": {
            "AccessKeyId": "access_key_id",
            "SecretAccessKey": "secret_access_key",
        }
    }
    access_key = aws_api_iam.create_access_key("user")
    assert access_key.access_key_id == "access_key_id"
    assert access_key.secret_access_key == "secret_access_key"


def test_aws_api_typed_iam_create_user(
    aws_api_iam: AWSApiIam, iam_client: MagicMock
) -> None:
    iam_client.create_user.return_value = {
        "User": {
            "UserName": "user_name",
            "UserId": "user_id",
            "Arn": "arn",
            "Path": "path",
        }
    }
    user = aws_api_iam.create_user("user_name")
    assert user.user_name == "user_name"
    assert user.user_id == "user_id"
    assert user.arn == "arn"
    assert user.path == "path"


def test_aws_api_typed_iam_attach_user_policy(
    aws_api_iam: AWSApiIam, iam_client: MagicMock
) -> None:
    aws_api_iam.attach_user_policy("user_name", "policy_arn")
    iam_client.attach_user_policy.assert_called_once_with(
        UserName="user_name",
        PolicyArn="policy_arn",
    )


def test_aws_api_typed_iam_create_account_alias(
    aws_api_iam: AWSApiIam, iam_client: MagicMock
) -> None:
    aws_api_iam.create_account_alias("account_alias")
    iam_client.create_account_alias.assert_called_once_with(
        AccountAlias="account_alias",
    )
