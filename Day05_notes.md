# TOPICS
## REST API
## IDEMPOTENT
## PATCH vs PUT
## API Design
## Collection vs Specific Resource

# REST
* Representational State Transfer
* REST is an architectural style for designing network APIs around resources and standard HTTP operations.
* RESOURCE : the thing with which your API work with (URLs)
* HTTP Method : tells us the operation performed on the resource
* ` The URL identifies the resource.`
* ` The HTTP method describes the action.`
### API vs REST API
* API : The URL identifies the resource. The HTTP method describes the action.
* REST API : is a type of API designed according to REST architectural principles, commonly using HTTP.

# Idempotent
* simply basha mei kahun aise HTTP Method jisse baar baar same url dene par server ke state ko koi farak nhi padhta (mujhe farak nhi padta).
* Example the GET method .

# PATCH vs PUT
* PATCH is like only changing some info of a student
* PUT : whereas it is liek completely changing the resource.

# API Design 
* HTTP Method + URL Path : GET /students/54✅
* not /get/students NOPE ❌

# Collection vs Specific Resource
* Collection : GET /students <br>
GET /students?id=43  (this also going to give the collection)😁
* Specific Resource : GET /students/43

