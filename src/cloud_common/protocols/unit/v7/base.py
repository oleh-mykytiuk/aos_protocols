#
#  Copyright (c) 2018-2025 EPAM Systems Inc.
#
from typing import Annotated, Union

from pydantic import BaseModel, Discriminator, Field

from .alert import AosAlertsV7
from .envars import (
    AosOverrideEnvVarsRequestV7,
    AosOverrideEnvVarsStatusesV7,
)
from .state import (
    AosNewStateV7,
    AosStateAcceptanceV7,
    AosStateRequestV7,
    AosUpdateStateV7,
)
from .log import AosRequestLogV7, AosPushLogV7
from .monitoring import AosMonitoringV7
from .provisioning import (
    AosStartProvisioningRequestV7,
    AosStartProvisioningResponseV7,
    AosFinishProvisioningRequestV7,
    AosFinishProvisioningResponseV7,
    AosDeProvisioningRequestV7,
    AosDeProvisioningResponseV7,
)
from .unit_status import AosUnitStatusV7
from .desired_status import AosDesiredStatusV7
from .header import AosUnitHeaderV7
from .certificates import (
    AosRenewCertsNotificationV7,
    AosIssuedUnitCertificatesV7,
    AosIssueUnitCertificatesV7,
    AosInstallUnitCertificatesConfirmationV7,
)


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
            AosAlertsV7,
            AosMonitoringV7,
            AosUnitStatusV7,
            AosDesiredStatusV7,
            AosNewStateV7,
            AosStateRequestV7,
            AosStateAcceptanceV7,
            AosUpdateStateV7,
            AosRequestLogV7,
            AosPushLogV7,
            AosOverrideEnvVarsRequestV7,
            AosOverrideEnvVarsStatusesV7,
            AosRenewCertsNotificationV7,
            AosIssuedUnitCertificatesV7,
            AosIssueUnitCertificatesV7,
            AosInstallUnitCertificatesConfirmationV7,
            AosStartProvisioningRequestV7,
            AosStartProvisioningResponseV7,
            AosFinishProvisioningRequestV7,
            AosFinishProvisioningResponseV7,
            AosDeProvisioningRequestV7,
            AosDeProvisioningResponseV7,
        ],
        Field(
            description='message payload',
        ),
        Discriminator('message_type'),
    ]
