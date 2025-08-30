# Puppet manifest to install a specified package on the system.
package { 'werkzeug':
    ensure   => '2.1.1',
    provider => 'pip3'
}

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
    require  => Package['werkzeug']
}
