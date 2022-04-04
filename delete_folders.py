from common_variables import bucket_name
import boto3

s3 = boto3.resource('s3')

#Script will get the values from current_year and previous_year scripts and will delete those folder in S3

bucket = s3.Bucket(bucket_name)

def delete_folder(year,month,days):
    day=str(year)+"/"+str(month)+"/"+str(days)+"/"
    for obj in bucket.objects.filter(Prefix=day):
        s3.Object(bucket.name,obj.key).delete()