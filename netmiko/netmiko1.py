from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.146',
    'username': 'aldi',
    'password': 'cisco'
}

net_connect = ConnectHandler(iosv_l2)
output = net_connect.send_command('show ip int brief')
print(output)

config_commands = ['int loop 2', 'ip address 3.3.3.3 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print(output)

for n in range(31, 36):
    print("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output)
