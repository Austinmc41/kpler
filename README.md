# kpler assignment

Backend steps
 
1. cd into `backend`
 
2. run `docker compose build`

3. run `sudo docker compose run web python manage.py migrate` 

4. run `docker compose up` (can take a second to get going, may need to ctrl + c for the first time 
and rerun command)


Unit tests

There is basic test coverage for getting and posting vessels
These tests can be viewed in tests/test_views.py & and tests/test_models.py

command to run tests: `sudo docker compose run web python manage.py test` 



Frontend steps

1. cd into `frontend/frontend`

2. run `docker compose build`

3. run `docker compose up`
