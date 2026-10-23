'''
    Update-NSG.py

    Updates the specified Network Security Group (NSG) entry within Oracle Cloud Infrastructure (OCI) with current networks public IP.
'''


from datetime import datetime
import requests
import oci

# Configuration
ociConfDir="oci/config"
ipaddr=""
ipsrcUri="https://myip.util.chlf.dev/"
nsg = {
    "ocid":"ocid1.networksecuritygroup.oc1.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "rule":{
        "id":"xxxxxx",
        "proto":"6",
        "description":"UPDATED BY SCRIPT: " + str(datetime.now()),
        "destPort":00000
    }
}

# get current ip
res = requests.get(ipsrcUri)
ipaddr = res.text

# init config
config = oci.config.from_file(ociConfDir, "DEFAULT")
oci.config.validate_config(config)

# init VCN service core
coreClient = oci.core.VirtualNetworkClient(config)

# send request
updateNSGResponse = coreClient.update_network_security_group_security_rules(
    network_security_group_id=nsg["ocid"],
    update_network_security_group_security_rules_details=oci.core.models.UpdateNetworkSecurityGroupSecurityRulesDetails(
        security_rules=[
            oci.core.models.UpdateSecurityRuleDetails(
                direction="INGRESS",
                id=nsg["rule"]["id"],
                protocol=nsg["rule"]["proto"],
                source=ipaddr + "/32",
                description=nsg["rule"]["description"],
                tcp_options=oci.core.models.TcpOptions(
                    destination_port_range=oci.core.models.PortRange(
                        max=nsg["rule"]["destPort"],
                        min=nsg["rule"]["destPort"]
                    )
                )
            )
        ]
    )
)