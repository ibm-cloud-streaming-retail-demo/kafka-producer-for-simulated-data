#!/bin/bash

# abort on error
set -e 

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export VCAP_SERVICES="{$(cat ${DIR}/../etc/message_hub_vcap.json)}"
export PORT=12345
export TRANSACTIONS_TOPIC=transactions_load
export CF_INSTANCE_INDEX=0

python3 index.py
