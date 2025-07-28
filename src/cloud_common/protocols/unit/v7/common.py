#
#  Copyright (c) 2018-2024 Renesas Inc.
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#
from typing import Annotated, Optional, Literal

from pydantic import BaseModel, Field, UUID4

from ..common import (
    AosErrorInfo,
    AosHostRecord,
)


class AosIdentifier(BaseModel):
    """Aos objects identifier."""

    id:  Annotated[
        Optional[UUID4],
        Field(
            default=None,
            alias='id',
            title='Aos object UUID identifier. Unique per Aos instance.',
            description='Aos object unique per Aos instance UUID.',
        ),
    ] = None

    type: Annotated[
        Optional[Literal[
            'aosComponent',
            'aosService',
            'aosLayer',
            'aosSubject',
            'aosOEM',
        ]],
        Field(
            default=None,
            alias='type',
            title='Aos object type.',
            description='Aos object type. E.g.: AosService, AosComponent',
        ),
    ] = None

    codename: Annotated[
        Optional[str],
        Field(
            default=None,
            title='Aos object codename.',
            description='Aos object codename. Uniqueness depends on object type.',
        ),
    ] = None

    title: Annotated[
        Optional[str],
        Field(
            default=None,
            title='Aos object title.',
            description='Aos object title.',
        ),
    ] = None

    description: Annotated[
        Optional[str],
        Field(
            default=None,
            title='Aos object description.',
            description='Aos object description.',
        ),
    ] = None

    urn: Annotated[
        Optional[str],
        Field(
            default=None,
            alias='urn',
            title='Aos object URN.',
            description='Aos object URN. Globally unique.',
        ),
    ] = None


class AosResourceInfo(BaseModel):

    name: Annotated[
        str,
        Field(
            alias='name',
            description='The name of the resource.',
            examples=['camera0', 'shared_folder_1', 'dbus'],
        ),
    ]

    shared_count: Annotated[
        int,
        Field(
            alias='sharedCount',
            ge=0,
            description='The number of maximum shared usages. 0 mean unlimited',
        ),
    ]


TypeAosIdentifierMandatory = Annotated[
    AosIdentifier,
    Field(
        alias='identifier',
        description='The identification of the resource.',
    ),
]


TypeAosIdentifierOptional = Annotated[
    Optional[AosIdentifier],
    Field(
        default=None,
        alias='identifier',
        description='The identification of the resource.',
    ),
]


__all__ = (
    'AosIdentifier',
    'AosErrorInfo',
    'AosHostRecord',
    'AosResourceInfo',
    'TypeAosIdentifierMandatory',
    'TypeAosIdentifierOptional',
)
