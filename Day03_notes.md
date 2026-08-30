# TOPICS 

### 1. URL
### 2. Router and Routing
### 3. Endpoints
<hr>

## URL 
* Uniform Resource Locator 
* where and what resource whants to access.

#### https://example.com/students  
* https: - PROTOCOL
* example.com - DOMAIN
* students - PATH or we can say that URL PATH 

* Protocol : the method the browser uses to connect (http or https)
* Domain and SubDomain
* Path : the specific folder or file location on the server
* Query Parameters : optional codes startes with a question mark used to filter data
<hr>

## ROUTER : decide which view/handler should receive the request.

* ROUTE : it is the RULE that maps a URL Path to the code/handler/view that should process the request.
* ROUTING : it is the process of matching an incoming request to the code responsible for handling it.
* Analogy : Router is like marriage bureau wali aunty that does matching of which boy (request path) is suitable for which girl (Handler/ Endpoint).
<HR>

## ENDPOINTS (API Endpoints)
* HTTP Method + URl Path
* specific operation is being performed when we get a particular request 
<HR>

## Path Parameters 
* /students/{id} : here {id} can be any +ve integer and it is a path parameter
<HR>

## Query Parameters 
* /students?department=CSE&year=2 : here /students is the path and department and year are query parameters.
* used for 
#### Filtering
#### Searching
#### Sorting
#### Pagination 

* Example : GET /students?page=2
<hr>

## PRACTICAL CHALLENGE
#### Design API Endpoints for the following
1. Get all students : GET /students
2. Get one student: GET /students/{id}
3. Create a student: POST /students
4. Update a student: PUT /students/{id}
5. Delete a student: DELETE /students/{id}
6. Get a students belonging to CSE: GET /students?department=CSE
7. Search students by name: GET /students?name=ABC
8. Get page 2 of students: GET /students?page=2

* don't need to put query parameters in quotes ""
* {id} here means any +ve integer
<hr>

## KEY CONCEPTS 
* Client
* Request
* HTTP
* URL
* Path
* Query Parameters
* Headers
* Body
* Router
* Route
* Endpoint
* View
* Response
* Status Code
<hr>

## QNA
1. GET /students/42 and PUT /students/53 : both have the same path (/students)
2. GET /students/43 and PUT /students/35 : both have the same path but not same HTTP Method and hence Different ENDPOINT.
<HR>

## IMPORTANT POINT 

#### 1. REQUEST ANATOMY :
* Request Line : ` HTTP METHOD` | `URL Path` | `HTTP Version`
* Headers
* Blank Line : this line indicates that the request structure is completed
* Body : (optional)

#### 2. RESPONSE ANATOMY :
* status line : `HTTP Version` | `Status Code` | `Reason`
* Headers 
* Blank Line :  same as request.
* Body : (optional)

