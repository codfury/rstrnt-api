# rstrnt-api

A RESTful api for Restaurant orders.

This api created using django rest framework library.

To start using the api,

<ul>

<li>Navigate to inside the folder and then create a new virtual environment to run the project

Run this to create the env:

```
python3 -m venv env
```
Then run in your bash terminal to activate the environment

```
source env/bin/activate
```
You can also follow this <a href='https://www.python.org/downloads/'>site</a> for more details.

<li>After that navigate to the eshop folder where there is *requirements.txt* and using the command

```
pip install requirements.txt
```
<li>Create superuser (to gain admin rights) by using command.


```
python manage.py createsuperuser
```
</ul>

Then after these we are good to go for using the APIs.

In postman to use the endpoints which requires authentication please generate a token using login/ endpoint and then insert the generated token as Key:Authorization and Value: Token <YOUR_GENERATED_TOKEN_HERE> in headers of your request.
