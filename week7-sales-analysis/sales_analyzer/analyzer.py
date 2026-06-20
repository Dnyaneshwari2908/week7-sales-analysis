class SalesAnalyzer:

    def basic_stats(self, df):

        print("\nBASIC STATISTICS")
        print("-" * 30)

        print("Total Sales:", df["total_amount"].sum())

        print("Average Sale:",
              round(df["total_amount"].mean(), 2))

        print("Total Orders:",
              len(df))

        print("Unique Customers:",
              df["customer_id"].nunique())

        print("Unique Products:",
              df["product_id"].nunique())

    def category_sales(self, df):

        print("\nSALES BY CATEGORY")
        print("-" * 30)

        print(df.groupby("category")
              ["total_amount"]
              .sum()
              .sort_values(ascending=False))

    def top_products(self, df):

        print("\nTOP CATEGORIES")

        print(df["category"]
              .value_counts())