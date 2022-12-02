class Student:
    #ФИО, пол, возраст, телефон, почта, курс, оценки
    def __init__(self, number, fio, gender, age, tel, email, group, kurs, marks):
        self.number = int(number)
        self.fio = fio
        self.gender = gender
        self.age = int(age)
        self.tel = tel
        self.email = email
        self.group = group
        self.kurs = int(kurs)
        self.marks = marks



    # Метод добавления оценок для студента.

    # Метод перевода студента на курс выше.
    def increase_kurs(self):
        self.kurs += 1

    # Перехват функции print, когда она преобразует свое значение в строку
    def __str__(self):
        return f"{'Студент' if self.gender=='м' else 'Студентка'}: {self.fio}" \
               f" в группе {self.group} на {self.kurs} курсе, номер студ.билета: {self.number}"

    # Предусмотреть операции сравнения студентов по курсу.
    def __lt__(self, other):
        return self.kurs < other.kurs

stud_1 = Student(1, 'Кагарманов Родион Радикович', 'м', '20', '890478747976', 'test@test,ru', '195ИС', '2',
                 {"отлично" : 5, "хорошо" : 3, "удовлетворительно" : 2, "неудовлетворительно" : 0})
print(stud_1)
stud_2 = Student(1, 'Иванова Альбина Ивановна', 'ж', '18', '890478747976', 'test@test,ru', '205ИС', '1',
                 {"отлично" : 5, "хорошо" : 3, "удовлетворительно" : 2, "неудовлетворительно" : 0})
print(stud_2)
print(stud_2 < stud_1)
Student.increase_kurs(stud_2)
Student.increase_kurs(stud_2)
print(stud_2)
print(stud_2 < stud_1)