# created a small database
users = { "ABC" : {
    "password" : "123456", "role" : "student" } , "ADMIN" : {
        "password" : "admin123" , "role" : "admin" } }

# here first of all we check if the user already exits in database or not
def login (username, password) :
    if username not in users :
        return "Invalid"

    if users[username] ["password"] != password :
        return "Invalid"

    # if exits then we create a token and assign it to the user
    token = username
    return token


# here we authenticates the user by the token which we had assigned to it earlier. AUTHENTICATION
def authenticate (token) :
    if token in users :
        print("\nAUTHENTICATED")
        print("Token is Assigned")
        return users[token]

    print("\nUNAUTHENTICATED")
    return None


# here we check if the user is allowed/suppose to perform the specific operations by AUTHORIZATION 
def authorize (user, role ) :
    return user["role"] == role


#  here login check
token = login(input("Enter username: "), input("Enter password: "))
print("---LOGIN---")
print(token)


# here authentication check
if token != "Invalid" :
    user = authenticate(token)

#  here authorization check
if token != "Invalid" :
    if user is None :
        print("\n401 Unauthorized")
    
    elif not authorize (user, "admin") :
        print("\nUNAUTHORIZED")
        print("403 Forbidden")
    
    else :
        print("\nAUTHORIZED")
        print("Access Granted")

