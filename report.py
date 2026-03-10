from reportlab.platypus import SimpleDocTemplate, Image, Spacer
import os


def generate_pdf_report():

    files = os.listdir("charts")

    images = [f for f in files if f.endswith(".png")]

    if not images:
        print("No charts to include.")
        return

    elements = []

    for img in images:

        elements.append(Image(f"charts/{img}", width=500, height=300))
        elements.append(Spacer(1,20))

    doc = SimpleDocTemplate("data_report.pdf")

    doc.build(elements)

    print("PDF report created -> data_report.pdf")
