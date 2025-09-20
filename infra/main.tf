# To deploy Azure function app, we need 4 resources:
# Resource Group
# Storage Account
# App Service Plan
# Azure Function App

##### 1. Resources #####
# Create a resource group
resource "azurerm_resource_group" "rg_digital_wholesale" {
  location = var.resource_group_location
  name     = var.resource_group_name
}

##### 2. Storage #####
# Create a storage account
resource "azurerm_storage_account" "sa_digital_wholesale" {
  name                     = var.sa_name
  resource_group_name      = azurerm_resource_group.rg_digital_wholesale.name
  location                 = azurerm_resource_group.rg_digital_wholesale.location
  account_tier             = var.sa_account_tier
  account_replication_type = var.sa_account_replication_type
}

# (Optional) Create a storage container
resource "azurerm_storage_container" "sc_digital_wholesale" {
  name                  = var.sc_name
  storage_account_id    = azurerm_storage_account.sa_digital_wholesale.id
  container_access_type = "private"
}

# (Optional) Create a Log Analytics workspace for Application Insights
resource "azurerm_log_analytics_workspace" "law_digital_wholesale" {
  name                = var.ws_name
  location            = azurerm_resource_group.rg_digital_wholesale.location
  resource_group_name = azurerm_resource_group.rg_digital_wholesale.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}

# (Optional) Create an Application Insights instance for monitoring
resource "azurerm_application_insights" "ai_digital_wholesale" {
  name                = var.ai_name
  location            = azurerm_resource_group.rg_digital_wholesale.location
  resource_group_name = azurerm_resource_group.rg_digital_wholesale.name
  application_type    = "web"
  workspace_id        = azurerm_log_analytics_workspace.law_digital_wholesale.id
}

##### 3. Service #####
# Create a service plan
resource "azurerm_service_plan" "sp_digital_wholesale" {
  name                = var.sp_name
  resource_group_name = azurerm_resource_group.rg_digital_wholesale.name
  location            = azurerm_resource_group.rg_digital_wholesale.location
  sku_name            = "FC1"
  os_type             = "Linux"
}

##### 4. Function App #####
# Create a function app
resource "azurerm_function_app_flex_consumption" "fa_digital_wholesale" {
  name                = var.fa_name
  resource_group_name = azurerm_resource_group.rg_digital_wholesale.name
  location            = azurerm_resource_group.rg_digital_wholesale.location
  service_plan_id     = azurerm_service_plan.sp_digital_wholesale.id

  storage_container_type      = "blobContainer"
  storage_container_endpoint  = "${azurerm_storage_account.sa_digital_wholesale.primary_blob_endpoint}${azurerm_storage_container.sc_digital_wholesale.name}"
  storage_authentication_type = "StorageAccountConnectionString"
  storage_access_key          = azurerm_storage_account.sa_digital_wholesale.primary_access_key
  runtime_name                = var.runtime_name
  runtime_version             = var.runtime_version
  maximum_instance_count      = 50
  instance_memory_in_mb       = 2048

  site_config {}
}