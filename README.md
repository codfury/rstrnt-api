# rstrnt-api

A RESTful api for Restaurant orders.

This api is created using django rest framework library.

To start using the api,

<ul>

<li>Navigate to inside the folder and then either create a new virtual environment to run the project or use the existing one named as "myvenv".

Run this to create the env:

```
python3 -m venv env
```
Then run in your bash terminal to activate the environment

```
source env/bin/activate
```


<li>After that navigate to the restaurant folder where there is *requirements.txt* and use the command

```
pip install requirements.txt
```
<li>Create superuser (to gain admin rights) by using command.


```
python manage.py createsuperuser
```

<li>Start the server using this command.


```
python manage.py runserver
```
</ul>

Then after these we are good to go for using the APIs.

In postman or in browser to use the endpoints which requires authentication please generate a token using login/ endpoint and then insert the generated token as Key:Authorization and Value: Token <YOUR_GENERATED_TOKEN_HERE> in headers of your request, if using chrome then can also use the <a href=https://chrome.google.com/webstore/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj> chrome extension</a> for the same.
