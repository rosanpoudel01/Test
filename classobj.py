class Student:
    # def __init__(self, name, address):
    #     self.name = name
    #     self.address = address

    def details(self):
        print(f"Name is {self.name} i live in {self.address}")


s = Student("Ram", "Ktm")
s.details()


class Student:
    def __init__(self, _id, name, rollno):
        self._id = _id
        self.name = name
        self.rollno = rollno
        self.totalattendence = 0

    def view_attendance(this):
        # the paramenter name is not required to be same as in init function
        print(f"Total attendence of {this.name} = {this.totalattendence}")

    def __str__(self):
        return f"{self.rollno}.{self.name}"

    def __repr__(self):
        return f"{self.rollno}.{self.name}"


s = Student(1, "Ram", 12)
s.view_attendance()

students = []
for i in range(1, 6):
    name = input("Enter Name: ")
    rollno = input("Enter Roll no: ")
    s = Student(i, name, rollno)
    students.append(s)

print(students)


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def profile(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")


class Student(Person):
    def __init__(self, name, address, roll):
        super().__init__(name, address)
        self.roll = roll

    def profile(self):
        super().profile()
        print(f"Roll No: {self.roll}")


class Staff(Person):
    def __init__(self, name, address, designation):
        super().__init__(name, address)
        self.designation = designation

    def profile(self):
        super().profile()
        print(f"Designation: {self.designation}")


st = Student("Ram", "Chitwan", 13)
st.profile()
s = Staff("Hari", "Ktm", "Manager")
s.profile()
