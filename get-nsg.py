
import oci

# Configuration
ociConfDir="oci/config"
nsg = {
    "ocid":"ocid1.networksecuritygroup.oc1.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}

# init config
config = oci.config.from_file(ociConfDir, "DEFAULT")

oci.config.validate_config(config)

# init VCN service core
coreClient = oci.core.VirtualNetworkClient(config)

nsgRulesResponse = coreClient.list_network_security_group_security_rules(
    network_security_group_id=nsg["ocid"])

# Get the data from response
print(nsgRulesResponse.data)
