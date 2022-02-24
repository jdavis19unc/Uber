import pandas as pd

d = pd.read_csv("data.csv", index_col=False, header=0)
d = pd.DataFrame(d)
print(d)
test = {"Price": 1.1, "Destination": 1.1}
d = d.append(test, ignore_index=True)
print(d)

d.to_csv("d2.csv")