import boto3

# Create S3 client
s3 = boto3.client('s3')

bucket_name = 'november-23'
file_key = 'index.html'  # update with folder path if needed, e.g., 'folder/index(1).html'

# Function to change storage class
def change_storage_class(bucket, key, storage_class):
    try:
        s3.copy_object(
            Bucket=bucket,
            Key=key,
            CopySource={'Bucket': bucket, 'Key': key},  # use function parameters
            StorageClass=storage_class,
            MetadataDirective='COPY'
        )
        print(f"{key} storage class changed to {storage_class}")
    except s3.exceptions.NoSuchKey:
        print(f"Error: The file '{key}' does not exist in bucket '{bucket}'.")

# Change storage class step by step
# change_storage_class(bucket_name, file_key, 'INTELLIGENT_TIERING')  # Standard → Intelligent-Tiering
change_storage_class(bucket_name, file_key, 'ONEZONE_IA')           # Intelligent-Tiering → One Zone-IA
# change_storage_class(bucket_name, file_key, 'DEEP_ARCHIVE')         # One Zone-IA → Glacier Deep Archive
