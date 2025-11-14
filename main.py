from pyscript import document, display

def general_weighted_average(e):
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value
    social_studies = float(document.getElementById("social_studies").value)
    math = float(document.getElementById("math").value)
    science = float(document.getElementById("science").value)
    english = float(document.getElementById("english").value)
    physical_education = float(document.getElementById("physical_education").value)
    filipino = float(document.getElementById("filipino").value)
    
    units_subject = (5, 3, 2, 1)

    weighted_sum = (social_studies * 5 + math * 5 + science * 5 + english * 5   + filipino* 3 + physical_education * 1)
    total_units = sum(5 * 3) + 3 + 2 + 1
    gwa = weighted_sum / total_units
    
    
    
    subjects = ["Social Studies", "Math", "Science", "English", "Filipino", "Physical Education"]
    summary = f''' {subjects[0]}: {social_studies:.0f}
    {subjects[1]}: {math:.0f}
    {subjects[2]}: {science:.0f}
    {subjects[3]}: {english:.0f}    
    {subjects[4]}: {filipino:.0f}
    {subjects[5]}: {physical_education:.0f}'''


    display(f'Name: {first_name} {last_name}', target="student_info")
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output')

