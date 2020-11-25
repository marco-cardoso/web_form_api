# Coding Task
Your primary task is to build an API to store and retrieve/query WEB form data, filled by users.
In this task, as in our business, performance and scalability are key. It would be great if the architecture
of the application reflected these constraints.


## Requirements
* Python must be used as a programming language.
* Your API should have a POST /data endpoint that receives a JSON body with the WEB form data to store. 
* A successful request will return a JSON body with the id of the object stored.
* When issued a GET request providing an ID of a form data stored, then the form data should be returned.
* Design the data storage layer to be queried on any field’s values stored(e.g. background image;height;arrow colour).
* README file explaining how to run your service and describing how you would extend the API to store a 
large amount of data and have it queryable. Please try to add as much detail as you can.

## Examples of potential queries
* Get all form fields which are using colour XYZ
* Search for a phrase in the body text

## Notes
* Feel free to choose the technologies/tools from the frameworks/libraries to the data storage.
* It may be easier to give us a link to a git repo when you're done, otherwise a compressed git archive would be fine.


## Examples of WEB forms data.
##### Form A

| Form Field                | Example of Value         | Type  |
| ------------------------- |:------------------------:| -----:|
| background colour         | 234 234 234              | str   |
| background image          | path_to_the_image        | str   |
| height                    | 30                       | int   |
| background colour         | 234 234 234              | str   |
| border radius             | 1                        | int   |
| body text                 | Hello World              | str   |

##### Form B

| Form Field                | Example of Value         | Type  |
| ------------------------- |:------------------------:| -----:|
| arrow colour              | 234 234 234              | str   |
| background image arrow    | path_to_the_image        | str   |
| background image alt text | Image text               | str   |
| content                   | Hello World              | str   |