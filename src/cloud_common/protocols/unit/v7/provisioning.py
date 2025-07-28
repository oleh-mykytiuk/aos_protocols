#
#  Copyright (c) 2018-2025 EPAM Systems Inc.
#
from typing import Annotated, Literal

from pydantic import BaseModel, Field

from cloud_common.protocols.unit.certificates import AosIssuedUnitCerts
from cloud_common.protocols.unit.common import TypeAosErrorInfoOptional
from cloud_common.protocols.unit.types import TypeNodeIdMandatory
from cloud_common.protocols.unit.v7.common import AosIdentifier


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


class AosStartProvisioningRequestV7(BaseModel):
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

    node_id: Annotated[
        AosIdentifier,
        Field(
            alias='nodeId',
            description='The identification of the naode.',
        ),
    ]

    password: Annotated[
        str,
        Field(
            alias='password',
            description='Admin (secure officer) password for the node TPM.',
        ),
    ]


class AosStartProvisioningResponseV7(BaseModel):
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

    node_id: Annotated[
        AosIdentifier,
        Field(
            alias='nodeId',
            description='The identification of the naode.',
        ),
    ]

    error_info: TypeAosErrorInfoOptional

    csrs: Annotated[
        list[AosCSR],
        Field(
            alias='csrs',
            description='List of the CSRs.',
        )
    ]


class AosFinishProvisioningRequestV7(BaseModel):
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

    node_id: Annotated[
        AosIdentifier,
        Field(
            alias='nodeId',
            description='The identification of the naode.',
        ),
    ]

    certificates: Annotated[
        list[AosIssuedUnitCerts],
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


class AosFinishProvisioningResponseV7(BaseModel):
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

    node_id: Annotated[
        AosIdentifier,
        Field(
            alias='nodeId',
            description='The identification of the naode.',
        ),
    ]

    error_info: TypeAosErrorInfoOptional


class AosDeProvisioningRequestV7(BaseModel):
    """
    AosUnit protocol: 'deprovisioningRequest' message.
    """

    message_type: Annotated[
        Literal['deprovisioningRequest'],
        Field(
            alias='messageType',
            description='message body type',
        ),
    ]

    node_id: Annotated[
        AosIdentifier,
        Field(
            alias='nodeId',
            description='The identification of the naode.',
        ),
    ]

    password: Annotated[
        str,
        Field(
            alias='password',
            description='Admin (secure officer) password for the node TPM.',
        ),
    ]


class AosDeProvisioningResponseV7(BaseModel):
    """
    AosUnit protocol: 'deprovisioningResponse' message.
    """

    message_type: Annotated[
        Literal['deprovisioningResponse'],
        Field(
            alias='messageType',
            description='message body type',
        ),
    ]

    node_id: Annotated[
        AosIdentifier,
        Field(
            alias='nodeId',
            description='The identification of the naode.',
        ),
    ]

    error_info: TypeAosErrorInfoOptional
