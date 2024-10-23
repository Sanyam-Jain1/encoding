import pandas as pd # type: ignore
#Creating a dataframe of Phones (without names) , ID - SIZE - COLOUR
df = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Price': [299, 349, 259, 279, 399, 329, 289, 359, 199, 419],
    'Colour': ['Red', 'Blue', 'Green', 'Yellow', 'Black', 'Grey', 'Red', 'Green', 'Blue', 'Yellow']
})

#Makes a list of object type columns (which are to be encoded)
object_cols = []
for col in df.columns:
    if df[col].dtype=='object':
        object_cols.append(col)

items = df['Colour'].unique()

tup_items = tuple(items)
dic = {tup_items[x]: x+1 for x in range(0,len(items))}

for i in range(0,len(df)):
    a=df.loc[i, 'Colour']
    df.loc[i, 'Colour'] = dic[a]
    
print(df)   

