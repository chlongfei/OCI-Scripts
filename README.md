## Configuration
To utilize the OCI API, `.oci/config` is required, this can be obtained from the OCI console by generating an API key under `Identity & Security > Domains > {domain name} > {username} > API Keys`.

Sample:
```
[DEFAULT]
user=ocid1.user.oc1..xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
fingerprint=xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx
tenancy=ocid1.tenancy.oc1..xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
region=xx-xxxxxxxxx-1
key_file=oci/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.pem
```

## `update-nsg.py`
Updates the source IP of the specified Network Security Group (NSG) with current network public IP.

The Public IP is resolved via a lookup service, this can be defined within the script.

Make copies of the script for each NSG and NSG rule to be automatically updated.

Use a CRON job to automate/schedule.

## `get-nsg.py`
Dumps all the NSG rules of the specified NSG.

Useful for pulling the NSG Rule ID required for `update-nsg.py`.