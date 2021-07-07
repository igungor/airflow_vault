from typing import Optional
from airflow.providers.hashicorp.secrets.vault import VaultBackend


class PeakVaultBackend(VaultBackend):
    def get_variable(self, key: str) -> Optional[str]:
        if self.variables_path is None:
            return None

        secret_path = self.build_path(self.variables_path, key)
        return self.vault_client.get_secret(secret_path=secret_path)
