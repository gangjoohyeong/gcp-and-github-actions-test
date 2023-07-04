import os
from google.cloud import storage

KEY_PATH = "GCP_Service_API.json"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = KEY_PATH

# bucket 리스트 가져오기
storage_client = storage.Client()
buckets = list(storage_client.list_buckets())
print(buckets)

# 다운로드한 파일을 저장할 파일 경로
destination_file_path =  "./downloaded_data.csv"

# GCP에 저장되어 있는 다운로드할 파일명
source_blob_name = "newspaper_VALID_1250_1300_summarize.csv"

# 다운로드할 파일이 있는 bucket 지정
bucket_name = "bles-bucket-1"
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(source_blob_name)

# 다운로드
blob.download_to_filename(destination_file_path)

print("Complete")


