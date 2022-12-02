class Student:
    #ФИО, пол, возраст, телефон, почта, курс, оценки
    def __init__(self, number, fio, gender, age, tel, email, kurs, marks):
        self.number = int(number)
        self.fio = fio
        self.gender = gender
        self.age = int(age)
        self.tel = tel
        self.email = email
        self.kurs = int(kurs)
        self.marks = marks

    # Метод добавления оценок для студента.

    # Метод перевода студента на курс выше.
    def increase_kurs(self):
        self.kurs += 1

    # Перехват функции print, когда она преобразует свое значение в строку
    def __str__(self):
        return f"{'Студент' if self.gender=='м' else 'Студентка'}: {self.fio}" \
               f" на {self.kurs} курсе, номер студ.билета: {self.number}"

    # Предусмотреть операции сравнения студентов по курсу.
    def __lt__(self, other):
        return self.kurs < other.kurs
    def __le__(self, other):
        return self.kurs <= other.kurs
    def __eq__(self, other):
        return self.kurs == other.kurs

#Методы: вывод всех
#студентов группы. Вывод всех мальчиков/ девочек группы. Предусмотреть операции
#сравнения по количеству студентов в группе.
class Group:
    #Группы – содержат студентов; Атрибуты: название, номер.
    def __init__(self, title, nomer, students=None):
        self.title = title
        self.nomer = int(nomer)
        if students is None:
            students = list()
        self.students = students

    # Добавляем студента в группу
    def append(self, stud):
        self.students.append(stud)

    def __str__(self):
        return f"Группа: {self.nomer}{self.title}, Количество сотрудников: {len(self.students)}"

    # Вывод сотрудников отдела
    def print_students(self):
        for stud in self.students:
            print(stud)

    # Вывод сотрудников отдела в отпуске/не в отпуске
    #def print_employees_on_leave(self, status=True):
    #    for emp in self.employees:
    #        if emp.on_leave == status:
    #            print(emp.number, emp.fio)


stud_1 = Student(1, 'Кагарманов Родион Радикович', 'м', '20', '890478747976', 'test@test,ru', '2',
                 {"отлично" : 5, "хорошо" : 3, "удовлетворительно" : 2, "неудовлетворительно" : 0})
print(stud_1)
stud_2 = Student(1, 'Иванова Альбина Ивановна', 'ж', '18', '890478747976', 'test@test,ru', '1',
                 {"отлично" : 5, "хорошо" : 3, "удовлетворительно" : 2, "неудовлетворительно" : 0})
print(stud_2)
print(stud_2 < stud_1)
Student.increase_kurs(stud_2)
print(stud_2 == stud_1)
Student.increase_kurs(stud_2)
print(stud_2)
print(stud_2 > stud_1)

group_1 = Group('ИС', 195)
group_1.append(stud_1)
group_1.append(stud_2)
print(group_1)
group_1.print_students()