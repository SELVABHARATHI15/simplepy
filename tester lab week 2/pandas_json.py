import pandas as pd
# x = pd.read_json("data3.json")
# print(x)
df = {
    "name" : ["John", "sam", "Athi", "ram"],
    "age" : [28, 24, 32, 27],
    "city" : ["thiruvarur", "delhi", "nagapattinam", "chennai"]
}
x = pd.DataFrame(df,index=["one", "two", "three", "four"])
print(x)