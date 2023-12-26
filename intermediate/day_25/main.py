import pandas as pd
squirrel_df = pd.read_csv('squirrel_data.csv')

color_counts = squirrel_df['Primary Fur Color'].value_counts()
results_df = pd.DataFrame({'Fur Color': color_counts.index, 'count': color_counts.values})

print(results_df)
results_df.to_csv('results.csv')

