from napalm import get_network_driver
import json

driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.210', 'aldi', 'cisco')
iosvl2.open()

ios_output = iosvl2.get_facts()
print(json.dumps(ios_output, indent=5))
