months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May":"05",
    "June":"06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}
def main():
    while True:
        try:
            date = input("Date:")
            if "/" in date:
                month, day, year = date.split("/")
            elif "," in date:
                date = date.replace(",", "")
                month, day, year = date.split()
                month = months[month]
            else:
                continue
     
            month = int(month) 
            day = int(day)
            year = int(year) 
            if month >12 or day >31:
                continue
            break
        except (ValueError, KeyError):
            continue
    print(f"{year}-{month:02}-{day:02}")
main()

# Algorithm:
# 1 input date in month day year
# 2 format 2/5/2001 or sept 4 2020
# 3 check month value from list
# 4 check month <=12 and date <=31
# 5 output date in yyyy-mm-dd 
