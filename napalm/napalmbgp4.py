import json
from napalm import get_network_driver

bgplist = ['172.16.1.1',
           '172.16.1.2',
           '172.17.1.2',
           '172.18.1.2'
           ]

for ip_address in bgplist:
    print ("Connecting to " + str(ip_address))
    driver = get_network_driver('ios')
    iosv_router = driver(ip_address, 'aldi', 'cisco')
    iosv_router.open()
    bgp_neighbors = iosv_router.get_bgp_neighbors()
    print (json.dumps(bgp_neighbors, sort_keys=True, indent=4))
    iosv_router.close()