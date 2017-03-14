# Increase max file descriptors limit for qpidd

Abive 2-3k hosts with katello-agent qpidd causing file descriptors leak: https://bugzilla.redhat.com/show_bug.cgi?id=

To check qpidd's current limits use `/proc/<PID>/limits`
