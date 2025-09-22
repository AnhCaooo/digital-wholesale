# Output the Static Web App deployment token (sensitive)
output "deployment_token" {
  description = "The deployment token for GitHub Actions/ command line deployment"
  value       = azurerm_static_web_app.swa_digital_wholesale.api_key
  sensitive   = true
} 