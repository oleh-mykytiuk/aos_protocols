#
#  Copyright (c) 2018-2024 Renesas Inc.
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#
from datetime import datetime
from typing import Annotated, Literal, Optional, Dict, Any

from pydantic import BaseModel, Field


class AosDependency(BaseModel):
    """Dependency for a component."""

    component_type: Annotated[
        str,
        Field(
            alias="type",
            description="The type (unique identifier) of the component.",
        ),
    ]

    required_version: Annotated[
        Optional[str],
        Field(
            alias='requiredVersion',
            default=None,
            description='The exact required version of the component.',
        ),
    ]

    min_version: Annotated[
        Optional[str],
        Field(
            alias='minVersion',
            default=None,
            description='The minimum required version of the component.',
        ),
    ]


class AosComponent(BaseModel):
    """
    AosEdge Component schema description.

    Contains description and dependencies information.
    """

    component_type: Annotated[
        str,
        Field(
            alias='type',
            description="""\
Unique for the AosEdge unit model component identifier.
Note that components are shared between different unit models."""
        ),
    ]

    file_name: Annotated[
        str,
        Field(
            alias='fileName',
            description='Path to the component file inside bundle.',
        ),
    ]

    version: Annotated[
        str,
        Field(
            alias='version',
            description='Component version in SemVer format.',
        ),
    ]

    description: Annotated[
        Optional[str],
        Field(
            alias='description',
            default=None,
            description='Component update description, for information purpose..',
        ),
    ]

    required_version: Annotated[
        Optional[str],
        Field(
            alias='requiredVersion',
            default=None,
            description="""\
Indicates the exact version of the component on which this version should be applied
   (explicitly means that update incremental) (requiredVersion discards minVersion and maxVersion).
Format - SemVer.""",
        ),
    ]

    min_version: Annotated[
        Optional[str],
        Field(
            alias='minVersion',
            default=None,
            description="""\
Indicates minimum version which should the component have before installing this one. Format - SemVer.""",
        ),
    ]

    max_version: Annotated[
        Optional[str],
        Field(
            alias='maxVersion',
            default=None,
            description="""\
Indicates maximum version which should the component have before installing this one. Format - SemVer.""",
        ),
    ]

    download_ttl: Annotated[
        Optional[datetime],
        Field(
            alias='downloadTTL',
            default=None,
            description="""\
Download TTL (ISO 8601 duration).
In case of the unit is not able to download service or related layer more than TTL time - Service should be deleted.""",
        ),
    ]

    annotations: Annotated[
        Optional[Dict[str, Any]],
        Field(
            alias='annotations',
            default=None,
            description="""\
Any valid JSON structure, it will be passed directly to the target,
  used to provide component-specific data required for update on the target.""",
            examples=[{'type': 'full'}]
        ),
    ]

    runtime_dependencies: Annotated[
        Optional[list[AosDependency]],
        Field(
            alias='runtimeDependencies',
            default=None,
            description="""\
List of components and their versions which should be installed at same time with required component""",
            examples=[[{'id': 'boot', 'requiredVersion': '1.0.0'}, {'id': 'bios', 'minVersion': '1.2.0'}]],
        ),
    ]


class AosUpdateSchema(BaseModel):
    """SOTA/FOTA manifest format."""

    format_version: Annotated[
        Literal[2],
        Field(
            alias='formatVersion',
            description='Format version,  used to support future extension and backward compatibility.'
        ),
    ]

    components: Annotated[
        list[AosComponent],
        Field(
            alias='components',
            description='Array of component images this bundle contains.',
            examples=[
                {
                    'type': 'rootfs',
                    'fileName': 'component.gz',
                    'version': '2.1.0',
                    'description': 'this is rootfs update',
                    'requiredVersion': '2.0.0',
                    'downloadTTL': 'P1M',
                    'annotations': {'type': 'incremental'},
                    'runtimeDependencies': [
                        {'type': 'boot', 'requiredVersion': '1.0.0'},
                        {'type': 'bios', 'minVersion': '1.2.0'},
                    ],
                },
                {
                    'type': 'rootfs',
                    'fileName': 'component.gz',
                    'version': '2.0.0',
                    'description': 'this is rootfs update',
                    'minVersion': '1.0.0',
                    'maxVersion': '2.0.0b99',
                    'downloadTTL': 'P1M',
                    'annotations': {'type': 'full'},
                }
            ]
        ),
    ]
