# configured to use the private key ~/.ssh/holberton
# configured to refuse to authenticate using a password

file_line {'Conf to use private key':
    path => '~/.ssh/config',
    line => 'IdentityFile ~/.ssh/holberton',
}
file_line {'Conf to authenticate using a password':
    path => '~/.ssh/config'
    line => 'PasswordAuthentication no',
}