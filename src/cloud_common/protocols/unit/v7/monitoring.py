#
#  Copyright (c) 2018-2025 EPAM Systems Inc.
#
from datetime import datetime
from typing import Annotated, Literal, Union, Optional

from pydantic import BaseModel, Field

from .types import TypeUpdateItemInstanceState, TypeNodeState
from ..types import TypeInstanceNoMandatory, TypeNodeIdMandatory
from .common import AosIdentifier


class AosPartitionUsage(BaseModel):
    """PartitionUsage partition usage information."""

    name: Annotated[
        str,
        Field(
            alias='name',
            description='Name of disk partition',
        ),
    ]

    used_size: Annotated[
        int,
        Field(
            alias='usedSize',
            description='Used of disk partition in bytes',
        ),
    ]


class AosUpdateItemStateData(BaseModel):
    """Service instance state information."""

    timestamp: Annotated[
        datetime,
        Field(
            alias='timestamp',
            description='Timestamp when unit monitoring was recorded in ISO8601 format',
        ),
    ]

    state: TypeUpdateItemInstanceState


class AosMonitoringData(BaseModel):
    """AosEdge monitoring data."""

    timestamp: Annotated[
        datetime,
        Field(
            alias='timestamp',
            description='Timestamp when unit monitoring was recorded in ISO8601 format',
        ),
    ]

    ram: Annotated[
        int,
        Field(
            alias='ram',
            description='RAM Parameter of unit monitoring',
        ),
    ]

    cpu: Annotated[
        int,
        Field(
            alias='cpu',
            description='CPU Parameter of unit monitoring',
        ),
    ]

    download: Annotated[
        int,
        Field(
            default=None,
            alias='download',
            description='In Traffic Parameter of unit monitoring',
        ),
    ]

    upload: Annotated[
        int,
        Field(
            default=None,
            alias='upload',
            description='Out Traffic Parameter of unit monitoring',
        ),
    ]

    partitions: Annotated[
        list[AosPartitionUsage],
        Field(
            default=None,
            alias='partitions',
            description='Usage of disk partitions',
        ),
    ]


class AosInstanceMonitoringDataV7(BaseModel):
    """AosEdge unit monitoring data for service."""

    item_id: Annotated[
        AosIdentifier,
        Field(
            alias='itemId',
            description='The identification of the service.',
        ),
    ]

    subject_id: Annotated[
        AosIdentifier,
        Field(
            alias='subjectId',
            description='The identification of the service.',
        ),
    ]

    instance: TypeInstanceNoMandatory

    node_id: Annotated[
        AosIdentifier,
        Field(
            alias='nodeId',
            description='The identification of the node.',
        ),
    ]

    items: Annotated[  # noqa: WPS110
        list[AosMonitoringData],
        Field(
            alias='items',
            description='List of the monitoring records',
        ),
    ]


class AosNodeMonitoringDataV7(BaseModel):
    """AosEdge unit monitoring information."""

    node_id: Annotated[
        AosIdentifier,
        Field(
            alias='nodeId',
            description='The identification of the node.',
        ),
    ]

    items: Annotated[  # noqa: WPS110
        list[AosMonitoringData],
        Field(
            alias='items',
            description='List of the monitoring records.',
        ),
    ]


class AosNodeState(BaseModel):
    """AosEdge unit monitoring information."""

    node_id: TypeNodeIdMandatory

    timestamp: Annotated[
        datetime,
        Field(
            alias='timestamp',
            description='Timestamp when the node state change was recorded in ISO8601 format',
        ),
    ]

    provisioned: Annotated[
        bool,
        Field(
            alias='provisioned',
            description='Flag to indicate if the node is provisioned.',
        ),
    ]

    state: TypeNodeState


class AosMonitoringV7(BaseModel):

    message_type: Annotated[
        Literal['monitoringData'],
        Field(
            alias='messageType',
            description='message body type',
        ),
    ]

    nodes: Annotated[  # noqa: WPS110
        list[AosNodeMonitoringDataV7],
        Field(
            description='List of AosEdge unit monitoring items',
        ),
    ]

    node_states: Annotated[
        Optional[list[AosNodeState]],
        Field(
            default=None,
            alias='nodeStates',
            description='List of AosEdge unit monitoring got from node states.',
        ),
    ]

    item_states: Annotated[
        Optional[list[AosUpdateItemStateData]],
        Field(
            default=None,
            alias='itemStates',
            description='List of AosEdge update item state changes.',
        ),
    ]

    instances: Annotated[
        list[AosInstanceMonitoringDataV7],
        Field(
            default=None,
            alias='instances',
            description='List of AosEdge unit monitoring got from update items.',
        ),
    ]
