import pandas as pd
import numpy as np

import time
start = time.time()
# Set the random seed for reproducibility
np.random.seed(42)

# Create a DataFrame with random values
df = pd.DataFrame(np.random.randn(1000000, 5), columns=['A', 'B', 'C', 'D', 'E'])

# Iterate through the DataFrame and add 10 to each row of each column
for index, row in df.iterrows():
    df.loc[index] = row + 10

print(df)
end = time.time()
print(end - start)