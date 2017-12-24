To Run the application:
-----------------------

1. Specify your database name and database user name under the 'DATABASES'
	section settings.py.
2. Create new migrations:
	- python3 manage.py makemigrations
3. Apply the migrations:
	- python3 manage.py migrate
4. Create super user 
    - python3 manage.py createsuperuser
5. start the application:
	- python manage.py runserver
6. Access the application in the browser using the url:
	- http://127.0.0.1:8000/
	
	
Accessing the Rest Api Endpoints using curl:
--------------------------------------------

1. Generte the authentication using the curl command by specifying 
	user name and password:
	
	curl --request POST 
		 --url http://127.0.0.1:8000/api-token/ 
		 --header 'content-type: application/json' 
		 --data '{"username": "user1", "password": "pass@123"}'
	
2. Retrieve all the orders by using the authentication token:

	curl -H "Content-Type: application/json" 
     	 -H "Authorization: JWT token_value" 
	 	 -X GET  http://127.0.0.1:8000/GetOrdersApi/
	 	 
3. Create a new order by using the authentication token and by
	supplying the data:
	
	curl -X POST http://127.0.0.1:8000:8000/CreateOrderApi/  
		-d '{"customer":'1',"product":'1',"comments":"Its a comment"}' 
		-H "Content-Type: application/json" 
		-H "Authorization: JWT token_value"
	    
 
    
 