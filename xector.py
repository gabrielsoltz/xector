#!/usr/bin/env python3

import argparse
import json

from modules.url import URLModule
from modules.network import NetworkModule

if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,description='''
    xEctor
    https://github.com/gabrielsoltz/xector
    Author: Gabriel Soltz
    '''
    )
    
    parser.add_argument('-t', '--target', help="Target", required=True)
    args = vars(parser.parse_args())
    
    target = args["target"]
    
    URLObject = URLModule(target)
    NetworkObject = NetworkModule(target)
    
    URLData = {'images': URLObject.images, 'links': URLObject.links, 'js': URLObject.js, 'favicon': URLObject.favicon}
    NETWORKData = {'domain_name': NetworkObject.domain_name, 'name_servers': NetworkObject.name_servers, 'registrar': NetworkObject.registrar, 'registrar_url': NetworkObject.registrar_url, 'status': NetworkObject.status, 'registrant_name': NetworkObject.registrant_name, 'creation_date': NetworkObject.creation_date, 'expiration_date': NetworkObject.expiration_date, 'updated_date': NetworkObject.updated_date, 'emails': NetworkObject.emails}
    
    AllData = {'xector': [
        {'URLData': URLData}, 
        {'NETWORKData': NETWORKData}
    ]}
    
    print(json.dumps(AllData, indent=4, sort_keys=True))
