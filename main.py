import csv
from collections import Counter

protocols = Counter()
source_ips = Counter()

with open("capture.csv", "r", encoding="latin-1") as file:
    reader = csv.DictReader(file)

    for row in reader:
        protocol = row["Protocol"]
        source = row["Source"]

        protocols[protocol] += 1
        source_ips[source] += 1

print("\n==== Protocol Counts ====")

for protocol, count in protocols.items():
    print(f"{protocol}: {count}")

print("\n==== Top Source IPs ====")

for ip, count in source_ips.most_common(10):
    print(f"{ip}: {count}")