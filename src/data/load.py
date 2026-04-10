import kagglehub
from kagglehub import KaggleDatasetAdapter

#Set the path for the file
file_path = 'data/raw'

df = kagglehub.dataset_load(KaggleDatasetAdapter.PANDAS, "rohitrox/healthcare-provider-fraud-detection-analysis", file_path)

print("First 5 records:", df.head())