[comment]: # "Auto-generated SOAR connector documentation"
# Bitdefender GravityZone

Publisher: Splunk Community  
Connector Version: 1\.0\.1  
Product Vendor: Bitdefender  
Product Name: GravityZone  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 5\.1\.0  

This app integrates with Bitdefender GravityZone to execute various containment, corrective and investigative actions

[comment]: # "File: README.md"
[comment]: # "Copyright (c) 2022 Splunk Inc."
[comment]: # ""
[comment]: # "Licensed under the Apache License, Version 2.0 (the 'License');"
[comment]: # "you may not use this file except in compliance with the License."
[comment]: # "You may obtain a copy of the License at"
[comment]: # ""
[comment]: # "    http://www.apache.org/licenses/LICENSE-2.0"
[comment]: # ""
[comment]: # "Unless required by applicable law or agreed to in writing, software distributed under"
[comment]: # "the License is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,"
[comment]: # "either express or implied. See the License for the specific language governing permissions"
[comment]: # "and limitations under the License."
[comment]: # ""
## Authentication

The API calls to Bitdefender Control Center are authenticated at HTTP protocol level using HTTP
Basic Authentication.

## API Key

API Keys provide a way to authenticate with the Bitdefender GravityZone API and can be generated
from your Bitdefender Control Center. To support the available actions, please select
`     Quarantine API    ` when creating your API key.


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a GravityZone asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**base\_url** |  required  | string | URL \(e\.g\. https\://cloud\.gravityzone\.bitdefender\.com/api\)
**api\_key** |  required  | password | API Key
**verify\_server\_cert** |  optional  | boolean | Verify server certificate

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[delete quarantine](#action-delete-quarantine) - Delete items from quarantine  
[unquarantine computer](#action-unquarantine-computer) - Unquarantine Computers and Virtual Machines  
[unquarantine exchange](#action-unquarantine-exchange) - Unquarantine items for Exchange Servers  
[list quarantine](#action-list-quarantine) - Get list of available quarantined items related to a company  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'delete quarantine'
Delete items from quarantine

Type: **contain**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**service\_name** |  required  | Service name \(computers or exchange\) | string | 
**empty\_all** |  optional  | Check to remove all items from quarantine | boolean | 
**item\_ids** |  optional  | List of quarantined IDs to be removed \(comma separated\) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.service\_name | string | 
action\_result\.parameter\.empty\_all | boolean | 
action\_result\.parameter\.item\_ids | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.id | string | 
action\_result\.data\.\*\.result | boolean | 
action\_result\.summary | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'unquarantine computer'
Unquarantine Computers and Virtual Machines

Type: **correct**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**item\_ids** |  required  | List of quarantined IDs to be restored \(comma separated\) | string | 
**location** |  optional  | Absolute path to the folder where items will be restored | string | 
**add\_exclusion\_policy** |  optional  | Exclude files to be restored from future scans | boolean | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.item\_ids | string | 
action\_result\.parameter\.location | string | 
action\_result\.parameter\.add\_exclusion\_policy | boolean | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.id | string | 
action\_result\.data\.\*\.result | boolean | 
action\_result\.summary | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'unquarantine exchange'
Unquarantine items for Exchange Servers

Type: **correct**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**item\_ids** |  required  | List of quarantined IDs to be restored \(comma separated\) | string | 
**username** |  required  | Username of a MS Exchange user \(incl\. domain name\) | string | 
**password** |  required  | Password of a MS Exchange user | string | 
**email** |  optional  | Email address of the MS Exchange user | string |  `email` 
**ews\_url** |  optional  | MS Exchange Web Services URL | string |  `url` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.item\_ids | string | 
action\_result\.parameter\.username | string | 
action\_result\.parameter\.password | password | 
action\_result\.parameter\.email | string |  `email` 
action\_result\.parameter\.ews\_url | string |  `url` 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.id | string | 
action\_result\.data\.\*\.result | boolean | 
action\_result\.summary | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'list quarantine'
Get list of available quarantined items related to a company

Type: **generic**  
Read only: **False**

Services allowed are computers for 'Computers and VMs' and exchange for 'Security for Exchange'\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**service\_name** |  required  | Service name \(computers or exchange\) | string | 
**endpoint\_id** |  optional  | ID of device for which quarantined items are retrieved\. Empty to fetch all quarantined items in the network | string | 
**page** |  optional  | Results page | numeric | 
**per\_page** |  optional  | Number of items per page | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.service\_name | string | 
action\_result\.parameter\.endpoint\_id | string | 
action\_result\.parameter\.page | numeric | 
action\_result\.parameter\.per\_page | numeric | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.id | string | 
action\_result\.data\.\*\.quarantinedOn | string | 
action\_result\.data\.\*\.actionStatus | numeric | 
action\_result\.data\.\*\.endpointId | string | 
action\_result\.data\.\*\.endpointName | string | 
action\_result\.data\.\*\.endpointIP | string |  `ip` 
action\_result\.data\.\*\.canBeRestored | boolean | 
action\_result\.data\.\*\.canBeRemoved | boolean | 
action\_result\.data\.\*\.threatName | string | 
action\_result\.data\.\*\.companyId | string | 
action\_result\.summary\.num\_items | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 