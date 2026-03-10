import os

CHART_FOLDER = "charts"

def ensure_chart_folder():
    if not os.path.exists(CHART_FOLDER):
        os.makedirs(CHART_FOLDER)


def save_matplotlib(fig, name):
    ensure_chart_folder()
    path = f"{CHART_FOLDER}/{name}.png"
    fig.savefig(path)
    print(f"Saved chart -> {path}")
