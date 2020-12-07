users = LOAD '/user/maria_dev/data/ml-100k/u.user'
        USING PigStorage('|')
        AS (userID: int, age: int, gender: chararray, occupation: chararray, zip: int);

STORE users INTO 'hbase://users'
  USING org.apache.pig.backed.hadoop.hbase.HBaseStorage (
    'userinfo:age,userinfo:gender,userinfo:occupation,userinfo:zip');