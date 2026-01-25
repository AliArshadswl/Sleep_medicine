import pandas as pd
from sklearn.metrics import cohen_kappa_score

# Load Excel
file_path = ""E:\test\sleep\Final_results.xlsx""
human1 = pd.read_excel(file_path, sheet_name="human1")
human2 = pd.read_excel(file_path, sheet_name="human2")
