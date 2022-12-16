
![Picture1](https://user-images.githubusercontent.com/39345855/208182950-34a28fda-b59b-4df1-9d0b-b9883d7ce2b1.jpg)

### Project Overview
* Users in this architecture purchase things from online retailers and generate an order transaction that is kept in DynamoDB. The raw data layer stores the order transaction data that is fed into the data lake. To accomplish this, enable Kinesis Data Streams for DynamoDB, and we will stream real-time transactions from DynamoDB into kinesis data streams, process the streaming data with lambda, and insert the data into the next kinesis stream, where a glue streaming job will process and insert the data into Apache Hudi Transaction data lake, and build dashboards and derive insights using QuickSight.

## Video Tutorial 
* Link: https://www.youtube.com/watch?v=cWmRZ9WOZB8

## Code 
* Link: https://github.com/soumilshah1995/dynamodb-hudi-stream-project


## Step by Step guide with Instruction and Screenshots 
* PDF https://drive.google.com/file/d/1W-E_SupsoI8VZWGtq5d7doxdWdNDPEoj/view?usp=sharing
 
# Steps 



### Step 1: 
* Users in this architecture purchase things from online retailers and generate an order transaction that is kept in DynamoDB.

## Step 2: 
* The raw data layer stores the order transaction data that is fed into the data lake. To accomplish this, enable Kinesis Data Streams for DynamoDB, and we will stream real-time transactions from DynamoDB into kinesis data streams, process the streaming data with lambda, and insert the data into the next kinesis stream, where a glue streaming job will process and insert the data into Apache Hudi Transaction data lake.  

## Step 3: 
* Users can build dashboards and derive insights using QuickSight.



