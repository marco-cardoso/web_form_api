## Technologies used

<ul>
    <li>Flask</li>
    <li>MongoDB/PyMONGO</li>
    <li>Unittest library (tests available in the tests folder)</li>
</ul>

## Requirements

1. At least docker v19.03.12
2. At least docker-compose v1.26.2

## How to execute it ?

    docker-compose up --build
    
## Available endpoints

After starting the app you can test the following endpoints :

Store a WEB form 

    POST: http://127.0.0.1:8080/data
    
     Request body example :
        {  
            "background_colour": "234 234 234",
            "background image": "path_to_the_image",
            "height": 30,
            "background colour": "234 234 234",
            "border radius": 1,
            "body text": "Hello World"
        }
        
    If sucessfully created, the endpoint will return the new WEB form id.



Get a web form by ID 

    GET:  http://127.0.0.1:8080/data/<form_id>

    Get a WEB form object.

## How to query data using the project data architecture ?

As MongoDB is a NoSQL database it's much simpler to query the data from the WEB forms, being 
only necessary to use the method '*find*' passing the wished values. To increase the performance of 
the queries, it's also possible to create indexes for the most used fields. 

For more details check : https://docs.mongodb.com/manual/indexes/

In order to find documents which have a specific string inside a text variable it's possible to use
 the operators $text and $search.

https://docs.mongodb.com/manual/text-search/

It's also possible to use them with PyMongo.

## How to scale the current project ?

First of all, remove the data layer from the docker compose. Ideally, the best alternative
would be to use a cloud provider service, such as Amazon DocumentDB.  Also, configure a service 
like AWS ECS with a load balancer.



