## Interact wit AWS s3 from pyspark

This repo define the jars needed to interact with aws s3 
from pyspark.

in order to interact with AWS s3 you need two jars [hadoop-aws](https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-aws) and [aws-java-sdk-bundle](https://mvnrepository.com/artifact/com.amazonaws/aws-java-sdk-bundle) .

the correct versions for these two jars depend on your spark version.

you can check the correct version for [hadoop-aws](https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-aws) jar from [pom.xml](https://github.com/apache/spark/blob/v3.5.1/pom.xml#L125) file for your Spark version

this link for spark 3.5.1 you need to check the page for your spark version and search for
`<hadoop.version>` token.

then download the correct version for [hadoop-aws](https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-aws)
you will find the correct version for [aws-java-sdk-bundle](https://mvnrepository.com/artifact/com.amazonaws/aws-java-sdk-bundle) 
in the dependency for  [hadoop-aws](https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-aws) jar.

once these two jars downloaded you can add them in your spark-submit command or in the code using `.config('spark.jars', 'jar1,jar2')`


you can provide the AWS credentials in many ways
- in the code. check main.py
- in environment variables
- and others

more info can be founded here
https://hadoop.apache.org/docs/stable/hadoop-aws/tools/hadoop-aws/index.html
