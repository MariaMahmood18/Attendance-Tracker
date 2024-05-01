import datetime

class Classes:

    def __init__(self, subject, date):
        self.subject = subject
        self.date = date

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, subject):
        subjects = ["English", "Urdu", "Maths", "Science", "Islamiyat", "Social Studies"]
        if subject in subjects:
            self._subject = subject
        else:
            raise ValueError("Invalid subject name")

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        try:
            self._date = datetime.datetime.strptime(date, r'%Y-%m-%d').date()
        except:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD format.")

    @classmethod
    def get(cls):
        subject = input("Enter subject: ").strip().title()
        date = input("Enter date in (YYYY-MM-DD): ").strip()
        return cls(subject, date)

    def __str__(self):
        return f"Subject: {self.subject}\nDate: {self.date}"

def main():
    clas = Classes.get()
    print(clas)

if __name__=="__main__":
    main()

