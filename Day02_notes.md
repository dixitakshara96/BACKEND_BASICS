# Topics 

### 1. Request Anatomy 
* Request Line
* Headers
* Body

### 2. Response Anatomy
* Status Line
* Headers
* Body
<hr>
<br>

## Request Anatomy : The actual context inside a Request send by the Client to the Server.

### 1. Request Line 
* HTTP METHOD : GET, POST, PUT, PATCH, DELETE
* URL/PATH : Exact Location of the resource where we want server to perform operations or give us response of 
* HTTP VERSION 
<br>

### 2. Headers : this has the complete details like 
* HOST : Receiver
* Content-Type : which content format type (json, xml) you are sending to the server
* Accept-Type : which content format type you like server to send (json, xml)
* Authorization : Authentication and all 
<br>

### 3. Body : actual content you want to send in the format you have mentioned in Content-Type 
* We don't write body when we Retrieve data (GET) or Remove Data (DELETE)
<hr>
<br> 

## Response Anatomy : The content inside the Response which Server send back to Client.

### 1. Status Line 
* HTTP VERSION
* Status Code  (2XX, 3XX, 4XX , 5XX families)
* Reason (according to Status code)

### 2. Headers
* Content-Type : server also tells which content format type it is sending back to the Client 

### 3. Body : actual Content send by the Server to the Client in the format type mention in Content-Type

<hr>


## Tiny Exercise

### 1. Construct a HTTP Request :
want to create a new student

` POST /students HTTP/1.1 ` // Request Line<br>
` HOST : example.come` // headers<br>
` Content-Type : application/json` // headers <br>
` Authorization : Bearer abc123` // headers<br>
` { "name" : "ABC" , "marks" : 85}` // body

### 2. Client wants to retrieve data :
` GET /students/101 HTTP 1.1` // Request Line <br>
` HOST : example.com` // header <br>
` Accept-Type : application/json` //header <br>
//no body 
<hr>


