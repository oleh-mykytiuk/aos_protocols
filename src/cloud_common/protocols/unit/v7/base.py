#
#  Copyright (c) 2018-2024 Renesas Inc.
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#
from typing import Annotated, Union

from pydantic import BaseModel, Discriminator, Field

from .alert import AosAlerts
from cloud_common.protocols.unit.certificates import (
    AosInstallUnitCertificatesConfirmation,
    AosIssuedUnitCertificates,
    AosIssueUnitCertificates,
    AosRenewCertsNotification,
)
from cloud_common.protocols.unit.envars import (
    AosOverrideEnvVarsRequest,
    AosOverrideEnvVarsStatuses,
)
from cloud_common.protocols.unit.log import AosPushLog, AosRequestLog
from cloud_common.protocols.unit.monitoring import AosMonitoring
from cloud_common.protocols.unit.provisioning import (
    AosStartProvisioningRequest,
    AosStartProvisioningResponse,
    AosFinishProvisioningResponse,
    AosFinishProvisioningRequest,
    AosDeProvisioningResponse,
    AosDeProvisioningRequest,
)
from cloud_common.protocols.unit.state import (
    AosNewState,
    AosStateAcceptance,
    AosStateRequest,
    AosUpdateState,
)
from .unit_status import AosUnitStatusV7
from .desired_status import AosDesiredStatusV7
from .header import AosUnitHeaderV7


class AosUnitMessageV7(BaseModel):
    """Unit message model."""

    header: Annotated[
        AosUnitHeaderV7,
        Field(
            description='Aos Unit-Cloud message header',
        ),
    ]
    data: Annotated[  # noqa: WPS110
        Union[
            AosAlerts,
            # AosMonitoring,
            AosUnitStatusV7,
            AosDesiredStatusV7,
            # AosNewState,
            # AosStateRequest,
            # AosStateAcceptance,
            # AosUpdateState,
            # AosRequestLog,
            # AosPushLog,
            # AosOverrideEnvVarsRequest,
            # AosOverrideEnvVarsStatuses,
            # AosRenewCertsNotification,
            # AosRenewCertsNotification,
            # AosIssuedUnitCertificates,
            # AosIssueUnitCertificates,
            # AosInstallUnitCertificatesConfirmation,
            # AosStartProvisioningRequest,
            # AosStartProvisioningResponse,
            # AosFinishProvisioningRequest,
            # AosFinishProvisioningResponse,
            # AosDeProvisioningRequest,
            # AosDeProvisioningResponse,
        ],
        Field(
            description='message payload',
        ),
        Discriminator('message_type'),
    ]
