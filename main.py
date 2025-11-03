from pyscript import display, document

subjects = ['Math', 'English', 'Science', 'Filipino', 'VE,' 'SS', 'ICT', 'TLE', 'PEH', 'CAT']
units = (1, 2, 3, 4, 5)

display(subjects[0], target='subjectA')
display(subjects[1], target='subjectB')
display(subjects[2], target='subjectC')
display(subjects[3], target='subjectD')
display(subjects[4], target='subjectE')
display(subjects[5], target='subjectF')
display(subjects[6], target='subjectG')
display(subjects[7], target='subjectH')
display(subjects[8], target='subjectI')
display(subjects[9], target='subjectJ')


def finalizedinfo(e):

    fname = document.getElementById('firstnameinput').value
    lname = document.getElementById('lastnameinput').value

    gradeA = units(4) * int(document.getElementById('inputA').value)
    gradeB = units(4) * int(document.getElementById('inputB').value)
    gradeC = units(3) * int(document.getElementById('inputC').value)
    gradeD = units(2) * int(document.getElementById('inputD').value)
    gradeE = units(0) * int(document.getElementById('inputE').value)
    gradeF = units(2) * int(document.getElementById('inputF').value)
    gradeG = units(1) * int(document.getElementById('inputG').value)
    gradeH = units(1) * int(document.getElementById('inputH').value)
    gradeI = units(0) * int(document.getElementById('inputI').value)
    gradeI = units(1) * int(document.getElementById('inputJ').value)

    totalgrades = int['gradeA', 'gradeB', 'gradeC', 'gradeD', 'gradeE','gradeF', 'gradeG', 'gradeH', 'gradeI', 'gradeJ']

    gradesadded = sum(totalgrades)
    unitsadded = units(4)*2 + units(3) + units(2)*2 + units(3)*1 + units(0)*2

    genave = gradesadded / unitsadded

    display(f"Name: {fname},{lname}", target="fullname")
    display(f"Gen Ave: {genave}", target="average")



    
