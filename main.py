from pyspark.sql import SparkSession

AWS_ACCESS_KEY = 'YOUR_ACCESS_KEY'
AWS_SECRET_KEY = 'YOUR_ACCESS_SECRET'
BUCKET_NAME = 'YOUR_BUCKET_NAME'
JARS_PATH = 'PATH_WHERE_YOUR_JARS_SAVED'

jars = ','.join(
    [f'{JARS_PATH}/hadoop-aws-3.3.4.jar',
     f'{JARS_PATH}/aws-java-sdk-bundle-1.12.767.jar'])

print(jars)

spark = (SparkSession.builder.appName('Interact With S3').master('local[*]')
         .config('spark.jars', jars)
         .config("fs.s3a.access.key", AWS_ACCESS_KEY)
         .config("fs.s3a.secret.key", AWS_SECRET_KEY)
         .getOrCreate())


spark.read.text(f's3a://{BUCKET_NAME}/license.md').show()

df = spark.range(100)
(df.write
 .format('csv')
 .option('header', 'true')
 .mode('overwrite')
 .save(f's3a://{BUCKET_NAME}/csv/file1'))


spark.stop()
