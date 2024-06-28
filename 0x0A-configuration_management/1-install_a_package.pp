# Using Puppet to install Flask Where version should be 2.1.0
exec { 'install_flask_2.1.0':
  command => 'pip3 install flask==2.1.0',
  path    => ['/usr/bin', '/bin'],
}