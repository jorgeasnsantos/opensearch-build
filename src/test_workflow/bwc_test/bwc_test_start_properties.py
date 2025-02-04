# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.


import abc

from manifests.build_manifest import BuildManifest
from manifests.bundle_manifest import BundleManifest


class BwcTestStartProperties(abc.ABC):
    def __init__(self, path, build_dir, bundle_dir):
        self.path = path
        self.build_dir = build_dir
        self.bundle_dir = bundle_dir

        self.bundle_manifest = BundleManifest.from_urlpath("/".join([self.path.rstrip("/"), self.bundle_dir]))
        self.build_manifest = BuildManifest.from_urlpath("/".join([self.path.rstrip("/"), self.build_dir]))
