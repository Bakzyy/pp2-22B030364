import json

with open('/Users/bakustar2005/Documents/pp2/tsis4/json/sample-data.json') as f:
    data = json.load(f)

    print("Interface Status")
    print("================================================================================")
    print("DN                                                 Description           Speed    MTU  ")
    print("-------------------------------------------------- --------------------  ------  ------")


    for i in data['imdata']:
        l1PhysIf = i["l1PhysIf"]
        attributes = l1PhysIf["attributes"]
        dn = attributes["dn"]
        speed = attributes["speed"]
        mtu = attributes["mtu"]
        if len(dn) == 42:
            print(dn + "                             " , speed , " ", mtu)