import matplotlib.pyplot as plt

class Visualizer:

    def category_chart(self, df):

        category_sales = (
            df.groupby("category")
            ["total_amount"]
            .sum()
        )

        plt.figure(figsize=(8,5))

        category_sales.plot(kind="bar")

        plt.title("Sales By Category")

        plt.tight_layout()

        plt.savefig(
            "data/reports/category_sales.png"
        )

        print("Chart saved.")