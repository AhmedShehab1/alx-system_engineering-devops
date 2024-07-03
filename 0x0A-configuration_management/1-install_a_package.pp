# install Werzeug dependency for flask
exec {'install_werkzeug':
  command => 'pip3 install Werkzeug',
  path    => ['/usr/bin', 'bin'],
  unless  => 'pip3 show Werkzeug',
}
# install flask v: 2.1
exec {'install_flask_2.1.0':
  command => 'pip3 install flask==2.1.0',
  path    => ['/usr/bin', '/bin'],
  unless  => 'pip3 show flask | grep -q "Version: 2.1.0"',
  require => Exec['install_werkzeug'],
}
