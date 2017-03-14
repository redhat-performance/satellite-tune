# Increase max file descriptors limit for qdrouterd

Abive 2-3k hosts with katello-agent qdrouterd causing file descriptors leak: https://bugzilla.redhat.com/show_bug.cgi?id=

To check qdrouterd's current limits use `/proc/<PID>/limits`
