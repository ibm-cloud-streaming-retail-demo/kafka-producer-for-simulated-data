#!/usr/local/bin/python3

import sys
import json
import os


def get_opts():
    opts = {}

    if os.environ.get('VCAP_SERVICES'):
        print('Found VCAP_SERVICES environment variable.')
        vcap_services = json.loads(os.environ.get('VCAP_SERVICES'))
        for vcap_service in vcap_services:
            if vcap_service.startswith('messagehub'):
                messagehub_service = vcap_services[vcap_service][0]

                brokers = messagehub_service['credentials']['kafka_brokers_sasl']

                # Ensure the broker parameter was set
                if  ''.join(brokers).strip() == '':
                    raise LookupError('ERROR: brokers not set: ' + str(brokers))

                opts['brokers'] = ','.join(messagehub_service['credentials']['kafka_brokers_sasl'])
                opts['api_key'] = messagehub_service['credentials']['api_key']
                opts['username'] = messagehub_service['credentials']['user']
                opts['password'] = messagehub_service['credentials']['password']
                opts['rest_endpoint'] = messagehub_service['credentials']['kafka_admin_url']

    else:
        raise LookupError('ERROR: no VCAP_SERVICES found in environment')

    if opts == {}:
        raise LookupError('ERROR: no messagehub bound to application')

    # create a copy so we can remove sensitive data and print out the rest
    opts_copy = opts.copy()
    del opts_copy['password']
    del opts_copy['api_key']

    print(">>> SERVICE CREDENTIALS START") 
    print(opts_copy)
    print(">>> SERVICE CREDENTIALS END") 

    return opts
