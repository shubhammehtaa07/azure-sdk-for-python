# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.core import PipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

from ._configuration import AzureFileStorageConfiguration
from .operations import ServiceOperations
from .operations import ShareOperations
from .operations import DirectoryOperations
from .operations import FileOperations
from . import models


class AzureFileStorage(object):
    """AzureFileStorage.

    :ivar service: ServiceOperations operations
    :vartype service: azure.storage.fileshare.operations.ServiceOperations
    :ivar share: ShareOperations operations
    :vartype share: azure.storage.fileshare.operations.ShareOperations
    :ivar directory: DirectoryOperations operations
    :vartype directory: azure.storage.fileshare.operations.DirectoryOperations
    :ivar file: FileOperations operations
    :vartype file: azure.storage.fileshare.operations.FileOperations
    :param url: The URL of the service account, share, directory or file that is the target of the desired operation.
    :type url: str
    """

    def __init__(
        self,
        url,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        base_url = '{url}'
        self._config = AzureFileStorageConfiguration(url, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.service = ServiceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.share = ShareOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.directory = DirectoryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.file = FileOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AzureFileStorage
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
