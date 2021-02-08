class Make_Questions:
    ''' 
    assumptions are that there is a hierarchy -: easy then intermediate and then hard i.e. the setting of questions should be ordered
    number of questions is fixed in our code 
    you need to give all the solutions consecutively and solutions should be typed
    '''
    def __init__(self, teacher_name, institute_name, contact_number):
        self.teacher_name = teacher_name
        self.institute_name = institute_name
        self.contact_number = contact_number
        self.question_dict = {}
        self.__solutions = {}

    # The instructor needs to input here 4 easy questions 
    def easy_questions(self, easy_question, choice_a, choice_b, choice_c, choice_d, correct_choice, marks_for_easy):
        self.easy_question = easy_question
        self.marks_for_easy = marks_for_easy
        self.question_dict[easy_question] = (choice_a,choice_b,choice_c,choice_d)
        self.__solutions[easy_question] = correct_choice

    # The instructor needs to input here 4 intermediate questions
    def intermediate_questions(self, intermediate_question, choice_a, choice_b, choice_c, choice_d, correct_choice, marks_for_intermediate):
        self.intermediate_question = intermediate_question
        self.marks_for_intermediate = marks_for_intermediate
        self.question_dict[intermediate_question] = (choice_a,choice_b,choice_c,choice_d)
        self.__solutions[intermediate_question] = correct_choice

    # The instructor needs to input here 4 hard questions
    def hard_questions(self, hard_question, choice_a, choice_b, choice_c, choice_d, correct_choice, marks_for_hard):
        self.hard_question = hard_question
        self.marks_for_hard = marks_for_hard
        self.question_dict[hard_question] = (choice_a,choice_b,choice_c,choice_d)
        self.__solutions[hard_question] = correct_choice

    # This is for the instructor to see all the questions and all the solutions that the instructor has put
    # To re-check
    def show_dict(self):
        print(f'{self.teacher_name} - {self.institute_name}')
        print(self.question_dict)
        print('\n')
        print(self.__solutions)

# Child class
class Give_questions(Make_Questions):
    # Teacher may input their information and then should go futher towards making questions
    def __init__(self, teacher_name, institute_name, contact_number):
        super().__init__(teacher_name, institute_name, contact_number)
        print(f'Your test is being taken by {teacher_name} of {self.institute_name}')

    # Here the student will give their information and will then further proceed to the test 
    def student_information(self, student_name, student_email, student_number):
        self.student_name = student_name
        self.student_email = student_email
        self.student_number = student_number
        print(f'Your Information has already been taken kindly procees forward to take your examination, Mr {self.student_name}')
        print(f'If you have any problems with your assessment kindly talk to {self.contact_number}')

    # calling this function students test will start
    def begin_MCQ(self):
        a_ord = 97
        option_ord = 0
        for i in self.question_dict:
            print(chr(a_ord)+")", i,"?")
            a_ord +=1
            option_ord = 0
            for j in self.question_dict[i]:
                option_ord +=1
                print(option_ord,j)
            
    # calling this function takes student's input for per question
    def Mcq_solutions(self):
        self.solution_list = []
        n = len(self.question_dict)
        for i in range(n):
            answer = input('Write your solution -: ')
            print("Your answer for",str(i+1)+")","is",answer)
            self.solution_list.append(answer.strip())

    # calling this function will compute stuent's result 
    def get_marks(self):
        total_marks = 0
        for numbering,i in enumerate(list(zip(self.solution_list,self._Make_Questions__solutions.values()))):
            # print(numbering, i)
            if numbering <= 3 and (i[0] == i[1]):
                total_marks += self.marks_for_easy
            elif numbering <= 7 and (i[0] == i[1]):
                total_marks +=self.marks_for_intermediate
            elif numbering <= 9 and (i[0] == i[1]):
                total_marks += self.marks_for_hard
        print(f'{self.student_name} got a total marks of',total_marks,'out of',(self.marks_for_easy*4)+(self.marks_for_intermediate*4)+(self.marks_for_hard*2))

    # calling this function will give all the wrong answer given by the student and in response to that will give all the ccorrect answer
    def wrong_questions(self):
        total_wrong_questions = 0
        unattempted_question = 0
        for j in list(zip(self.solution_list,self._Make_Questions__solutions.values())):
            if j[0] != j[1]:
                # print(j)
                if j[0] == "":
                    # print(j)
                    unattempted_question+=1
                    print('answer for unattempted question is',j[1])
                else:
                    # print(j)
                    total_wrong_questions+=1
                    print(f'False answer is',j[0],'while the true answer of this question was',j[1])
        print('Total Unattempted questions are -:', unattempted_question)
        print('Total Wrong questions are -:', total_wrong_questions)


# print(help(Make_Questions))


obj1 = Give_questions('Shiva Reddy', 'Edyoda','9999992353')
obj1.easy_questions('Which one of the following river flows between Vindhyan and Satpura ranges', 'Narmada', 'Mahanadi', 'Son', 'Netravati', 'Narmada', 2)
obj1.easy_questions('The Central Rice Research Station is situated in', 'Chennai', 'Cuttack', 'Banglore', 'Quilon', 'Cuttack',2)
obj1.easy_questions('Who among the following headstreams meets the Ganges in last', 'Alaknanda', 'Pindar', 'Mandakini', 'Bhagirathi', 'Bhagirathi', 2)
obj1.easy_questions('The metal whose salts are sensitive to light is', 'Zinc', 'Silver', 'Copper', 'Aluminium', 'Silver', 2)
obj1.intermediate_questions('Pantanjali is well known for the compilation of', 'Yoga Sutra', 'Panchatantra', 'Brahma Sutra', 'Ayurveda', 'Yoga Sutra',3)
obj1.intermediate_questions('River Luni originates near Pushkar and drains into which one of the following', 'Rann of Kachchh', 'Arabian Sea', 'Gulf of Cambay', 'Lake Sambhar', 'Rann of Kachchh',3)
obj1.intermediate_questions('Which one of the following rivers originates in Brahmagiri range of Western Ghats', 'Pennar', 'Cauvery', 'Krishna', 'Tapti', 'Cauvery',3)
obj1.intermediate_questions('The country that has the highest in Barley Production', 'China', 'India', 'Russia', 'France', 'Russia',3)
obj1.hard_questions('Tsunami are not caused by', 'Hurricanes', 'Earthquakes', 'Undersea landslides', 'Volcanic eruptions', 'Hurricanes',5)
obj1.hard_questions('DDT was invented by', 'Mosley', 'Rudolf', 'Karl Benz', 'Dalton', 'Mosley',5)

obj1.student_information('Palash Mukherjee', 'palashmukherjee15@gmail.com', 7290899319)

obj1.begin_MCQ()
obj1.Mcq_solutions()
obj1.wrong_questions()
obj1.get_marks()