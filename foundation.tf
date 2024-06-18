# Define the Azure provider
provider "azurerm" {
    features {}
}

# Create a resource group
resource "azurerm_resource_group" "aks_rg" {
    name     = "my-aks-resource-group"
    location = "West Europe"
}

# Create an AKS cluster
resource "azurerm_kubernetes_cluster" "aks_cluster" {
    name                = "my-aks-cluster"
    location            = azurerm_resource_group.aks_rg.location
    resource_group_name = azurerm_resource_group.aks_rg.name
    dns_prefix          = "myakscluster"

    default_node_pool {
        name       = "default"
        node_count = 1
        vm_size    = "Standard_DS2_v2"
    }
}

# Deploy microservices to AKS
data "local_file" "microservices" {
    filename = "${path.module}/src/microservices.yaml"
}

resource "null_resource" "deploy_microservices" {
    provisioner "local-exec" {
        command = "kubectl apply -f ${data.local_file.microservices.filename}"
    }

    depends_on = [azurerm_kubernetes_cluster.aks_cluster]
}