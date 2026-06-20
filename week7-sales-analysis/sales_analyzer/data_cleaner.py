class DataCleaner:

    def clean_data(self, df):
        df = df.drop_duplicates()

        df["order_date"] = df["order_date"].astype("datetime64[ns]")

        return df