# kpler assignment

Backend steps
 
1. cd into `backend`
 
2. run `docker compose build`

3. run `sudo docker compose run web python manage.py migrate` (on first try may need to run again if gives port error)

4. run `docker compose up` (can take a second to get going, may need to ctrl + c for the first time 
and rerun command)


Run Script

(make sure python 3 is installed)
1. cd into csv_script
2. run `python post_vessels.py`
3. wait
4. see file.txt for output (can use prettfier tool to increase readabiity and ease of finding errors w/ cmd + f) 

Unit tests

There is basic test coverage for getting and posting vessels
These tests can be viewed in tests/test_views.py & and tests/test_models.py

command to run tests: `sudo docker compose run web python manage.py test` 



Frontend steps

1. cd into `frontend/frontend`

2. run `docker compose build`

3. run `docker compose up`

4. open 'http://localhost:8080/'


Note about Docker: If you don't Docker install the latest version from 'https://www.docker.com/get-started/'
Please use `docker compose` instead of `docker-compose`, the latter may work but I have done testing with the former. 
https://docs.docker.com/compose/#compose-v2-and-the-new-docker-compose-command -> more about compose
