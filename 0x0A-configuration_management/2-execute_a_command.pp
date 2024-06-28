# Puppet Manifest that kills a process named killmenow
exec { 'terminate_process':
  command  => 'pkill -x killmenow',
  path     => '/usr/bin:usr/sbin:/bin',
  provider => shell,
  returns  => [0, 1],
}

