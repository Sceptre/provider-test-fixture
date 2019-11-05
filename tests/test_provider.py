from provider.provider_fixture import CONNECTION_MANAGER


class TestStackActions:
    def test_connection_manager_call_returns_string(self):
        assert CONNECTION_MANAGER.call() == "called provider_test_fixture"
