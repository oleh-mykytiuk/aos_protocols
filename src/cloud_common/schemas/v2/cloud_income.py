#
#  Copyright (c) 2018-2025 EPAM Systems Inc.
#
from typing import Annotated, Literal, Optional

from pydantic import BaseModel, Field

from .aos_types import AosUpdateItem


class AosPublisher(BaseModel):

    author: Annotated[
        Optional[str],
        Field(
            default=None,
            description='Author of the package.',
        ),
    ] = None

    company: Annotated[
        Optional[str],
        Field(
            default=None,
            description='Company that created the package.',
        ),
    ] = None


class AosPublish(BaseModel):

    tls_key: Annotated[
        str,
        Field(
            alias='tlsKey',
            description='Certificate and private key for the TLS connection.',
        ),
    ]

    sign_key: Annotated[
        Optional[str],
        Field(
            default=None,
            alias='signKey',
            description='Signing key for the package. If not provided, the package will be signed with the TLS key.',
        ),
    ] = None

    domain: Annotated[
        Optional[str],
        Field(
            default=None,
            description='Domain to upload the package. If not provided, domain will be extracted from the certificate.',
        ),
    ] = None


class AosUploadMetaConfig(BaseModel):

    schema_version: Annotated[
        Literal[2],
        Field(
            default=2,
            alias='schemaVersion',
            description='Schema version of the metadata configuration.',
        ),
    ] = 2

    publisher: Annotated[
        Optional[AosPublisher],
        Field(
            default=None,
            description='Publisher information about the package.',
        ),
    ]

    publish: Annotated[
        Optional[AosPublish],
        Field(
            default=None,
            description='Publish information about the package.',
        ),
    ] = None

    items: Annotated[
        list[AosUpdateItem],
        Field(
            description='List of the update items to upload.',
        ),
    ]

