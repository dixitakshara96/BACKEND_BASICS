method = input("Enter Method: ").upper()

path = input("Enter path: ").lower()

path_component = path.split("/")


for path_parameter in path_component :
    if path_parameter.isdigit() :
        global student_id ;
        student_id = path_parameter

print(path_component)

        



endpoint = method + " " + path

if (endpoint == "GET /students") :
    print("---All Students---")
    print("Ram")
    print("Shyam")
    print("Sita")
    print("Radha")

elif (endpoint == "POST /students") :
    print("Student Data Entity Created Successfully")

elif (endpoint == f"GET /students/{student_id}") :
    print("Shiva")
 
else :
    print("Invalid Input")
