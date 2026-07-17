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
