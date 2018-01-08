# Introduction

The purpose of this project is to take the simulated data set created by the [dataset-generator](https://github.com/ibm-cloud-streaming-retail-demo/dataset-generator) and continuosly produce that data to Kafka.

This project is a Cloud Foundry application.

# Prerequisites

- You have followed the instructions in the project [dataset-generator](https://github.com/ibm-cloud-streaming-retail-demo/dataset-generator) to create a dataset, `OnlineRetail.json.gz`.
- You have an IBM Cloud account
- You have some knowledge of deploying Cloud Foundry applications on the IBM Cloud (E.g. https://developer.ibm.com/courses/all/bluemix-essentials/)

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
# and create a topic (for now, the default topic settings should suffice)
# https://console.bluemix.net/docs/services/MessageHub/index.html#messagehub

# bind the Message Hub instance to this application

# restage this application
cf restage ...
```


# Description

TODO

