# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CertificateRestoreParameters(Model):
    """The certificate restore parameters.

    :param certificate_bundle_backup: The backup blob associated with a
     certificate bundle.
    :type certificate_bundle_backup: bytes
    """

    _validation = {
        'certificate_bundle_backup': {'required': True},
    }

    _attribute_map = {
        'certificate_bundle_backup': {'key': 'value', 'type': 'base64'},
    }

    def __init__(self, certificate_bundle_backup):
        super(CertificateRestoreParameters, self).__init__()
        self.certificate_bundle_backup = certificate_bundle_backup
