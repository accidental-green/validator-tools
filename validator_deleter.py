import subprocess

# Print deleted users
print("sudo userdel geth")
print("sudo userdel besu")
print("sudo userdel nethermind")
print("sudo userdel teku")
print("sudo userdel nimbus")
print("sudo userdel lighthousebeacon")
print("sudo userdel lighthousevalidator")
print("sudo userdel prysmbeacon")
print("sudo userdel prysmvalidator")
print("sudo userdel mevboost")

# Delete Users
subprocess.run(['sudo', 'userdel', 'geth'])
subprocess.run(['sudo', 'userdel', 'besu'])
subprocess.run(['sudo', 'userdel', 'nethermind'])
subprocess.run(['sudo', 'userdel', 'teku'])
subprocess.run(['sudo', 'userdel', 'nimbus'])
subprocess.run(['sudo', 'userdel', 'lighthousebeacon'])
subprocess.run(['sudo', 'userdel', 'lighthousevalidator'])
subprocess.run(['sudo', 'userdel', 'prysmbeacon'])
subprocess.run(['sudo', 'userdel', 'prysmvalidator'])
subprocess.run(['sudo', 'userdel', 'mevboost'])

# Print /usr/local/bin
print("sudo rm -rf /usr/local/bin/beacon-chain")
print("sudo rm -rf /usr/local/bin/geth")
print("sudo rm -rf /usr/local/bin/mev-boost")
print("sudo rm -rf /usr/local/bin/nimbus_beacon_node")
print("sudo rm -rf /usr/local/bin/validator")
print("sudo rm -rf /usr/local/bin/besu")
print("sudo rm -rf /usr/local/bin/lighthouse")
print("sudo rm -rf /usr/local/bin/nethermind")
print("sudo rm -rf /usr/local/bin/teku")

# Delete files in /usr/local/bin
subprocess.run(['sudo', 'rm', '-rf', '/usr/local/bin/beacon-chain'])
subprocess.run(['sudo', 'rm', '-rf', '/usr/local/bin/geth'])
subprocess.run(['sudo', 'rm', '-rf', '/usr/local/bin/mev-boost'])
subprocess.run(['sudo', 'rm', '-rf', '/usr/local/bin/nimbus_beacon_node'])
subprocess.run(['sudo', 'rm', '-rf', '/usr/local/bin/validator'])
subprocess.run(['sudo', 'rm', '-rf', '/usr/local/bin/besu'])
subprocess.run(['sudo', 'rm', '-rf', '/usr/local/bin/lighthouse'])
subprocess.run(['sudo', 'rm', '-rf', '/usr/local/bin/nethermind'])
subprocess.run(['sudo', 'rm', '-rf', '/usr/local/bin/teku'])

# Print /var/lib
print("sudo rm -rf /var/lib/geth")
print("sudo rm -rf /var/lib/besu")
print("sudo rm -rf /var/lib/nethermind")
print("sudo rm -rf /var/lib/teku")
print("sudo rm -rf /var/lib/prysm")
print("sudo rm -rf /var/lib/lighthouse")
print("sudo rm -rf /var/lib/nimbus")
print("sudo rm -rf /var/lib/jwtsecret")

# Delete files in /var/lib
subprocess.run(['sudo', 'rm', '-rf', '/var/lib/geth'])
subprocess.run(['sudo', 'rm', '-rf', '/var/lib/besu'])
subprocess.run(['sudo', 'rm', '-rf', '/var/lib/nethermind'])
subprocess.run(['sudo', 'rm', '-rf', '/var/lib/teku'])
subprocess.run(['sudo', 'rm', '-rf', '/var/lib/prysm'])
subprocess.run(['sudo', 'rm', '-rf', '/var/lib/lighthouse'])
subprocess.run(['sudo', 'rm', '-rf', '/var/lib/nimbus'])
subprocess.run(['sudo', 'rm', '-rf', '/var/lib/jwtsecret'])

# Print removal commands
print("sudo rm -f /etc/systemd/system/geth.service")
print("sudo rm -f /etc/systemd/system/besu.service")
print("sudo rm -f /etc/systemd/system/nethermind.service")
print("sudo rm -f /etc/systemd/system/nimbus.service")
print("sudo rm -f /etc/systemd/system/teku.service")
print("sudo rm -f /etc/systemd/system/prysmbeacon.service")
print("sudo rm -f /etc/systemd/system/prysmvalidator.service")
print("sudo rm -f /etc/systemd/system/lighthousebeacon.service")
print("sudo rm -f /etc/systemd/system/lighthousevalidator.service")
print("sudo rm -f /etc/systemd/system/mevboost.service")
print("sudo systemctl daemon-reload")

# Execute removal of service files
subprocess.run(['sudo', 'rm', '-f', '/etc/systemd/system/geth.service'])
subprocess.run(['sudo', 'rm', '-f', '/etc/systemd/system/besu.service'])
subprocess.run(['sudo', 'rm', '-f', '/etc/systemd/system/nethermind.service'])
subprocess.run(['sudo', 'rm', '-f', '/etc/systemd/system/nimbus.service'])
subprocess.run(['sudo', 'rm', '-f', '/etc/systemd/system/teku.service'])
subprocess.run(['sudo', 'rm', '-f', '/etc/systemd/system/prysmbeacon.service'])
subprocess.run(['sudo', 'rm', '-f', '/etc/systemd/system/prysmvalidator.service'])
subprocess.run(['sudo', 'rm', '-f', '/etc/systemd/system/lighthousebeacon.service'])
subprocess.run(['sudo', 'rm', '-f', '/etc/systemd/system/lighthousevalidator.service'])
subprocess.run(['sudo', 'rm', '-f', '/etc/systemd/system/mevboost.service'])
subprocess.run(['sudo', 'systemctl', 'daemon-reload'])

