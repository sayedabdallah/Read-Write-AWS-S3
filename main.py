"""
in order to interact with AWS s3 you need to jars hadoop-aws and aws-java-sdk-bundle
the versions depends on your spark version.
you can check the correct version based on this file
https://github.com/apache/spark/blob/v3.5.1/pom.xml#L125
this link for spark 3.5.1 you need to check the page for your spark version and search for
`<hadoop.version>` token.
then from this page https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-aws download
the correct version for hadoop-aws jar, you find in the dependency for this jar the
aws-java-sdk-bundle jar required version

once these two jars downloaded you can add them in your spark-submit command or in the code

you can provide the AWS credentials in many ways
- in the code as below
- in environment variables
- and others

more info can be founded here
https://hadoop.apache.org/docs/stable/hadoop-aws/tools/hadoop-aws/index.html
"""
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
