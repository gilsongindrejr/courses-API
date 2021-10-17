# Courses-API

Project made to learn Django Rest Framework.\
This project is a movie rating system, admins can add movies and users can add reviews.\
The API returns the movies and ratings.

# Running backend server

#### Clone this repository
```
$ git clone <https://github.com/gilsongindrejr/courses-API.git>
```

#### Access the project folder
```
$ cd school
```

#### Activate the virtual enviroment
```
$ source venv/bin/activate
```

#### Install requirements
```
$ pip install -r requirements.txt
```

#### Migrate the database
```
$ python manage.py migrate
```

#### Run server
```
$ python manage.py runserver
```

#### The server will be initiated on port 8000 - access <http://127.0.0.1:8000> 

# Endpoints

The endpoints is the same for API v1 and v2, just need to change the version in the url.

#### Courses

<http://127.0.0.1:8000/api/v1/courses/>

the course id can be passed to retrieve a specific course, like:\
<http://127.0.0.1:8000/api/v1/courses/1/>

To retrieve the course ratings, use:\
<http://127.0.0.1:8000/api/v1/courses/1/ratings/>

And to retrieve a specific rating, use:\
<http://127.0.0.1:8000/api/v1/courses/1/ratings/1/>

#### Ratings

<http://127.0.0.1:8000/api/v1/ratings/>

The rating id can be passed to retrieve a specific rating, like:\
<http://127.0.0.1:8000/api/v1/rating/1/>

# Testing

The tests was made using pytest.


#### Run tests and show coverage
```
$ pytest --cov
```

#### Run tests and create coverage html page
```
$ pytest --cov --cov-report=html
```

Access htmlcov folder
```
$ cd htmlcov/
```

Run python http server
```
$ python -m http.server
```

Access the server on <http://127.0.0.1:8000> 
