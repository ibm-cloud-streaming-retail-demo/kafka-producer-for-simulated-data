#!/bin/bash

# abort on error
set -e

# abort on undefined variable
set -u

# get the project directory
BIN_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# get the project directory
PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"

# retrieve the file path for the message hub credentials
export VCAP_SERVICES_FILE="${PROJECT_DIR}/etc/message_hub_vcap.json"

if [[ ! -f "$VCAP_SERVICES_FILE" ]]; then
   echo "ERROR: Couldn't find '$VCAP_SERVICES_FILE'"
   exit -1
fi

# retrieve the json credentials
export VCAP_SERVICES="{$(cat "${VCAP_SERVICES_FILE}")}"
export TRANSACTIONS_TOPIC=transactions_load

python "${BIN_DIR}/consumer.py"
