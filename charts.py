import matplotlib.pyplot as plt
import seaborn as sns
from utils import save_matplotlib


def line_chart(df, x, y):

    fig = plt.figure()
    plt.plot(df[x], df[y])
    plt.title(f"{y} vs {x}")
    plt.xlabel(x)
    plt.ylabel(y)

    save_matplotlib(fig, f"line_{x}_{y}")


def bar_chart(df, x, y):

    fig = plt.figure()
    sns.barplot(x=df[x], y=df[y])
    plt.title(f"{y} vs {x}")

    save_matplotlib(fig, f"bar_{x}_{y}")


def scatter_chart(df, x, y):

    fig = plt.figure()
    plt.scatter(df[x], df[y])

    plt.title(f"{y} vs {x}")

    save_matplotlib(fig, f"scatter_{x}_{y}")


def histogram(df, col):

    fig = plt.figure()

    plt.hist(df[col], bins=30)

    plt.title(f"Distribution of {col}")

    save_matplotlib(fig, f"histogram_{col}")


def boxplot(df, col):

    fig = plt.figure()

    sns.boxplot(x=df[col])

    plt.title(f"Boxplot {col}")

    save_matplotlib(fig, f"box_{col}")


def violinplot(df, col):

    fig = plt.figure()

    sns.violinplot(x=df[col])

    plt.title(f"Violin {col}")

    save_matplotlib(fig, f"violin_{col}")
