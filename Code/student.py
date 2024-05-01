class Student:

    def __init__(self, id, name = ""):
        self.id = id
        self.name = name

    # getter
    @property
    def id(self):
        return self._id
    # setter
    @id.setter
    def id(self, id):
        self._id = id

    # getter
    @property
    def name(self):
        return self._name

    # setter
    @name.setter
    def name(self, name):
        if name != "":
            self._name = name
        else:
            raise ValueError("Invalid name")

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}"

    @classmethod
    def get(cls):
        id = input("Enter ID: ")
        name = input("Enter Name: ").strip().title()
        return cls(id, name)

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()

