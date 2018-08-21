# Introduction

The purpose of this project is to take the simulated data set created by the [dataset-generator](https://github.com/ibm-cloud-streaming-retail-demo/dataset-generator) and continuosly produce that data to Kafka.

This project is a Cloud Foundry application.

# Dependencies

- This project has a dependency on the datasets `OnlineRetail.json.gz` and `OnlineRetailCustomers.csv.gz` that are output from the [dataset-generator](https://github.com/ibm-cloud-streaming-retail-demo/dataset-generator)

# Prerequisites

- You have followed the instructions in the project [dataset-generator](https://github.com/ibm-cloud-streaming-retail-demo/dataset-generator) to create the datasets, `OnlineRetail.json.gz` and `OnlineRetailCustomers.csv.gz`
- You have an IBM Cloud account
- You have some knowledge of deploying Cloud Foundry applications on the IBM Cloud, E.g.
  - https://developer.ibm.com/courses/all/bluemix-essentials/ - only LAB 1 and 3 required
  - https://console.bluemix.net/docs/cfapps/index.html
- You have some knowledge of working with IBM Message Hub, E.g.
  - https://console.bluemix.net/docs/services/MessageHub/index.html#messagehub
- You have a Message Hub instance in the IBM Cloud space where you will be deploying this Cloud Foundry application.
- You are able to run unix shell scripts

# Deploy

- If you haven't already done so, create two Message Hub topics called `transactions_load` and `customers_load` in your Message Hub instance. The default topic creation settings should be ok to start with.

```
# clone this project
git clone https://github.com/ibm-cloud-streaming-retail-demo/kafka-producer-for-simulated-data
cd kafka-producer-for-simulated-data

# change the applications.name and applications.route values in the manifest.yml to values that
# should be unique to you

# copy `OnlineRetail.json.gz` and `OnlineRetailCustomers.csv.gz` to this folder
cp ../dataset-generator/OnlineRetail.json.gz .
cp ../dataset-generator/OnlineRetailCustomers.csv.gz .

# deploy this application
cf push [your_app_name]

# bind the Message Hub instance to this application
cf bind-service [your_app_name] [your_name_for_your_messagehub_service]

# restage this application
cf restage [your_app_name]
```

## Scaling

TODO (each instance of cloud foundry generates a unique dataset)

# Example data

An example of the transactions data published to Message Hub:

InvoiceNo | StockCode | Description             | Quantity | InvoiceDate    | UnitPrice | CustomerID | Country | LineNo | InvoiceTime | StoreID | TransactionID
-- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | --
5370812   | 15056BL   | EDWARDIAN PARASOL BLACK | 12       | 1515542400000 | 5.95      | 15332      | Lithuania  | 3 | 00:00:00 | 0 | 537081230180110

The main changes between this dataset and the dataset created by the  [dataset-generator](https://github.com/ibm-cloud-streaming-retail-demo/dataset-generator) project are:

- InvoiceDate has been converted to a unix timestamp (milliseconds since epoch)
- The following fields have been added:
  - LineNo - the invoice line item number
  - InvoiceTime - the invoice time (format HH:MM:SS)
  - StoreID - the store ID (each cloud foundry instance will have a unique store id - see TODO)
  - TransactionID - the unique transaction ID, derived from InvoiceNo, TODO

# Developing

Copy the file `etc/message_hub_vcap.json_template` to `etc/message_hub_vcap.json` and populate with your Message Hub instance values.  These can be found in the IBM Console in the section 'Credentials'.

```
cd kafka-producer-for-simulated-data
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt

./bin/run_locally.sh
```

Or, using docker:

```
docker run -it --rm -v "$PWD":/usr/src/myapp -w /usr/src/myapp amancevice/pandas:0.20.2-python3 bash -c "pip3 install -r requirements.txt && ./bin/run_locally.sh"
```

# Verifying data is being produced

To verify that the topic is receiving data, you can consume the data with:

```
cd kafka-producer-for-simulated-data
virtualenv venv
source venv/bin/activate

./bin/run_consumer.sh
```

- IMPORTANT: OSX users; if you receive the error: `SSL: CERTIFICATE_VERIFY_FAILED` you may need to google how to fix it, for example my running `/Applications/Python\ 3.6/Install\ Certificates.command`

Or, using docker:

```
docker run -it --rm -v "$PWD":/usr/src/myapp -w /usr/src/myapp amancevice/pandas:0.20.2-python3 bash -c "pip3 install -r requirements.txt && ./bin/run_consumer.sh"
```

# Description

TODO
