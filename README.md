
## Test Assignment #1 - Implementation of Functions and Classes (approximate time - 4 hours):
A. The function takes a set of links as an argument. The links are in the format of links to projects on the githab (for example: https://github.com/miguelgrinberg/Flask-SocketIO, https://github.com/miguelgrinberg/Flask-SocketIO.git). The function should parse the received links and display the names of the git projects themselves in the console. It's worth considering protecting against links "out of format".

B. Implement a function that takes two lists and returns a dictionary (key from the first list, value from the second) ordered by keys. Output the result to the console. The length of the first list should not be equal to the length of the second list. Output the result to the console.

C. Implement the function using the map and lambda methods. The function accepts a list of elements (consisting of strings and digits) and returns a new list, with the condition that if the list element was a string then the text "abc_" should be added to the beginning of the string and "_cba" to the end of the string. If the item was int - then its value must be squared. The result should be printed to the console.

D. Implement a function that measures the time to execute 100 queries to the address: http://httpbin.org/delay/3. The queries must be executed asynchronously. It is allowed to write auxiliary functions and use third-party libraries. The result of time measurement is printed to the console. The expected time should not exceed 10 seconds.

E. Write a class that accepts text. One method of the class should print to the console the longest word in the text. The second method should output the most frequent word. The third method prints the number of special characters in the text (dots, commas, and so on). The fourth method outputs all palindromes separated by commas.

F.  Write a decorator to the previous class that will output each method's execution time to the console. The result of the assignment must be written in the form of a code file.

## Test Case #2 - write an application in Django (approximate time: 24 hours).
Application description: The application is developed with Django framework, works with PostgreSQL database, has API and web interfaces.

The purpose of the application: the cataloging and structuring of the information on various Web resources.

## 1.	API interface. The application accepts GET and POST requests:

  a.	POST request #1 must contain a link to a web resource in its body. The application must process the received link and decompose it into a protocol, domain, domain zone and path. If the link contains parameters, convert them into a dictionary. The resulting data must be stored in a database table and assigned a unique identification number (uuid). Return the user a response in json format with decomposed data and processing status. If the user did not send the link - inform them about it in the response.
  

  b.	POST request #2 must contain a csv file with a list of links (file format - each new line - one link). All links must be processed according to the sample POST request #1, and processing must be performed in the background. In response, add the overall status of file processing (number of links processed, number of errors, number of links sent to save to the database).
  
  c.	GET request should output all saved links from the database (add the ability to select by domain zone, id, uuid).

  d.	GET request #2 returns the last 20 lines of the log (see step 2).


## 2. Logging. 

The application must log its work with log file rotation when a certain file size (1 megabyte) is reached. It is necessary to log all received requests and responses of the application, as well as information about adding a new record to the database


## 3. Web interface. We need to implement 3 web pages for the application.
Bootstrap5 framework should be used for page makeup. Try to keep the single concept of the pages design.

a.	Page 1. Implement a web page that contains forms to add new web resources to the application. The forms should add web resources both piece by piece and by uploading a CSV file. The format of the CSV file is the same as for the API interface.

b.	Page 2. Implement a web page with a table displaying all links from the database broken down into pages (pagination, 10 items per page). The web page should also contain controls - search by domain name, ability to filter by domain zone, and remove a specific item from the table and database respectively.

## 4. Authorization. 

Add to the application user authorization by tokens, add necessary endpoints and templates for authorization and session completion, functionality described in items 1-3 make available only for authorized users. Log authorization, session termination and unauthorized access attempts.

## 5. Distribution and Containerization.
The application code should be packaged in a docker container and run automatically when the container starts up.
