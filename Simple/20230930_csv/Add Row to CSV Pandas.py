import pandas as pd
# Create the initial CSV data
rows = [{'A':'Z1', 'B':'Z2', 'C':'Z3'},
        {'A':'ZZ1', 'B':'ZZ2', 'C':'ZZ3'},
        {'A':'ZZZ1', 'B':'ZZZ2', 'C':'ZZZ3'}]

# Create a DataFrame and write to CSV
df = pd.DataFrame(rows)
df.to_csv('my_file.csv', header=True, index=False)
print(df)

# Create another row and append row (as df) to existing CSV
row = [{'A':'X1', 'B':'X2', 'C':'X3'}]
df = pd.DataFrame(row)
df.to_csv('my_file.csv', mode='a', header=False, index=False)
print(df)