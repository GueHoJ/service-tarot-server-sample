# Set log level to debug to get detailed logs
# log_level = "debug"

# Auto-auth configuration to handle AppRole authentication
auto_auth {
  method "approle" {
    mount_path = "auth/approle"
    config = {
      role_id_file_path = "/etc/vault-agent/role-id"        # Path to Role ID
      secret_id_file_path = "/etc/vault-agent/secret-id"    # Path to Secret ID
      remove_secret_id_file_after_reading = false           # Keep Secret ID after reading
    }
  }

  # Sink configuration to store the Vault token in a file
  sink "file" {
    config = {
      path = "/etc/vault-agent/token"                       # Path to store the token
    }
  }
}

# Template configuration to render a file with secrets from Vault
template {
  # source      = "/etc/vault-agent/templates/settings.tpl"   # Path to the template file
  source      = "/etc/vault-agent/templates/settings-rendered.tpl"   # Path to the template file
  destination = "/etc/vault-agent/django_rest_framework/project/config/settings_vault.py"     # Path to render the template output
}

vault {
  address = "http://${HOST_IP}:8200"                         # Address of the Vault server
}

# Enabling the agent to dynamically update secrets and keep running
# Ensure Vault Agent continues running to handle token renewal and dynamic updates
exit_after_auth = false
