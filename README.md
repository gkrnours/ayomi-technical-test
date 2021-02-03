# ayomi-technical-test
basic django app running on docker


## Start the app
TL;DR:
`make`

Long explanation:
Calling `make` on its own will call the `start` target which have two dependencies. First 
`artifacts/build_backend` will trigger a build of the backend if the requirements.txt file have changed more recently than the file `artifacts/build_backend`. This take care of installing all the dependencies for the django application. Secondly, the target `artifacts/db` will trigger a database migration, making sure your local django installation have access to all the table required for its model. Then django will be started in the background.

## Logging
Logs can be read in real time using the command `docker-compose logs --tail=99 -f backend`.