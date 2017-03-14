# Tune passenger configuration 

Passenger configuration is specified within the Apache configuration files and can be used to control the performance, scaling, and behavior of Foreman and Puppet.

The most important out-of-the box tunable that should be adjusted is the PassengerMaxPoolSize.  This should be adjusted to 1.5 * Physical CPU Cores available to Red Hat Satellite server. This configures the maximum number of processes available for both Foreman and Puppet on Red Hat Satellite 6.2 and capsules.  PassengerMaxInstancesPerApp can be used to prevent one application from consuming all available Passenger processes.

PassengerMaxRequestQueueSize determines the maximum number of queued requests before Passenger will send a HTTP 503 Service Error to the requester.  Depending upon the maximum expected burst of requests, it will be necessary to adjust the Passenger Queue.  A queued request consumes an Apache process and setting the queue above Apache’s MaxClients and ServerLimit configuration will force queued requests to wait within the ListenBacklog queue in Apache.  This will also block Apache from serving any other requests that do not require Foreman or Puppet.  It is recommended to adjust PassengerMaxRequestQueueSize to the maximum expected burst in Foreman and Puppet traffic, but below Apache’s MaxClients and ServerLimit configuration thus allowing other requests to complete without waiting for Passenger to free up Apache processes such as a client downloading content by running yum install or yum update.

If the environment has an issue with continuous growth in memory from either Foreman or Puppet, it is recommended to set PassengerMaxRequests such that those processes will be recycled to free up memory.  Preventing the Red Hat Satellite 6 server from swapping is critical to its performance and Scalability.  An example tuned configuration of Passenger for Red Hat  Satellite 6.2 is as follows:

Global Passenger configuration: /etc/httpd/conf.d/passenger.conf
