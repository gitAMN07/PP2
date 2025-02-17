import json

file_path = "sample-data.json"
with open(file_path, "r") as json_file:
    data = json.load(json_file)

interfaces = []
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes["descr"] if attributes["descr"] else ""
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    
    interfaces.append((dn, description, speed, mtu))

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<5}")
print("-" * 80)
for dn, description, speed, mtu in interfaces:
    print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<5}")