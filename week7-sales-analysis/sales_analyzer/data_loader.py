import pandas as pd

class DataLoader:

    def load_data(self, file_path):
        try:
            df = pd.read_csv(file_path)
            print("Data loaded successfully!")
            return df
        except Exception as e:
            print("Error:", e)
            return None