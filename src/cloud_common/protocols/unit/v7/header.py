#
#  Copyright (c) 2018-2025 EPAM Systems Inc.
#
from datetime import datetime
from typing import Annotated, Literal, Optional

from pydantic import BaseModel, Field

from cloud_common.protocols.unit.types import TypeAosSystemIdMandatory


class AosUnitHeaderV7(BaseModel):
    """Aos Unit message header."""

    version: Annotated[
        Literal[7],
        Field(
            title='Protocol version',
            description='The version of Unit-Cloud protocol.',
        ),
    ]
    system_id: TypeAosSystemIdMandatory

    created_at: Annotated[
        datetime,
        Field(
            alias='createdAt',
            description='The time when the message was created.',
        ),
    ]

    txn: Annotated[
        Optional[str],
        Field(
            alias='txn',
            default=None,
            description='Correlation ID of the request.',
        )
    ] = None

