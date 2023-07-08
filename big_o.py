import pandas as pd
import numpy as np

import time
start = time.time()
# Set the random seed for reproducibility
np.random.seed(42)

# Create a DataFrame with random values
df = pd.DataFrame(np.random.randn(1000000, 5), columns=['A', 'B', 'C', 'D', 'E'])

# Apply the lambda function to add 10 to each row of each column
df = df.apply(lambda x: x + 10)

print(df)
end = time.time()
print(end - start)