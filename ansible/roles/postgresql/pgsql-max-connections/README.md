# Increase postgresql max_connections

For concurrent registrations & scale postgresql max_connections needs to be increased. By default 90-100 concurrent registrations are possible. with this limit and other passenge tunings, concurrent registrations can be increased to 200: https://bugzilla.redhat.com/show_bug.cgi?id=

max_connections are set here: /var/lib/pgsql/data/postgresql.conf
