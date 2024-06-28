# Craeting a file with the specified directory and inserting (content) to it
file { '/tmp/school':
  ensure  =>  present,
  content =>  'I love Puppet',
  mode    =>  '0744',
  owner   =>  www-data,
  group   =>  www-data,
}

