# Increase max file descriptors limit for smart_proxy_dynflow_core on capsule

During Remote execution on large scale hosts will cause smart_proxy_dynflow_core going down often due to open file descriptors limitation: https://bugzilla.redhat.com/show_bug.cgi?id=

To check smart_proxy_dynflow_core's current limits on capsule use `/proc/<PID>/limits`
