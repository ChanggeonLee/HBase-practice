from starbase import Connection
import csv

c = Connection(host="127.0.0.1", port=8005) # default is '127.0.0.1:8000'
ratings = c.table('ratings')
if (ratings.exists()):
  ratings.drop()
print(ratings.create('rating'))

batch = ratings.batch()
if batch:
  print("Batch update... \n")
  with open("./data/ml-latest-small/ratings.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip header
    for row in reader:
      batch.update(row[0], {'rating' : {row[1]: row[2]}})

    print("Committing... \n")
    batch.commit(finalize=True)

print("Get ratings for users... \n")
print("Rating for UserID 1: ")
print(ratings.fetch("1"))

print("\n")
print("Ratings for UserID 33: ")
print(ratings.fetch("33"))