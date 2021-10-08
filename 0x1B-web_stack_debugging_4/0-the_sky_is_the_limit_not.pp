# Fix problem to handle multiple request at the same time
exec {'expand-limit':
  path    => '/usr/local/bin/:/bin/',
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
}

exec {'restart-nginx':
  path    => '/etc/init.d/',
  command => 'nginx restart',
}
