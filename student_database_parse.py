database_filename = "c.csv"
output_filename = "index_temp.html"

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

classes_by_student = {}
for s in school_roster:
    classes_by_student[s] = []
    for c in students_by_class:
        if s in students_by_class[c]:
            classes_by_student[s].append(c)

books_by_student = {}
for s in school_roster:
    books_by_student[s] = []
    for c in classes_by_student[s]:
        for b in books_by_class[c]:
            books_by_student[s].append(b)

owed_by_student = {}
for s in school_roster:
    owed_by_student[s] = 0
    for b in books_by_student[s]:
        owed_by_student[s] += float(price_by_book[b])

for s in owed_by_student:
    print(F'{s}     {owed_by_student[s]}')

with open('first.txt','r') as firstfile, open('second.txt','w') as secondfile: 
    for line in firstfile: 
             secondfile.write(line)

with open(output_filename, 'w') as output_file:
    
output_file.close()