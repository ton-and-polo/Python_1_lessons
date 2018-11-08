# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Person:
    def __init__(self, first_name, patronymic, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__patronymic = patronymic
    @property
    def full_name(self):
        return "{} {} {}".format(self.__first_name, self.__patronymic, self.__last_name)

class Subject:
    def __init__(self, subject_name):
        self.subject_name = subject_name


class Teacher(Person):
    def __init__(self, first_name, last_name, patronymic, teacher_subject):
        Person.__init__(self, first_name, last_name, patronymic)
        self.teacher_subject = teacher_subject

class Student(Person):
    def __init__(self, first_name, last_name, patronymic, mother, father):
        Person.__init__(self, first_name, last_name, patronymic)
        self.mother = mother
        self.father = father
    def get_parents(self):
        return [self.mother.full_name, self.father.full_name]


class Class:
    def __init__(self, number, char):
        self.number = number
        self.char = char
        self.teachers = []
        self.students = []
    @property
    def class_name(self):
        return "{}{}".format(self.number, self.char)
    # add teacher in teachers list
    def add_teacher(self, *args):
        for i in args:
            self.teachers.append(i)
    # add student in students list
    def add_student(self, *args):
        for i in args:
            self.students.append(i)

class School:
    def __init__(self):
        self.classes = []
    # add class in school
    def add_class(self, *args):
        for i in args:
            self.classes.append(i)

    def get_classes(self):
        return [i.class_name for i in self.classes]

    def get_students(self, className):
        students = [i.students for i in self.classes if i.class_name == className]
        return [i.full_name for i in students[0]]

    def get_subjects(self, studentName):
        classes =[]
        for i in self.classes:
            for student in i.students:
                if student.full_name == studentName:
                    classes.append(i)
        result = []
        for i in classes[0].teachers:
            result.append(i.teacher_subject.subject_name)
        return result

    def get_parent(self, studentName):
        class_students = [i.students for i in self.classes if studentName in [j.full_name for j in i.students]]
        students = [i for i in class_students[0] if studentName == i.full_name]
        return students[0].get_parents()

    def get_teachers(self, className):
        teachers = [i.teachers for i in self.classes if i.class_name == className]
        return [i.full_name for i in teachers[0]]


# Parents:
mother1 = Person("Irina", "Vladimirovna", "Ivanova")
father1 = Person("Kiril", "Sergeevich", "Ivanov")

mother2 = Person("Olga", "Viktorovna", "Simirnova")
father2 = Person("Aleksandr", "Ivanovich", "Simirnov")

mother3 = Person("Anastasia", "Sergeevna", "Marushchak")
father3 = Person("Yaroslav", "Vladimirovich", "Marushchak")

mother4 = Person("Daria", "Viktorovna", "Kononetc")
father4 = Person("Victor", "Alekseevich", "Kononetc")

# Students:
student1 = Student("Aleksey", "Kirilovich", "Ivanov", mother1, father1)
student2 = Student("Galina", "Ivanovna", "Simirnova", mother2, father2)
student3 = Student("Feodor", "Yaroslavovich", "Marushchak", mother3, father3)
student4 = Student("Uliana", "Viktorovna", "Kononetc", mother4, father4)

# Subjects:
math_subject = Subject("Math")
physics_subject = Subject("Physics")
english_subject = Subject("English")
p_e_subject = Subject("Physical Education")
history_subject = Subject("History")

# Teachers:
math_teacher = Teacher("Oleg", "Viktorovich", "Aginsky", math_subject)
history_teacher = Teacher("Anton", "Nikitich", "Chugunov", history_subject)
physics_teacher = Teacher("Ilia", "Aleksandrovich", "Kozlov", physics_subject)
english_teacher = Teacher("Galina", "Konstantinovna", "Krichevskaya", english_subject)
p_e_teacher = Teacher("Ivan", "Ivanovich", "Archangelsky", p_e_subject)

# Classes:
class1 = Class(9, "A")
class2 = Class(8, "B")
class3 = Class(2, "G")

# Add teachers to the classes
class1.add_teacher(math_teacher, p_e_teacher, physics_teacher, english_teacher)
class2.add_teacher(math_teacher, physics_teacher)
class3.add_teacher(p_e_teacher, history_teacher, english_teacher)

# Add students to the classes
class1.add_student(student1)
class1.add_student(student2)
class2.add_student(student3)
class3.add_student(student4)

# School:
school = School()
school.add_class(class1, class2, class3)




# Resut:
class_name = "2G"
student = "Galina Ivanovna Simirnova"


print("School classes:", school.get_classes())
print("Students in \"{}\" class:".format(class_name), school.get_students(class_name))
print("Subjects of student ({}):".format(student), school.get_subjects(student))
print("Parents of student ({}):".format(student), school.get_parent(student))
print("\"{}\" class teachers:".format(class_name), school.get_teachers(class_name))
