from sales_analyzer.data_loader import DataLoader
from sales_analyzer.data_cleaner import DataCleaner
from sales_analyzer.analyzer import SalesAnalyzer
from sales_analyzer.visualizer import Visualizer
from sales_analyzer.reporter import Reporter

loader = DataLoader()

df = loader.load_data(
    "data/raw/sales_data.csv"
)

cleaner = DataCleaner()

df = cleaner.clean_data(df)

analyzer = SalesAnalyzer()

analyzer.basic_stats(df)

analyzer.category_sales(df)

analyzer.top_products(df)

visual = Visualizer()

visual.category_chart(df)

report = Reporter()

report.export_report(df)

print("\nAnalysis Complete!")