from collections.abc import Mapping
from typing import Any
from unittest.mock import Mock

import pytest

from reconcile.external_resources.aws import AWSRdsFactory
from reconcile.external_resources.model import (
    ExternalResource,
    ExternalResourceModuleConfiguration,
    ExternalResourceProvision,
)
from reconcile.utils.external_resource_spec import (
    ExternalResourceSpec,
)


@pytest.fixture
def factory() -> AWSRdsFactory:
    return AWSRdsFactory(er_inventory=Mock(), secret_reader=Mock())


@pytest.mark.parametrize(
    ("reconcile_timeout_minutes", "timeouts", "expected_timeouts"),
    [
        (
            120,
            {"create": "60m", "update": "60m", "delete": "60m"},
            {"create": "60m", "update": "60m", "delete": "60m"},
        ),
        (120, None, {"create": "115m", "update": "115m", "delete": "115m"}),
    ],
)
def test_validate_timeouts_ok(
    reconcile_timeout_minutes: int,
    timeouts: Mapping[str, str],
    expected_timeouts: Mapping[str, str],
) -> None:
    spec = ExternalResourceSpec(
        provision_provider="aws",
        provisioner={"name": "test"},
        resource={"identifier": "test-rds", "provider": "rds", "timeouts": timeouts},
        namespace={},
    )
    module_conf = ExternalResourceModuleConfiguration(
        reconcile_timeout_minutes=reconcile_timeout_minutes
    )
    factory = AWSRdsFactory(er_inventory=Mock(), secret_reader=Mock())
    data = factory.resolve(spec, module_conf)
    resource = ExternalResource(
        data=data,
        provision=Mock(spec=ExternalResourceProvision),
    )

    factory.validate(resource, module_conf)
    assert resource.data["timeouts"] == expected_timeouts


@pytest.mark.parametrize(
    ("timeouts", "expected_value_error"),
    [
        (
            {"create": "60m", "update": "60m", "delete": "60m"},
            "RDS instance create timeout value 60 must be lower than the module reconcile_timeout_minutes value 60.",
        ),
        (
            {"create": "55m", "update": "60m", "delete": "60m"},
            "RDS instance update timeout value 60 must be lower than the module reconcile_timeout_minutes value 60.",
        ),
        (
            {"create": "1h", "update": "1h", "delete": "1h"},
            r"Invalid RDS instance timeout format: 1h. Specify timeout in minutes\(m\).",
        ),
        (
            {"unknown_key": "55m"},
            "Timeouts must be a dictionary with 'create', 'update' and/or 'delete' keys. Offending keys: {'unknown_key'}.",
        ),
        (
            "Not_A_Dictionary",
            "Timeouts must be a dictionary with 'create', 'update' and/or 'delete' keys.",
        ),
    ],
)
def test_validate_timeouts_nok(timeouts: Any, expected_value_error: str) -> None:
    factory = AWSRdsFactory(er_inventory=Mock(), secret_reader=Mock())
    resource = ExternalResource(
        data={"timeouts": timeouts}, provision=Mock(spec=ExternalResourceProvision)
    )

    module_conf = ExternalResourceModuleConfiguration(reconcile_timeout_minutes=60)
    with pytest.raises(
        ValueError,
        match=rf".*{expected_value_error}.*",
    ):
        factory.validate(resource, module_conf)
