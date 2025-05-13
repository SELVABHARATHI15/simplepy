import pandas as pd
print("Pandas version:", pd.__version__)

# Test DataFrame creation
test_data = {'col1': [1, 2], 'col2': [3, 4]}
test_df = pd.DataFrame(test_data)
print("\nTest DataFrame:")
print(test_df)