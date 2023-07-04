import os
from google.cloud import storage

KEY_PATH = "GCP_Service_API.json"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = KEY_PATH

# bucket 리스트 가져오기
storage_client = storage.Client()
buckets = list(storage_client.list_buckets())
print(buckets)

# 업로드할 파일 경로
upload_file_path = "./upload_to_bucket.txt"

# GCP에 저장할 파일명
destination_blob_name = "uploaded_bucket.txt"

# 업로드할 목적지 bucket 지정
bucket_name = "bles-bucket-1"
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(destination_blob_name)

# 업로드
blob.upload_from_filename(upload_file_path)

print("Complete")