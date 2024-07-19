class SchoolJournal :

    def __init__ (self, subject, student) :
        
        self.subject = subject
        self.student = student 
        self.grade_list = []

    def grade (self, grade) :
        if grade >= 1 and grade <= 5:
            self.grade_list.append (grade)

    def printer (self) :
        print (self.subject)
        print (self.student)
        print (self.grade_list)

    def final_grade (self) :
        final_grade = (sum (self.grade_list)) / (len (self.grade_list))
        print (final_grade)

student_1 = SchoolJournal ('math', 'John')
student_1.grade (4)
student_1.grade (3)
student_1.grade (5)
student_1.printer ()
student_1.final_grade ()