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

# Setup

```
# clone this project
git clone https://github.com/ibm-cloud-streaming-retail-demo/kafka-producer-for-simulated-data
cd kafka-producer-for-simulated-data

# copy `OnlineRetail.json.gz` to this folder
cp ../dataset-generator/OnlineRetail.json.gz .

# deploy this application
cf push ...

# create IBM Message Hub (Kafka) service instance

# create a topic (for now, the default topic settings should suffice)
# use `transactions_load` for the topic name

# bind the Message Hub instance to this application
# https://console.bluemix.net/docs/cfapps/ee.html#ee_cf

# restage this application
cf restage ...
```


# Description

TODO

