import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.210', 'aldi', 'cisco')
iosvl2.open()

bgp_neighbors = iosvl2.get_bgp_neighbors()
print(json.dumps(bgp_neighbors, sort_keys=True, indent=4))

iosvl2.close()
