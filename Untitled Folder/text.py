with open('soybean-small.data', "r") as data:
    lines = data.read().split("\n")
    array = [i.split(",") for i in lines]
print array
data.close()
