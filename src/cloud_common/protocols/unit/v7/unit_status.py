#
#  Copyright (c) 2018-2025 EPAM Systems Inc.
#
from typing import Annotated, Dict, Literal, Optional, List

from pydantic import BaseModel, Field

from .common import AosIdentifier, AosResourceInfo
from ..common import TypeAosErrorInfoOptional
from .types import (
    TypeInstanceNoMandatory,
    TypeNodeStatus,
    TypeServiceInstanceStatus,
    TypeServiceStatus,
    TypeStateChecksumOptional,
    TypeVersionMandatory,
    TypeVersionOptional,
)


class AosUnitConfigStatus(BaseModel):
    version: TypeVersionOptional
    status: Annotated[
        Literal[
            'absent',
            'installed',
            'failed',
        ],
        Field(
            description='current status of the item',
        ),
    ]
    error_info: TypeAosErrorInfoOptional


class AosNodePartitionInfo(BaseModel):
    """Aos node partition info."""

    name: Annotated[
        str,
        Field(
            title='Name',
            alias='name',
        ),
    ]

    types: Annotated[
        list[str],
        Field(
            title='List of types',
            alias='types',
        ),
    ]

    total_size: Annotated[
        int,
        Field(
            title='Total size',
            alias='totalSize',
        ),
    ]


class AosArchInfo(BaseModel):

    architecture: Annotated[
        str,
        Field(
            alias='architecture',
            description='The architecture of the CPU. Refer to the "https://github.com/opencontainers/image-spec/blob/main/config.md#properties"',
            examples=['amd64', 'arm64', 'arm'],
        ),
    ]

    variant: Annotated[
        Optional[str],
        Field(
            default=None,
            alias='variant',
            description='The variant of the specified CPU architecture. Refer to the "https://github.com/opencontainers/image-spec/blob/main/config.md#properties"'
        ),
    ]


class AosNodeCPUInfo(BaseModel):

    cpu_model_name: Annotated[
        str,
        Field(
            default=None,
            alias='modelName',
        ),
    ]

    total_num_cores: Annotated[
        int,
        Field(
            default=None,
            alias='totalNumCores',
        ),
    ]

    total_num_threads: Annotated[
        int,
        Field(
            default=None,
            alias='totalNumThreads',
        ),
    ]
    arch_info: Annotated[
        AosArchInfo,
        Field(
            alias='archInfo',
        ),
    ]

    max_dmips: Annotated[
        Optional[int],
        Field(
            alias='maxDmips',
        ),
    ] = None


class AosOsInfo(BaseModel):

    os: Annotated[
        str,
        Field(
            alias='os',
            examples=['linux'],
        ),
    ]

    version: Annotated[
        Optional[str],
        Field(
            default=None,
            alias='version',
            description='The version of the OS.',
            examples=['6.8.0'],
        )
    ] = None

    features: Annotated[
        Optional[List[str]],
        Field(
            default=None,
            alias='features',
            description='This OPTIONAL property specifies an array of strings, each specifying a mandatory OS feature.',
        ),
    ] = None


class AosRuntimeInfo(BaseModel):

    identifier: Annotated[
        AosIdentifier,
        Field(
            alias='identifier',
        ),
    ]

    arch_info: Annotated[
        AosArchInfo,
        Field(
            alias='archInfo',
        ),
    ]

    os_info: Annotated[
        AosOsInfo,
        Field(
            alias='osInfo',
        ),
    ]

    max_dmips: Annotated[
        int,
        Field(
            alias='maxDmips',
        ),
    ]

    total_ram: Annotated[
        Optional[int],
        Field(
            alias='totalRam',
            description='The total RAM in bytes. Optional for AosComponents runtimes.',
        ),
    ]

    max_instances: Annotated[
        int,
        Field(
            alias='maxInstances',
            ge=0,
            description='The maximum number of instances. 0 for unlimited.',
        ),
    ]


class AosUnitNodeInfo(BaseModel):

    identifier: Annotated[
        AosIdentifier,
        Field(
            description='Identifier of the node.',
            examples=[{"codename": "node-1398431", "title": "DomD"}],
        )
    ]

    node_group_subject: Annotated[
        AosIdentifier,
        Field(
            alias='nodeGroupSubject',
            description='Subject of the node group. Previously known as NodeType.',
            examples=[{"codename": "main-node"}],
        ),
    ]

    max_dmips: Annotated[
        int,
        Field(
            alias='maxDmips',
        ),
    ]

    os_info: Annotated[
        AosOsInfo,
        Field(
            alias='osInfo',
        ),
    ]

    cpus: Annotated[
        Optional[list[AosNodeCPUInfo]],
        Field(
            default=None,
            alias='cpus',
        ),
    ] = None

    attrs: Annotated[
        Optional[Dict[str, str]],
        Field(
            default=None,
            alias='attrs',
            examples=[{'dynamic'}, {'static': '', 'cloud_connection': '', 'name1': 'value1'}],
        ),
    ] = None

    total_ram: Annotated[
        int,
        Field(
            alias='totalRam',
            description='Total node RAM in bytes.',
            ge=1,
        ),
    ]

    partitions: Annotated[
        list[AosNodePartitionInfo],
        Field(
            alias='partitions',
            default=None,
            description='List of partitions',
        ),
    ]

    runtimes: Annotated[
        Optional[List[AosRuntimeInfo]],
        Field(
            default=None,
            alias='runtimes',
            description='List of supported runtimes.',
        ),
    ]

    resources: Annotated[
        Optional[List[AosResourceInfo]],
        Field(
            default=None,
            description='List of available resources.',
        ),
    ]

    status: TypeNodeStatus
    error_info: TypeAosErrorInfoOptional


class AosInstanceInfo(BaseModel):

    node: Annotated[
        AosIdentifier,
        Field(
            alias='node',
        ),
    ]

    instance: TypeInstanceNoMandatory
    state_checksum: TypeStateChecksumOptional
    status: TypeServiceInstanceStatus
    error_info: TypeAosErrorInfoOptional


class AosInstancesInfo(BaseModel):
    """Update item info sent to the AosEdge Cloud."""

    identifier: Annotated[
        AosIdentifier,
        Field(
            alias='identifier',
        )
    ]

    subject: Annotated[
        AosIdentifier,
        Field(
            alias='subject',
            description='Subject for the update item. Layers have no subject.',
        ),
    ]

    version: TypeVersionMandatory

    instances: Annotated[
        List[AosInstanceInfo],
        Field(
            alias='instances',
        ),
    ]


class AosUpdateItemInfo(BaseModel):
    """Update item info sent to the AosEdge Cloud."""

    identifier: Annotated[
        AosIdentifier,
        Field(
            alias='identifier',
        )
    ]

    version: TypeVersionMandatory

    status: TypeServiceStatus
    error_info: TypeAosErrorInfoOptional


class AosUnitStatusV7(BaseModel):
    """
    AosUnit protocol: 'unitStatus' message.

    Unit reports all current status information using this message
    """

    message_type: Annotated[
        Literal['unitStatus'],
        Field(
            alias='messageType',
            description='message body type',
        ),
    ]

    is_delta_info: Annotated[
        Optional[bool],
        Field(
            default=None,
            alias='isDeltaInfo',
            title='Delta info?',
            description='Flag to indicate if this is a full info message or delta from previous times',
            examples=[True, False],
        ),
    ]

    unit_config: Annotated[
        list[AosUnitConfigStatus],
        Field(
            default=None,
            alias='unitConfig',
            description='Information about the installed unitConfig.',
        ),
    ]

    nodes: Annotated[
        list[AosUnitNodeInfo],
        Field(
            default=None,
            alias='nodes',
            description='The list of attached to the Unit nodes.',
        ),
    ]

    update_items: Annotated[
        list[AosUpdateItemInfo],
        Field(
            default=None,
            alias='updateItems',
            description='List of the Aos update items.',
        ),
    ]

    instances: Annotated[
        list[AosInstancesInfo],
        Field(
            default=None,
            alias='instances',
        ),
    ]

    unit_subjects: Annotated[
        list[str],
        Field(
            default=None,
            alias='unitSubjects',
        ),
    ]
