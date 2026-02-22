df.columns = [c.strip() for c in df.columns]  # trim spaces
# Try to map possible variants
mapping = {}
for c in df.columns:
    cl = c.lower().replace('_',' ').replace('-',' ')
    if 'age' in cl: mapping[c] = 'Age'
    elif 'gender' in cl or 'sex' in cl: mapping[c] = 'Gender'
    elif 'heart' in cl and ('rate' in cl or 'hr' in cl): mapping[c] = 'Heart rate'
# apply mapping
df = df.rename(columns=mapping)
print("Mapped columns:", df.columns.tolist())

# keep only the three columns
expected = ['Age','Gender','Heart rate']
missing = [x for x in expected if x not in df.columns]
if missing:
    raise ValueError("Missing columns after mapping: " + str(missing))

# drop rows with NaN and convert types
df = df[expected].dropna()
df['Age'] = df['Age'].astype(int)
# convert Gender if it's string like 'M' or 'F'
if df['Gender'].dtype == object:
    df['Gender'] = df['Gender'].str.strip().str.lower().map({'m':1,'male':1,'f':0,'female':0})
df['Gender'] = df['Gender'].astype(int)
df['Heart rate'] = df['Heart rate'].astype(float)

print("Clean data shape:", df.shape)
display(df.head(8))
