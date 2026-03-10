import seaborn as sns
import matplotlib.pyplot as plt
from utils import save_matplotlib


def correlation_heatmap(df):

    corr = df.corr(numeric_only=True)

    fig = plt.figure(figsize=(10,6))

    sns.heatmap(corr, annot=True, cmap="coolwarm")

    plt.title("Correlation Heatmap")

    save_matplotlib(fig, "correlation_heatmap")


def pair_plot(df):

    sns.pairplot(df.select_dtypes(include="number"))

    plt.savefig("charts/pairplot.png")

    print("Saved chart -> charts/pairplot.png")


def correlation_insights(df):

    corr = df.corr(numeric_only=True)

    pairs = corr.unstack()

    pairs = pairs.sort_values(kind="quicksort", ascending=False)

    print("\nTop correlations:")

    printed = set()

    for (a,b), value in pairs.items():

        if a == b:
            continue

        if (b,a) in printed:
            continue

        print(f"{a} ↔ {b} : {value:.2f}")

        printed.add((a,b))

        if len(printed) > 5:
            break


def auto_visualize(df):

    print("\nAUTOMATIC ANALYSIS")

    dataset_explorer(df)

    correlation_heatmap(df)

    pair_plot(df)

    correlation_insights(df)

    insight_engine(df)

    generate_dashboard(df)



def dataset_explorer(df):

    print("\nDATASET EXPLORER")
    print("----------------")

    rows, cols = df.shape

    print(f"Rows: {rows}")
    print(f"Columns: {cols}")

    numeric = df.select_dtypes(include="number").columns.tolist()
    categorical = df.select_dtypes(include="object").columns.tolist()

    print("\nNumeric Columns:")
    for c in numeric:
        print(" -", c)

    print("\nCategorical Columns:")
    for c in categorical:
        print(" -", c)

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if len(missing) > 0:
        print("\nMissing Values:")
        print(missing)
    else:
        print("\nNo missing values detected.")

    print("\nBasic Statistics:")
    print(df.describe())

def insight_engine(df):

    print("\nINSIGHTS")
    print("--------")

    corr = df.corr(numeric_only=True)

    if corr.empty:
        print("Not enough numeric data for insights.")
        return

    pairs = corr.unstack().sort_values(ascending=False)

    seen = set()

    print("\nStrongest correlations:")

    for (a, b), val in pairs.items():

        if a == b:
            continue

        if (b, a) in seen:
            continue

        print(f"{a} ↔ {b} : {val:.2f}")

        seen.add((a, b))

        if len(seen) >= 5:
            break

    # Outlier detection
    print("\nOutlier detection:")

    for col in df.select_dtypes(include="number").columns:

        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)

        iqr = q3 - q1

        outliers = df[(df[col] < q1 - 1.5 * iqr) |
                      (df[col] > q3 + 1.5 * iqr)]

        if len(outliers) > 0:
            print(f"{col} contains possible outliers.")



import plotly.express as px
import plotly.io as pio
import os


def generate_dashboard(df):

    os.makedirs("charts", exist_ok=True)

    numeric = df.select_dtypes(include="number").columns

    if len(numeric) < 2:
        print("Not enough numeric data for dashboard.")
        return

    x = numeric[0]
    y = numeric[1]

    scatter = px.scatter(df, x=x, y=y, title="Scatter Plot")

    hist = px.histogram(df, x=x, title="Distribution")

    corr = df.corr(numeric_only=True)

    heatmap = px.imshow(corr,
                        text_auto=True,
                        title="Correlation Heatmap")

    dashboard_path = "charts/dashboard.html"

    with open(dashboard_path, "w") as f:

        f.write("<h1>Data Visualizer Dashboard</h1>")

        f.write(pio.to_html(scatter, full_html=False))
        f.write(pio.to_html(hist, full_html=False))
        f.write(pio.to_html(heatmap, full_html=False))

    print("Dashboard created ->", dashboard_path)
