from pyscript import display, document

def generate_message(event):
    #  strings
    name: str = document.getElementById("name").value
    age: str = document.getElementById("age").value
    school: str = document.getElementById("school").value

    #  string with \t and \"
    profile: str = f"""
 Student Profile
Name   : \"{name}\"
Age    : {age}\t
School {school} ||

 Notes :
{name} is currently {age} years old and studies at {school}.
This information was gathered through input fields and displayed using
a multiline string in Python via PyScript.
"""

    # Clears previous message before showing new one
    display(profile, target="output", append=False)

