## Interact wit AWS s3 from pyspark

This repo define the jars/packages needed to interact with aws s3 from pyspark.


in order to interact with AWS s3 you need two jars [hadoop-aws](https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-aws) and [aws-java-sdk-bundle](https://mvnrepository.com/artifact/com.amazonaws/aws-java-sdk-bundle) .

the correct versions for these two jars depend on your spark version.

you can check the correct version for [hadoop-aws](https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-aws) jar from [pom.xml](https://github.com/apache/spark/blob/v3.5.2/pom.xml#L125) file for your Spark version

this link for spark 3.5.2 you need to check the page for your spark version and search for
`<hadoop.version>` token.

then download the correct version for [hadoop-aws](https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-aws)
you will find the correct version for [aws-java-sdk-bundle](https://mvnrepository.com/artifact/com.amazonaws/aws-java-sdk-bundle) 
in the dependency for  [hadoop-aws](https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-aws) jar.

once these two jars downloaded you can add them in your spark-submit command using `--jars jar1.jar,jar2.jar` or in the code using `.config('spark.jars', 'jar1,jar2')`


an alterntive to downloading these jars is to set them as packages in your spark-submit command `--packages package2,package2` or in the code using `.config('spark.jars.packages','package1,package2')`


also there is a new SDK for AWS they call it V2, you can find it at [aws-sdk](https://mvnrepository.com/artifact/software.amazon.awssdk)

to use this v2 sdk you can use `software.amazon.awssdk:s3:2.27.15` instead of `amazonaws:aws-java-sdk-bundle`

again here you can use jars option or packages option

you can provide the AWS credentials in many ways
- in the code. check main.py
- in environment variables
- and others

more info can be founded here
https://hadoop.apache.org/docs/stable/hadoop-aws/tools/hadoop-aws/index.html


## Note
I am using minio for simplicity if you need to use AWS S3 you can remove these config related to
minio
.config("fs.s3a.endpoint", 'localhost:9000') 
.config("fs.s3a.connection.ssl.enabled", "false") 
.config("fs.s3a.path.style.access", "true") 
.config("fs.s3a.attempts.maximum", "1")
.config("fs.s3a.connection.establish.timeout", "1000")
.config("fs.s3a.connection.timeout", "10000")
