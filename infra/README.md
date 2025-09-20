# Digital Wholesale Infra (IaC)

Infrastructure for Digital Wholesale application which utilizes Terraform and Azure CLI to build and manage infra easy, robust and automatic. 

## Getting started 
1. Ensure you have Azure account and subscription. If not, have one. Then continue. Otherwise, you can not set this up in your own machine. 

2. (Optional) Install Azure CLI and Terraform on your machine. Please check more [here](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)

3. (Optional) Update Azure CLI 
```bash
az upgrade
```

4. (Optional) If not sign in, sign in Azure with Azure CLI
```bash
az login
```


## Start to use
### Step 1: Authenticate to our Azure subscription 
Before run any terraform commands, you need to set ARM_SUBSCRIPTION_ID env variable to current subscription. Otherwise won't work. This command is used to be able to authenticate to your Azure subscription.
```bash
export ARM_SUBSCRIPTION_ID=$(az account show --query "id" --output tsv)
```

### Step 2: Initialize Terraform 
```bash
terraform init 
```

### Step 3: Create Terraform plan and export plan's file 
```bash 
terraform plan -out <plan_file_name> 
```
### Step 4: Check the plan before apply 
```bash 
terraform show <plan_file_name>
```

### Step 5: Apply Terraform plan 
```bash 
terraform apply <plan_file_name>
```

### Step 7: Create Terraform plan 
```bash 
terraform plan -destroy -out <destroy_plan_file_name>
```

### Step 7: Apply Terraform destroy plan 
```bash 
terraform apply <destroy_plan_file_name>
```

### Optional steps: 
#### Format the Terraform files
```bash
terraform fmt
```

#### Validate Terraform configuration files that deployable  
```bash 
terraform validate
```

#### List all Terraform states 
```bash
terraform state list 
```