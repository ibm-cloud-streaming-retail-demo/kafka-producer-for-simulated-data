#!/usr/local/bin/python3

from kafka import KafkaConsumer 
from kafka.structs import TopicPartition, OffsetAndMetadata
import sys
import ssl
import json
import os
import signal
import time
import io

class Application:

    def __init__( self ):
        signal.signal( signal.SIGINT, lambda signal, frame: self._signal_handler() )
        self.terminated = False
        self.opts = self._get_opts()

    def _signal_handler( self ):
        self.terminated = True

    def MainLoop( self ):        
        print('Starting consumer.py')
        print('**********************************************************************')
        print('* IMPORTANT: It may take 30 seconds before you see any transactions. *')
        print('**********************************************************************')

        consumer = self._get_consumer(self.opts)

        while not self.terminated:
            data_dict = consumer.poll(timeout_ms=10000, max_records=100)

            if data_dict is None:
                print('No data found')
            else:
                for key in data_dict.keys():
                    for msg in data_dict[key]:
                        print(msg)
        
        print('Exiting ...')
        consumer.close(autocommit=False)

    def _get_opts(self):
        opts = {}
        if os.environ.get('VCAP_SERVICES'):
            vcap_services = json.loads(os.environ.get('VCAP_SERVICES'))
            for vcap_service in vcap_services:
                if vcap_service.startswith('messagehub'):
                    messagehub_service = vcap_services[vcap_service][0]
                    opts['brokers'] = ','.join(messagehub_service['credentials']['kafka_brokers_sasl'])
                    opts['api_key'] = messagehub_service['credentials']['api_key']
                    opts['username'] = messagehub_service['credentials']['user']
                    opts['password'] = messagehub_service['credentials']['password']
                    opts['rest_endpoint'] = messagehub_service['credentials']['kafka_admin_url']

            if os.environ.get('TRANSACTIONS_TOPIC'):
                opts['kafka_topic'] = os.getenv('TRANSACTIONS_TOPIC')
            else:
                print('ERROR: TRANSACTIONS_TOPIC environment variable not set')
                sys.exit(-1)

            return opts
        else:
            print('ERROR: no VCAP_SERVICES found in environment')
            sys.exit(-1)
        
        if opts == {}:
            print('ERROR: no messagehub bound to application')
            sys.exit(-1)

    def _get_consumer(self, opts):
        sasl_mechanism = 'PLAIN'
        security_protocol = 'SASL_SSL'
        
        # Create a new context using system defaults, disable all but TLS1.2
        context = ssl.create_default_context()
        context.options &= ssl.OP_NO_TLSv1
        context.options &= ssl.OP_NO_TLSv1_1

        def get_random_group_id():
            import time; 
            return time.time()*1000.0

        consumer = KafkaConsumer(
                             bootstrap_servers = opts['brokers'],
                             sasl_plain_username = opts['username'],
                             sasl_plain_password = opts['password'],
                             security_protocol = security_protocol,
                             ssl_context = context,
                             sasl_mechanism = sasl_mechanism,
                             api_version = (0,10),
                             enable_auto_commit = False,
                             auto_offset_reset = 'earliest',
                             group_id = get_random_group_id()
                             )

        consumer.subscribe([ opts['kafka_topic'] ])
        return consumer

if __name__ == "__main__":
    app = Application()
    app.MainLoop()
