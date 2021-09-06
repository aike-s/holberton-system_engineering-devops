# configured to use the private key ~/.ssh/holberton
# configured to refuse to authenticate using a password

file_line {'Creating a custom HTTP header response':
    path => '/etc/nginx/sites-available/default',
    after => 'server_name _;',
    line => 'add_header X-Served-By $HOSTNAME always',
}