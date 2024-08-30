# using jars option and AWS SDK V2
from pyspark.sql import SparkSession

AWS_ACCESS_KEY = 'sayed' #'Replace it with your access key
AWS_SECRET_KEY = 'sayedsayed' #'Replace it with your access secret key
BUCKET_NAME = 'test' # Replace it with your bucket name
JARS_PATH = '.' # replace it with path where you saved your jars

# alot of jars are required so it is easier to use packages option, see main4.py
# this code will fail as more jars are required
jars = ','.join(
    [f'{JARS_PATH}/hadoop-aws-3.3.4.jar',
     f'{JARS_PATH}/software.amazon.awssdk_s3-2.27.15.jar'])

print(jars)

spark = (SparkSession.builder.appName('Interact With S3').master('local[*]')
         .config('spark.jars', jars)
         .config("fs.s3a.access.key", AWS_ACCESS_KEY)
         .config("fs.s3a.secret.key", AWS_SECRET_KEY)
         .config("fs.s3a.endpoint", 'localhost:9000') 
         .config("fs.s3a.connection.ssl.enabled", "false") 
         .config("fs.s3a.path.style.access", "true") 
         .config("fs.s3a.attempts.maximum", "1")
         .config("fs.s3a.connection.establish.timeout", "1000")
         .config("fs.s3a.connection.timeout", "10000")
         .getOrCreate())


spark.read.text(f's3a://{BUCKET_NAME}/license.md').show()

df = spark.range(100)
(df.write
 .format('csv')
 .option('header', 'true')
 .mode('overwrite')
 .save(f's3a://{BUCKET_NAME}/csv/file1'))


spark.stop()
