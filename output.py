import pandas as pd
import numpy as np
import time

start = time.time()

np.random.seed(42)
df = pd.DataFrame(np.random.randn(1000000, 5), columns=['A', 'B', 'C', 'D', 'E'])
df += 10

print(df)

end = time.time()
print(end - start)