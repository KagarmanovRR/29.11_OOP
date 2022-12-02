class Student:
    #ФИО, пол, возраст, телефон, почта, курс, оценки
    def __init__(self, number, fio, gender, age, tel, email, group, kurs, marks):
        self.number = number
        self.fio = fio
        self.gender = gender
        self.age = age
        self.tel = tel
        self.email = email
        self.group = group
        self.kurs = kurs
        self.marks = marks

    # Предусмотреть операции сравнения студентов по курсу.

    # Метод добавления оценок для студента.

    # Метод перевода студента на курс выше.
    def increase_kurs(self):
        self.kurs += 1

    # Перехват функции print, когда она преобразует свое значение в строку
    def __str__(self):
        return f"{'Студент' if self.gender=='м' else 'Студентка'}: {self.fio}" \
               f" в группе {self.group} на {self.kurs} курсе, номер студ.билета: {self.number}"



stud_1 = Student(1, 'Кагарманов Родион Радикович', 'м', '30', '890478747976', 'test@test,ru', '195ИС', '3',
                 {"отлично" : 5, "хорошо" : 3, "удовлетворительно" : 2, "неудовлетворительно" : 0})
print(stud_1)