# Puppet manifest to install a specified package on the system.
package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3'
}
