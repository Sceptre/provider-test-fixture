from sceptre.provider import Provider
from sceptre.provider.schema import Schema
from sceptre.provider.connection_manager import ConnectionManager


class ProviderTestCm(ConnectionManager):
    def call(self):
        return "called provider_test_fixture"


schema_obj = {
    "stack": {
        "type": "object",
        "properties": {
            "name": {"type": "string"}
        }
    }
}

SCHEMA = Schema(schema_obj)
cm_config = {"profile": "production"}
CONNECTION_MANAGER = ProviderTestCm(cm_config)


class ProviderTest(Provider, registry_key='provider_test_fixture'):
    def __init__(self):
        super().__init__('provider_test_fixture', SCHEMA, CONNECTION_MANAGER)
