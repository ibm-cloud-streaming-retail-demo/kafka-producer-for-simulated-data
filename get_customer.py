#!/usr/local/bin/python3

from faker import Faker
import pandas as pd
import datetime
import numpy as np

def getcustchange():
    # Function to pull a random existing customer record, create a new address, and return the results
    fake = Faker('en_GB')
    df = pd.read_csv('OnlineRetailCustomers.csv.gz', compression='gzip', header=None, usecols=[1,2], names=['customerID', 'name'])
    customer = df.iloc[np.random.randint(0, len(df))]
    # Remove df from memory
    del df
    # Change address, add new validFrom time, and return object with new values
    customer['address'] = fake.address().replace("\n", " ")
    customer['validFrom'] = datetime.datetime.now()
    return customer
