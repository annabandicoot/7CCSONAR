import csv
from ipregistry import ApiError, ClientError
from ipregistry import IpregistryClient
API_KEY = "<YUOR_API_KEY>"
PATH_TO_ATTACKER_IPS = "<YUOR_PATH_TO_CSV>"  # read unique IPs from honeypots “analysis/attackers_ip_unique"

try:
    path_to_attacker_ips = PATH_TO_ATTACKER_IPS
    with open(path_to_attacker_ips) as f:
        reader = csv.reader(f)
        next(reader)  #
        ipList = [row[1] for row in reader]

        try:
            apiKey = API_KEY
            client = IpregistryClient(apiKey)
            ipInfoList = client.lookup(ipList)
            with open("merged_results_of_ips_geo.csv", mode="w") as csv_file:
                fieldnames = ["IP Address", "Country", "Country Code"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                writer.writeheader()

                for lookupResult in ipInfoList:
                    try:
                        ip = lookupResult.ip
                        country = lookupResult.location["country"].get("name")
                        code = lookupResult.location["country"].get("code")
                        writer.writerow({"IP Address": ip, "Country": country, "Country Code": code})
                    except Exception as e:
                        print(e)

        except ApiError as e:
            print("API error", e)
        except ClientError as e:
            print("Client error", e)
except Exception as e:
    print("Unexpected error", e)
