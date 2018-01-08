# Introduction

The purpose of this project is to take the simulated data set created by the [dataset-generator](https://github.com/ibm-cloud-streaming-retail-demo/dataset-generator) and continuosly produce that data to Kafka.

This project is a Cloud Foundry application.

# Prerequisites

- You have followed the instructions in the project [dataset-generator](https://github.com/ibm-cloud-streaming-retail-demo/dataset-generator) to create a dataset, `OnlineRetail.json.gz`.
- You have an IBM Cloud account
- You have some knowledge of deploying Cloud Foundry applications on the IBM Cloud, E.g. 
  - https://developer.ibm.com/courses/all/bluemix-essentials/ - only LAB 1 and 3 required
  - https://console.bluemix.net/docs/cfapps/index.html
- You have some knowledge of working with IBM Message Hub, E.g.
  - https://console.bluemix.net/docs/services/MessageHub/index.html#messagehub
- You have created a Message Hub topic called `transactions_load`.  Use the default topic creation settings.

# Deploy

```
# clone this project
git clone https://github.com/ibm-cloud-streaming-retail-demo/kafka-producer-for-simulated-data
cd kafka-producer-for-simulated-data

# change the applications.name and applications.route values in the manifest.yml to values that
# should be unique to you

# copy `OnlineRetail.json.gz` to this folder
cp ../dataset-generator/OnlineRetail.json.gz .

# deploy this application
cf push [your_app_name]

# bind the Message Hub instance to this application
cf bind-service [your_app_name] [your_name_for_your_messagehub_service]

# restage this application
cf restage [your_app_name]
```

# Developing

Copy the file `etc/message_hub_vcap.json_template` to `etc/message_hub_vcap.json` and populate with your Message Hub instance values.  These can be found in the IBM Console in the section 'Credentials'.

```
cd kafka-producer-for-simulated-data
virtualenv venv
source venv/bin/activate

./bin/run_local.sh
```


# Description

TODO

