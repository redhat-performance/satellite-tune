# Increase max file descriptors limit for httpd

There was a bug that pulp causing file descriptors leak: https://bugzilla.redhat.com/show_bug.cgi?id=1328984

To check httpd's current limits use `/proc/<PID>/limits`
