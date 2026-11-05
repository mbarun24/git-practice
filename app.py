pip install boto3
import boto3 
ec2=boto3.client('ec2', region_name='us-east-1')
response=ec2.describe_instances()

filter = [
    {
        "Name": "tag:Environment", "values": ["production"]
    },
    {
        "Name" : "tag: auto-stop", "values": ["true"]
    },
    {   
        "Name" : "instance-state-name", "values": ["running"]
    }
]

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId'] 
        ec2.stop_instances(InstanceIds=[instance_id])
           
        print(f"Stopped instance: {instance_id}")


        print("Running from DEV branch")