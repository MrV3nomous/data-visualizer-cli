import argparse

from analytics import auto_visualize, dataset_explorer, insight_engine, generate_dashboard
from loader import load_csv, preview_dataset, dataset_summary, detect_columns, detect_missing
from analytics import auto_visualize
from charts import line_chart, bar_chart, scatter_chart, histogram
from plotly_charts import interactive_scatter
from report import generate_pdf_report


def interactive_menu():

    df = None

    while True:
        print("\nDATA VISUALIZER")
        print("1 Load dataset")
        print("2 Preview dataset")
        print("3 Dataset summary")
        print("4 Detect columns")
        print("5 Missing values")
        print("6 Generate chart")
        print("7 Advanced analytics")
        print("8 Interactive chart")
        print("9 Auto visualization")
        print("10 Generate PDF report")
        print("11 Dataset Explorer")
        print("12 Insight Engine")
        print("13 Generate Dashboard")
        print("0 Exit")

        choice = input("Select option: ")

        if choice == "1":
            path = input("CSV path: ")
            df = load_csv(path)

        elif choice == "2":
            preview_dataset(df)

        elif choice == "3":
            dataset_summary(df)

        elif choice == "4":
            detect_columns(df)

        elif choice == "5":
            detect_missing(df)

        elif choice == "6":
            x = input("X column: ")
            y = input("Y column: ")
            scatter_chart(df, x, y)

        elif choice == "7":
            auto_visualize(df)

        elif choice == "8":
            x = input("X column: ")
            y = input("Y column: ")
            interactive_scatter(df, x, y)

        elif choice == "9":
            auto_visualize(df)

        elif choice == "10":
            generate_pdf_report()

        elif choice == "11":
            dataset_explorer(df)

        elif choice == "12":
            insight_engine(df)

        elif choice == "13":
            generate_dashboard(df)

        elif choice == "0":
            break


def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument("csv", nargs="?", help="Dataset path")

    parser.add_argument("--auto", action="store_true")

    parser.add_argument("--report", action="store_true")

    return parser.parse_args()


def main():

    args = parse_args()

    if args.csv:

        df = load_csv(args.csv)

        if args.auto:
            auto_visualize(df)

        if args.report:
            generate_pdf_report()

    else:

        interactive_menu()


if __name__ == "__main__":
    main()
