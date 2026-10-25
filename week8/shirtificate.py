from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, name):
        super().__init__(orientation="P", format="A4")
        self.add_page()
        self.image("shirtificate.png", 10, 65, 190)
        self.set_y(15)
        self.set_font("helvetica", style="B", size=45)
        self.cell(0, 30, "CS50 Shirtificate", border=0, align="C")
        self.set_text_color(255, 255, 255)
        self.set_font("helvetica", style="B", size=23) 
        self.set_y(130)
        self.cell(0, 10, text=f"{name} took CS50", align="C")


def main():
    name = input("Name: ")
    pdf = PDF(name)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
