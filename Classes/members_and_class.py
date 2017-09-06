class OurClass():

    def __init__(self, name, location, members=None, size=0):

        self.name = name
        self.location = location
        self.size = size
        # self.questions_asked = []

        if members != None:
            self.members = members
        else:
            self.members = []

        self.check_if_at_capacity()


    def get_num_lines_coded(self):

        num_code_lines = 0

        for member in self.members:
            num_code_lines += member.num_lines_coded

        return num_code_lines


    def get_num_questions_asked(self):

        num_questions = 0

        for member in self.members:
            num_questions += len(member.questions_asked)

        return num_questions


    def add_class_members(self, member):

        if not self.check_if_at_capacity():
            self.members.append(member)
            self.size += 1
        else:
            print 'Capacity Reached!!'


    def check_if_at_capacity(self):

        if self.size >= 31:
            self.at_capacity = True
            return True

        self.at_capacity = False
        return False


class Member():

    def __init__(self, name, hair_color, birthdate):

        self.name = name
        self.hair_color = hair_color
        self.birthdate = birthdate

        self.questions_asked = []
        self.lines_of_code = []
        self.num_lines_coded = 0
        self.coding_level = "Beginner"


    def add_question_asked(self, question):

        self.questions_asked.append(question)


    def add_coded_line(self, coded_line):

        self.lines_of_code.append(coded_line)
        self.num_lines_coded += 1
        self.get_coding_level()


    def get_coding_level(self):

        if self.num_lines_coded > 100 and self.num_lines_coded <= 1000:
            self.coding_level = "Novice"

        elif self.num_lines_coded > 1000 and self.num_lines_coded <= 10000:
            self.coding_level = "Intermediate"

        elif self.num_lines_coded > 10000:
            self.coding_level = "Master"



#Main block Test

member1 = Member("Jane", "brown", "12/12/84")
member2 = Member("Alex", "brown", "12/12/84")
member3 = Member("Cody", "brown", "12/12/84")

lst_members = [member1, member2, member3]

for member in lst_members:
    member.add_question_asked("How do I do this?")
    member.add_question_asked("What does this mean?")
    member.add_question_asked("Will I get a job?")

    member.add_coded_line("print hello world")
    member.add_coded_line("return lst")

new_class = OurClass("python class", "austin", lst_members, 3)

print "All members of the class asked {} questions".format(new_class.get_num_questions_asked())
print "All members of the class wrote {} lines of code".format(new_class.get_num_lines_coded())

# while new_class.check_if_at_capacity() is False:
#
#     for index in range(1,33):
#         new_class.add_class_members(str(index))
#
# print new_class.members
