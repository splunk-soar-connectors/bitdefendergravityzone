# Copyright (c) 2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import json
from pathlib import Path


ROOT = Path(__file__).parent


def test_manifest_enables_certificate_verification_by_default():
    manifest = json.loads((ROOT / "bitdefendergravityzone.json").read_text())

    assert manifest["configuration"]["verify_server_cert"]["default"] is True


def test_connector_uses_secure_certificate_verification_fallback():
    source = (ROOT / "bitdefendergravityzone_connector.py").read_text()

    assert 'config.get("verify_server_cert", True)' in source
    assert 'config.get("verify_server_cert", False)' not in source
