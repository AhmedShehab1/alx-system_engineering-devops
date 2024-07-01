# Using Puppet to configure config file in order to connect to any server without passwd authetnication

  $str = "HOST *\n\tPasswordAuthentication no\n\tIdentityFile ~/.ssh/school/n"
file { '~/.ssh/config':
  ensure  => present,
  content => $str,
}
