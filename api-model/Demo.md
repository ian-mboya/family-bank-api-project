Interacting with the API
<p> FastAPI offers a simplified way of interacting with APIs via SwaggerUI. This is a rich web page with features that make testing out APIs built on FastAPI much simpler.<p>

<h2> Getting Started <h2>
<p> Ensure that your server is running on this address "http://127.0.0.1:8000"</p>
<br>
<p> To use SwaggerUI just add /docs to the the url in the address bar. "http://127.0.0.1:8000/docs"</p>
<br>
This is what you should see in your web browser.
  
![image](https://github.com/ian-mboya/family-bank-api-project/assets/68651784/0ca2d4db-0a21-4318-96f0-c39b63b4fc28)


As mentioned, FastAPI's SwaggerUI provides a friendly interface to API developers. As we can see, it is able to identify our API endpoints and Schema. 

<h2>Making POST request</h2>
<p>1. We have our database created in Postgres. We are going to make a POST request that has the following request body that sends the particular fee details to our database.</p>


![image](https://github.com/ian-mboya/family-bank-api-project/blob/main/assets/POST%20request%20empty.png?raw=true)

<p>2. These are our values that we need appended onto our database.</p>

![POST success](https://github.com/ian-mboya/family-bank-api-project/assets/68651784/cacae12f-49ca-4e2e-b6a7-1469e03ec785)


<p>3. After pressing execute, we should see the following 200 success code showing that the data has been successfully been sent to the database </p>


<p>4. Here is the updated value in our database.
<p>Before</p>
![Database unapdated](https://github.com/ian-mboya/family-bank-api-project/assets/68651784/60efec03-45cd-4250-9b1c-d5b6fdbc7004)

<p>After</p>
![database updated](https://github.com/ian-mboya/family-bank-api-project/assets/68651784/57b5d880-c986-4bc7-88a1-ac1c7b1c2870)


We have covered making POST requests in our API.


<h2> Making GET requests </h2>
<p>We have two endpoints that allow us to get a single student's payment history via student id and another one that is able to query all students' payment history</p>

<p> We will begin by getting a single student's payment history.</p>







