# TOPICS :

### 1. Path Parameters vs Query Parameters
### 2. Handler
### 3. Process Request
### 4. Static vs Dynamic Route


## QNA

### Ans 1: GET /students/25
* HTTP Method — GET
* Path — /students/25 ***** (important)
* Path parameter = 25 [student id]
* Query parameter = No
* Endpoint — GET /student/25 *****(important)


### Ans 2: 
GET /students?department=CSE&year=2
* HTTP Method — get to retrieve / read
* Path — /students
* Path parameter — No
* Query parameter — department = CSE, year = 2

### Difference between:
* GET /students/25<br>
"Give me the student resource whose ID is 25."<br>
<!-- Here, a path parameter is used.This is the right way because path parameters are used to retrieve a specific, single data entity or record.  this is wrong concept both are the correct ways but we convenionally don't do this actually--> 

* GET /students?id=25<br>
"Give me students matching the filter id=25."<br>
The second could conceptually return a collection: <br>
<!-- Here, a query parameter is used.This is not the right way because every student has a unique ID. Query parameters are meant to filter or retrieve a collection of resources matching certain criteria. -->

* Path parameters are generally preferred when identifying a specific resource, while query parameters are generally used for filtering, sorting, searching, pagination, or other optional criteria.

### (Request-Response Flow)Ans:
Client <br>
↓ <br>
HTTP Request<br>
↓<br>
Server<br>
↓<br>
Router<br>
↓<br>
Route Matching<br>
↓<br>
Handler // remove Endpoint because it is only like HTTP Method + Path isn't necessarily a processing step. It's the combination of HTTP method + path through which functionality is exposed. The router uses the incoming request to find the appropriate route/handler.<br>
↓<br>
Process Request<br>
↓<br>
Response<br>
↓
Client<br>

### (Specific Request Flow)Ans: 5
Request: GET /products/500?reviews=true<br>

Client<br>
↓ <br>
Request<br>
↓<br>
Server<br>
↓<br>
Router (Examines: HTTP Method & Path)<br>
↓<br>
Matches:
    GET /products/{product_id}<br>
↓<br>
Extracts:
    product_id = 500<br>
↓<br>
Handler  (Analyzes query & query parameter)Reads query parameter:
    reviews = trues<br>
↓<br>
process request<br>
↓<br>
May query database / perform business logic<br>
↓<br>
Response<br>
↓<br>
Client<br>
<hr>