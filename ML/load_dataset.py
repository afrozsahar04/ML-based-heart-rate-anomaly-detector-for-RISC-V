import pandas as pd
fn = list(uploaded.keys())[0]  # filename uploaded
df = pd.read_csv(fn)
print("Columns found:", df.columns.tolist())
display(df.head(30))
