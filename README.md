# Satellite-tune
Satellite-tune contains simple Ansible playbooks that can be used to perform any of the following tasks:
* Tune Satellite 6.1 or 6.2 for performance & scale
##Reference performance brief Article: 
* satellite 6.1: https://access.redhat.com/articles/2356131
* satellite 6.2: https://access.redhat.com/articles/2626101

## Getting Started
Ideally, you need two hosts to run this project:

1. Ansible Control node (referred to as `Control node` in the rest of this document) is the host from which this ansible project is run.
2. Destination node - This must be one of the following:
    - A Satellite server
    - Capsule servers

*Note*

1. You can get away with using one host by optionally choosing to use `Destination node` as the `Control node`.
2. Make sure that the `Control node` can connect to the `Destination node` via paswordless ssh.

#### On the Control node:

*Supported versions*
- RHEL 6
- RHEL 7

1. git clone this project.

   ```console
     # git clone https://github.com/redhat-performance/satellite-tune.git
   ```
   NOTE: Optionally you may utilize the script [control_node_setup.sh] (adhoc-scripts/control_node_setup.sh) to perform step 2 below.  The instructions to use this script are documented in the script itself.
2. Install `ansible` package on the Control node. For RHEL boxes, [access to EPEL] (https://access.redhat.com/solutions/3358) is required.

   ```console
     # yum install -y ansible
   ```
3. Create an inventory file named `inventory` (by copying `ansible/inventory.sample`) and update it as necessary:

  ```console
    # cp conf/hosts.ini.sample conf/hosts.ini
  ```

Now you can proceed to any of the following tasks:

 * [Tune a Satellite server for performance & scale](docs/satellite-perf-tune.md)
 * [Tune a Capsule server for performance & scale](docs/satellite-scale-tune.md)

Please check our [FAQ section](docs/faqs.md) for frequently asked questions
