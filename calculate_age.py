import datetime


def calculate_age(birth_year, birth_month, birth_day):
    today = datetime.date.today()
    birth_date = datetime.date(birth_year, birth_month, birth_day)
    
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    
    return age

def main():
    birth_year = int(input("Enter the birth year: "))
    birth_month = int(input("Enter the birth month: "))
    birth_day = int(input("Enter the birth day: "))
    
    age = calculate_age(birth_year, birth_month, birth_day)
    
    print(f"The age is {age} years.")

if __name__ == "__main__":
    main()