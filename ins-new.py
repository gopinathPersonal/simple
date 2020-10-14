import boto3
import sys

accesskey = 'AKIAQS5DASRCGEER732K'
secretkey = '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'


client = boto3.client('ec2','us-west-2', aws_access_key_id=accesskey, aws_secret_access_key=secretkey)

data1 = client.describe_instances()
for data2 in data1["Reservations"]:
	for data13 in data2["Instances"]:
		print(data13)
