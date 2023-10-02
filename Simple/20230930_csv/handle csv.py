# importing pandas as pd
import pandas as pd

# list of name, degree, score
nme = ["aparna", "pankaj", "sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]

# dictionary of lists
dict = {'name': nme, 'degree': deg, 'score': scr}

df = pd.DataFrame(dict)
print(df)
#      name  degree  score
# 0  aparna     MBA     90
# 1  pankaj     BCA     40
# 2  sudhir  M.Tech     80
# 3   Geeku     MBA     98


df2 = df.sort_values('score', ascending=False, ignore_index=True)
df2.index += 1
print(df2)

#      name  degree  score
# 1   Geeku     MBA     98
# 2  aparna     MBA     90
# 3  sudhir  M.Tech     80
# 4  pankaj     BCA     40
