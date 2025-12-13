import boto3

# Create S3 client
s3 = boto3.client('s3')

bucket_name = 'november-23'
file_key = 'index(1).html'

# Function to change storage class
def change_storage_class(bucket, key, storage_class):
    s3.copy_object(
        Bucket=bucket,
        Key=key,
        CopySource={'Bucket': bucket_name, 'Key': file_key},
        StorageClass=storage_class,
        MetadataDirective='COPY'
    )
    print(f"{key} storage class changed to {storage_class}")

# Change storage class step by step
change_storage_class(bucket_name, file_key, 'INTELLIGENT_TIERING')  # Standard → Intelligent-Tiering
#change_storage_class(bucket_name, file_key, 'ONEZONE_IA')            # Intelligent-Tiering → One Zone-IA
#change_storage_class(bucket_name, file_key, 'DEEP_ARCHIVE')          # One Zone-IA → Glacier Deep Archive

    
    