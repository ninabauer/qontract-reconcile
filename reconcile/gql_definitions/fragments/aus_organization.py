"""
Generated by qenerate plugin=pydantic_v1. DO NOT MODIFY MANUALLY!
"""
from collections.abc import Callable  # noqa: F401 # pylint: disable=W0611
from datetime import datetime  # noqa: F401 # pylint: disable=W0611
from enum import Enum  # noqa: F401 # pylint: disable=W0611
from typing import (  # noqa: F401 # pylint: disable=W0611
    Any,
    Optional,
    Union,
)

from pydantic import (  # noqa: F401 # pylint: disable=W0611
    BaseModel,
    Extra,
    Field,
    Json,
)

from reconcile.gql_definitions.fragments.upgrade_policy import ClusterUpgradePolicyV1
from reconcile.gql_definitions.fragments.disable import DisableAutomations
from reconcile.gql_definitions.fragments.minimal_ocm_organization import MinimalOCMOrganization
from reconcile.gql_definitions.fragments.ocm_environment import OCMEnvironment
from reconcile.gql_definitions.fragments.vault_secret import VaultSecret


class ConfiguredBaseModel(BaseModel):
    class Config:
        smart_union=True
        extra=Extra.forbid


class ClusterAddonV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")


class JenkinsInstanceV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    token: VaultSecret = Field(..., alias="token")


class AddonUpgradeTestV1(ConfiguredBaseModel):
    addon: ClusterAddonV1 = Field(..., alias="addon")
    instance: JenkinsInstanceV1 = Field(..., alias="instance")
    name: str = Field(..., alias="name")


class OpenShiftClusterManagerV1_OpenShiftClusterManagerV1_OpenShiftClusterManagerEnvironmentV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")


class OpenShiftClusterManagerV1_OpenShiftClusterManagerV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    org_id: str = Field(..., alias="orgId")
    environment: OpenShiftClusterManagerV1_OpenShiftClusterManagerV1_OpenShiftClusterManagerEnvironmentV1 = Field(..., alias="environment")
    publish_version_data: Optional[list[MinimalOCMOrganization]] = Field(..., alias="publishVersionData")


class OpenShiftClusterManagerSectorDependenciesV1_OpenShiftClusterManagerV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")


class OpenShiftClusterManagerSectorDependenciesV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    ocm: Optional[OpenShiftClusterManagerSectorDependenciesV1_OpenShiftClusterManagerV1] = Field(..., alias="ocm")


class OpenShiftClusterManagerSectorV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    dependencies: Optional[list[OpenShiftClusterManagerSectorDependenciesV1]] = Field(..., alias="dependencies")


class OpenShiftClusterManagerUpgradePolicyClusterV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    upgrade_policy: ClusterUpgradePolicyV1 = Field(..., alias="upgradePolicy")


class AusClusterHealthCheckV1(ConfiguredBaseModel):
    provider: str = Field(..., alias="provider")
    enforced: bool = Field(..., alias="enforced")


class AUSOCMOrganization(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    environment: OCMEnvironment = Field(..., alias="environment")
    org_id: str = Field(..., alias="orgId")
    access_token_client_id: Optional[str] = Field(..., alias="accessTokenClientId")
    access_token_url: Optional[str] = Field(..., alias="accessTokenUrl")
    access_token_client_secret: Optional[VaultSecret] = Field(..., alias="accessTokenClientSecret")
    disable: Optional[DisableAutomations] = Field(..., alias="disable")
    blocked_versions: Optional[list[str]] = Field(..., alias="blockedVersions")
    addon_managed_upgrades: Optional[bool] = Field(..., alias="addonManagedUpgrades")
    addon_upgrade_tests: Optional[list[AddonUpgradeTestV1]] = Field(..., alias="addonUpgradeTests")
    inherit_version_data: Optional[list[OpenShiftClusterManagerV1_OpenShiftClusterManagerV1]] = Field(..., alias="inheritVersionData")
    publish_version_data: Optional[list[MinimalOCMOrganization]] = Field(..., alias="publishVersionData")
    sectors: Optional[list[OpenShiftClusterManagerSectorV1]] = Field(..., alias="sectors")
    upgrade_policy_allowed_workloads: Optional[list[str]] = Field(..., alias="upgradePolicyAllowedWorkloads")
    upgrade_policy_clusters: Optional[list[OpenShiftClusterManagerUpgradePolicyClusterV1]] = Field(..., alias="upgradePolicyClusters")
    aus_cluster_health_checks: Optional[list[AusClusterHealthCheckV1]] = Field(..., alias="ausClusterHealthChecks")
