class Reporter:

    def export_report(self, df):

        df.to_excel(
            "data/reports/sales_report.xlsx",
            index=False
        )

        print("Excel report exported.")