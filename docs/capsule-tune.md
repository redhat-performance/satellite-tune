## Tuning capsule

   Different Tunings are targetted for different use cases. 
   Update hosts.ini before starting tunings

### Passenger Tuning

* [Passenger tunings] 
  
  ```console
     #ansible-playbook  -i conf/hosts.ini ansible/passenger.yaml
  ```

* [Puppet tunings]

  ```console
     #ansible-playbook  -i conf/hosts.ini ansible/puppet.yaml
   ```

* [qpidd tunings] 
 
  ```console
     #ansible-playbook  -i conf/hosts.ini ansible/qpidd.yaml
  ```

* [qdrouterd tunings] 

   ```console
     #ansible-playbook  -i conf/hosts.ini ansible/qdrouterd.yaml
   ```

* [httpd tunings] 

   ```console
     #ansible-playbook  -i conf/hosts.ini ansible/httpd.yaml

   ```

* [smart_proxy_dynflow_core tunings]

  ``` console
    #ansible-playbook  -i conf/hosts.ini ansible/smart_proxy_dynflow_core.yaml
  ```
