## Step 1: Install below packages

#pip install s3fs
#pip install pandas-profiling

## Step 2 : Use the below code to perform profiling:
import boto3
import pandas as pd
from pandas_profiling import ProfileReport
import re

s3 = boto3.resource('s3')
s3_bucket = ‘s3_bucket_name’
Path_Prefix=‘s3_bucket_prefix’

bucket = s3.Bucket(s3_bucket)
for path_obj in bucket.objects.filter(Prefix=Path_Prefix):
    Table_name = re.findall(f'{Path_Prefix}(.+?)/.', path_obj.key)[0]
    s3_Table_Prefix= f'{Path_Prefix}{Table_name}/'
    print(s3_Table_Prefix)
    df = (pd.read_csv(f"s3://{s3_bucket}/{obj.key}",sep = '|') for obj in bucket.objects.filter(Prefix=s3_Table_Prefix))
    df = pd.concat(df)
    prof = ProfileReport(df)
    prof.to_file(output_file=f'{Table_name}_output.html')
