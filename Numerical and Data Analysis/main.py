import numpy as np
import pandas as pd

years_exp = np.array([1, 3, 5, 7, 10, 12, 15]) 
salaries = np.array([[50, 60, 70, 75], [80, 90, 100, 110]])

print("Years of Experience:", years_exp)
print("Salary Matrix:\n", salaries)

zeros_array = np.zeros((2, 2))
ones_array = np.ones((2, 3))

identity_3x3 = np.eye(3)
print("\n3x3 Identity Matrix:\n", identity_3x3)

print("\n--- 2. ARRAY OPERATIONS ---")
print("Years + 5:", years_exp + 5)
print("Years * 2:", years_exp * 2)
print("Years / 2 (Division):", years_exp / 2) # "Try It" subtraction/division
print("Years - 1 (Subtraction):", years_exp - 1)

sample1 = np.array([1, 2, 3])
sample2 = np.array([4, 5, 6])
dot_result = np.dot(sample1, sample2)
print("Dot Product:", dot_result)

print("\n--- 3. INDEXING & SLICING ---")
print("First year of experience:", years_exp[0])
print("First two elements of first row salaries:", salaries[0, :2])
print("Last year of experience:", years_exp[-1])

reversed_years = years_exp[::-1]
print("Reversed Experience Array:", reversed_years)

print("\n--- 4. RESHAPING ---")
reshaped_exp = np.arange(1, 7).reshape(2, 3)
print("Reshaped 2x3 Matrix:\n", reshaped_exp)

print("Flattened Array:", reshaped_exp.flatten())
print("Transposed Matrix:\n", reshaped_exp.T)

print("\n--- 5. STATISTICAL OPERATIONS ---")
print("Mean experience:", np.mean(years_exp))
print("Std deviation:", np.std(years_exp))
print("Max salary:", np.max(salaries), "| Min salary:", np.min(salaries))

angles = np.array([0, np.pi/4, np.pi/2])
print("Sine of angles:", np.sin(angles))

print("\n--- 6. PANDAS ANALYSIS ---")
data = np.random.randint(1, 50, size=(5, 3))
df_data = pd.DataFrame(data, columns=['X', 'Y', 'Z'])

df_data['Sum_XY'] = df_data['X'] + df_data['Y']
print("DataFrame with Sum_XY column:\n", df_data)

df_data.to_csv('sample_data.csv', index=False)
print("\nFile 'sample_data.csv' has been created successfully.")

print("\nSummary Statistics:\n", df_data.describe())

print("\n--- ACTIVITY COMPLETED ---")
