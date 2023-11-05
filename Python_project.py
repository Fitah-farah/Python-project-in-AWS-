#using python boto3 module to manage and configure AWS services
import json
import boto3

def get_volume_id_from_arn(volume_arn):
    #slipt the arn using the colon(':') saperator
    arn_parts = volume_arn.split(':')
    #the volume id is the last part of arn after the 'volume/' prefix
    volume_id = arn_parts[-1].split('/')[-1]
    
    return volume_id
def lambda_handler(event, context):
   # TODO: write code...
    volume_arn = event['resources'][0]
    volume_id = get_volume_id_from_arn(volume_arn)
   
   #using boto3 client and modify the volume
    ec2_client = boto3.client('ec2')
    
    response = ec2_client.modify_volume(
   
        VolumeId = volume_id,
    
        VolumeType='gp3',
    )
    
 
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
