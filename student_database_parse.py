database_filename = "c.csv"
output_filename = "index.html"

classes_by_teacher = {}
students_by_class = {}
books_by_class = {}
price_by_book = {}

with open(database_filename, 'r') as database_file:
    for line in database_file:
        line = line.strip().split(',')
        if line[0] == 'teacher':
            classes_by_teacher[line[1]] = []
            for i in range(2,len(line)):
                if len(line[i]) > 0:
                    classes_by_teacher[line[1]].append(line[i])
        elif line[0] == 'roster':
            students_by_class[line[1]] = []
            for i in range(2,len(line)):
                if len(line[i]) > 0:
                    students_by_class[line[1]].append(line[i])
        elif line[0] == 'materials':
            books_by_class[line[1]] = []
            for i in range(2,len(line)):
                if len(line[i]) > 0:
                    books_by_class[line[1]].append(line[i])
        elif line[0] == 'book':
            price_by_book[line[1]] = line[2]
database_file.close()

school_roster = []
for c in students_by_class:
    for s in students_by_class[c]:
        if len(s)>1:
            school_roster.append(s)
    school_roster = list(set(school_roster))
school_roster.sort()

class_list = []
for c in students_by_class:
    class_list.append(c)
class_list.sort()

classes_by_student = {}
for s in school_roster:
    classes_by_student[s] = []
    for c in students_by_class:
        if s in students_by_class[c]:
            classes_by_student[s].append(c)

#books_by_student = {}
#for s in school_roster:
    #books_by_student[s] = []
    #for c in classes_by_student[s]:
        #for b in books_by_class[c]:
            #books_by_student[s].append(b)

#owed_by_student = {}
#for s in school_roster:
    #owed_by_student[s] = 0
    #for b in books_by_student[s]:
        #owed_by_student[s] += float(price_by_book[b])

#for s in owed_by_student:
    #print(F'{s}     {owed_by_student[s]}')

with open(output_filename, 'w') as output_file, open('html_a.html','r') as htmla: 
    for line in htmla: 
             output_file.write(line)
    output_file.write("\n")
output_file.close()
htmla.close()

with open(output_filename, 'a') as output_file:
    for c in class_list:
        line = f'<div class="class-button" id="{c}">&emsp;<button class="button" onclick="ChooseClass(\'{c}\')">{c}</button>&emsp;<br></div>\n'
        output_file.write(line)
    output_file.write("\n")
output_file.close()

with open(output_filename, 'a') as output_file, open('html_b.html','r') as htmlb: 
    for line in htmlb: 
             output_file.write(line)
    output_file.write("\n")
output_file.close()
htmlb.close()

with open(output_filename, 'a') as output_file:
    for s in school_roster:
        line = f'<table class="students" id="{s}" cellpadding=0 cellspacing=0><tr><td>{s}</td><td><input type="radio" id="{s}-present" name="{s}" value="Present"></td><td><input type="radio" id="{s}-late" name="{s}" value="Late"></td><td><input type="radio" id="{s}-excused" name="{s}" value="Excused"></td><td><input type="radio" id="{s}-unexcused" name="{s}" value="Unexcused"></td><td><input hidden type="radio" id="{s}-x" name="{s}" value="-" checked></td></tr></table>\n\n'
        output_file.write(line)
    output_file.write("\n")
output_file.close()

with open(output_filename, 'a') as output_file, open('html_c.html','r') as htmlc: 
    for line in htmlc: 
             output_file.write(line)
    output_file.write("\n")
output_file.close()
htmlc.close()

with open(output_filename, 'a') as output_file:
    line = f'var schoolRoster = ['
    for s in school_roster:
        line += f'\'{s}\', '
    line += f']\n'
    output_file.write(line)
    output_file.write("\n")
output_file.close()

with open(output_filename, 'a') as output_file, open('html_d.html','r') as htmld: 
    for line in htmld:
             output_file.write(line)
    output_file.write("\n")
output_file.close()
htmld.close()

with open(output_filename, 'a') as output_file:
    
    for t in classes_by_teacher:
        line = f'\t}} else if (teacherNameSent==="{t}") {{\n'
        output_file.write(line)
        line = f'\t\tclasses = ['
        for c in classes_by_teacher[t]:
             line += f'\'{c}\', ' 
        line += "];\n"
        output_file.write(line)
output_file.close()

with open(output_filename, 'a') as output_file, open('html_e.html','r') as htmle: 
    for line in htmle:
             output_file.write(line)
    output_file.write("\n")
output_file.close()
htmle.close()
