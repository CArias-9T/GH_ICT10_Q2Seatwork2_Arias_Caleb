from pyscript import display, document

#main required data

subjects = ['Math', 'English', 'Science', 'Filipino', 'VE', 'SS', 'ICT', 'TLE', 'PEH', 'CAT']
units = (5, 5, 4, 3, 3, 2, 2, 2, 1, 1)


def finalizedinfo(e):

    # name input, for full name info

    fname = document.getElementById('firstnameinput').value
    lname = document.getElementById('lastnameinput').value

    # collect data for grades

    gradeA = int(document.getElementById('inputA').value)
    gradeB = int(document.getElementById('inputB').value)
    gradeC = int(document.getElementById('inputC').value)
    gradeD = int(document.getElementById('inputD').value)
    gradeE = int(document.getElementById('inputE').value)
    gradeF = int(document.getElementById('inputF').value)
    gradeG = int(document.getElementById('inputG').value)
    gradeH = int(document.getElementById('inputH').value)
    gradeI = int(document.getElementById('inputI').value)
    gradeJ = int(document.getElementById('inputJ').value)

    # multiply data by respective units (in the tuple)

    fgradeA = units[0] * gradeA
    fgradeB = units[1] * gradeB
    fgradeC = units[2] * gradeC
    fgradeD = units[3] * gradeD
    fgradeE = units[8] * gradeE
    fgradeF = units[4] * gradeF
    fgradeG = units[5] * gradeG
    fgradeH = units[6] * gradeH
    fgradeI = units[9] * gradeI
    fgradeJ = units[7] * gradeJ

    # puts the data in a list

    totalgrades = [fgradeA, fgradeB, fgradeC, fgradeD, fgradeE, fgradeF, fgradeG, fgradeH, fgradeI, fgradeJ]

    # to then be added here

    gradesadded = sum(totalgrades)
    unitsadded = sum(units)

    # final formula, to get general average

    genave = gradesadded / unitsadded

    # displays for all data

    display(f"Name: {fname} {lname}", target="fullname")
    display(f"{subjects[0]}: {gradeA}", target='subjectA')
    display(f"{subjects[1]}: {gradeB}", target='subjectB')
    display(f"{subjects[2]}: {gradeC}", target='subjectC')
    display(f"{subjects[3]}: {gradeD}", target='subjectD')
    display(f"{subjects[4]}: {gradeE}", target='subjectE')
    display(f"{subjects[5]}: {gradeF}", target='subjectF')
    display(f"{subjects[6]}: {gradeG}", target='subjectG')
    display(f"{subjects[7]}: {gradeH}", target='subjectH')
    display(f"{subjects[8]}: {gradeI}", target='subjectI')
    display(f"{subjects[9]}: {gradeJ}", target='subjectJ')
    display(f"Gen Ave: {genave}", target="output")





    
