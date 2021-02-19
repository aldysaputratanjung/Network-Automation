import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosv = driver('192.168.122.210', 'aldi', 'cisco')
iosv.open()

ios_output = iosv.get_bgp_neighbors()
print(json.dumps(ios_output, sort_keys=True, indent=4))

iosv.close()
