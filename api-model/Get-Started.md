<h1 align="center" id="title">PulsePay API (Description)</h1>

![readme thumbnail](https://github.com/ian-mboya/family-bank-api-project/blob/main/assets/family-bank-api-project.png)

<p id="description">This simple API, simulates bank transaction process between a school and its merchant account. The API is integrated into a proposed payment app and it has the ability to perform payment transaction and fetch the records from the merchant database to the user. In an ideal integration, the client can specify who gets access to what records. However in this particular simulation, we can query various data depending on the specified endpoint.</p>

<br>

<p id="description">The API (PulsePay API) has been built in Python and FastAPI framework. FastAPI framework allows for fast development of APIS and its ecosystem allows for concise code by developers making it a favourable framework when developing scalable APIs for different use cases.</p>

<p id="description">For the Database i used PostgreSQL. PostgreSQL is a powerful opensource relational database provides excellent relational mapping especially for real time applications. <a href="https://www.postgresql.org/download/">Follow the official guide Postgres website to install postgres rdb locally on your machine before starting this project demo.</a> I have also provided a link to the Queries for setting up the relaions for this web app. <a href="">QUERY text file</a></p>


<h2>🛠️ Installation Steps:</h2>
<h3> Local installation on Windows, Mac or Linux Pc<h3>
<p>1. Ensure you have python installed, preferrably Python 3.10 <p>
<p>2. Clone this repository by running</p>

```
git clone https://github.com/ian-mboya/family-bank-api-project.git
```

<p>3. After cloning into your machine, install python virtual environment in your project directory by running</p>

```
pip install virtualenv
```

<p>4. In the same directory activate virtual environment by running</p>

```
.venv\Scripts\Activate.ps1
```

<p>5. Install the python dependencies using pip</p>

```
pip install requirements.txt
```

<p>6. Finally to start the server, we run this command</p>

```
uvicorn main:app --reload
```
you should see this in your terminal, congratulations your API server is running.

![image](https://github.com/ian-mboya/family-bank-api-project/blob/main/assets/API%20server%20Boot%20Success.png?raw=true)



<h2> After BootUp </p>
<p> Now that your server is up and running, head over to the specified url indicated on your terminal "http://127.0.0.1:8000"

You should be able to see this on your web browser. A success message from our API

![image](https://github.com/ian-mboya/family-bank-api-project/blob/main/assets/web%20api%20success%20message.png?raw=true)


<h1>Head over to the project demo using this link</h1>

<h2><a href="api-model/Demo.md">API demo</a></h2>












