import os
import json
import base64
import socket
import logging
import requests
import threading
from python_v2ray.config_parser import parse_uri

logging.disable(logging.WARNING)

def testSubscriptionConfigs(sub_url):
    global x 
    response = requests.get(sub_url, stream=True)

    if response.status_code == 200:
        for config in response.iter_lines():
            config = config.decode()
                
            if not config.startswith("#"):
                parsed_config = parse_uri(config_uri=config)

                if parsed_config:
                    addr_port = (parsed_config.address, parsed_config.port)                    
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                        client.settimeout(2.0)
                        try:
                            client.connect(addr_port)
                            with open("configs.txt", "a") as f:
                                f.write(f"{config}\n")
                            
                        except TimeoutError: # timeout
                            continue
                        except socket.gaierror: # could not resolve the domain
                            continue
                        except ConnectionRefusedError: # connection refuss
                            continue
                        except OSError: # No route to host (parsing problem)
                            continue

if not os.path.exists("sources.txt"):
    print("sources.txt doesn't find")
    exit()

with open("sources.txt" , "r") as f:
    source_urls = f.readlines()
    source_urls = list(set(source_urls))

for url in source_urls:
    url = url.strip()
    threading.Thread(target=testSubscriptionConfigs, args=[url]).start()