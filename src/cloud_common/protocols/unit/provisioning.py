#
#  Copyright (c) 2018-2024 Renesas Inc.
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#
from typing import Annotated, Literal

from pydantic import BaseModel, Field

from cloud_common.protocols.unit.common import TypeAosErrorInfoOptional
from cloud_common.protocols.unit.types import TypeNodeIdMandatory


class AosCSR(BaseModel):
    """Aos Certificate Sign Request."""

    csr_type: Annotated[
        str,
        Field(
            alias='type',
            description='Type of the CSR',
            examples=['online', 'offline'],
        )
    ]

    csr: Annotated[
        str,
        Field(
            alias='csr',
            description='CSR in the PEM format',
        ),
    ]


class AosStartProvisioningRequest(BaseModel):
    """
    AosUnit protocol: 'startProvisioningRequest' message.

    Cloud begins provisioning process with this message
    """

    message_type: Annotated[
        Literal['startProvisioningRequest'],
        Field(
            alias='messageType',
            description='message body type',
        ),
    ]

    node_id: TypeNodeIdMandatory

    password: Annotated[
        str,
        Field(
            alias='password',
            description='Admin (secure officer) password for the node TPM.',
        ),
    ]


class AosStartProvisioningResponse(BaseModel):
    """
    AosUnit protocol: 'startProvisioningResponse' message.
    """

    message_type: Annotated[
        Literal['startProvisioningResponse'],
        Field(
            alias='messageType',
            description='message body type',
        ),
    ]

    node_id: TypeNodeIdMandatory
    error_info: TypeAosErrorInfoOptional

    csrs: Annotated[
        list[AosCSR],
        Field(
            alias='csrs',
            description='List of the CSRs.',
        )
    ]


class AosFinishProvisioningRequest(BaseModel):
    """
    AosUnit protocol: 'finishProvisioningRequest' message.

    Cloud begins provisioning process with this message
    """

    message_type: Annotated[
        Literal['finishProvisioningRequest'],
        Field(
            alias='messageType',
            description='message body type',
        ),
    ]

    node_id: TypeNodeIdMandatory

    certificates: Annotated[
        list[str],
        Field(
            alias='certificates',
            description='The list of issued certificates',
        ),
    ]

    password: Annotated[
        str,
        Field(
            alias='password',
            description='Admin (secure officer) password for the node TPM.',
        ),
    ]


class AosFinishProvisioningResponse(BaseModel):
    """
    AosUnit protocol: 'finishProvisioningResponse' message.
    """

    message_type: Annotated[
        Literal['finishProvisioningResponse'],
        Field(
            alias='messageType',
            description='message body type',
        ),
    ]

    node_id: TypeNodeIdMandatory
    error_info: TypeAosErrorInfoOptional
