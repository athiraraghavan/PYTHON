import csv

header = ["place", "name", "age"]
with open("city.csv", "w") as file:
    write = csv.DictWriter(file, fieldnames=header)
    write.writeheader()
    write.writerow({"place": "kasaragod", "name": "Athira", "age": 21})
    write.writerow({"place": "kannur", "name": "Bavitha", "age": 21})
    write.writerow({"place": "idukki", "name": "Aparna", "age": 23})
    write.writerow({"place": "alapuzha", "name": "Gopika", "age": 21})
with open("city.csv", "r") as file:
    read = csv.DictReader(file);
    n = input("Enter the column name you want(place,name,age):")
    for i in read:
     print(i[n])