# ETITANGO

Repository of etitango site :dancer:

**Guide for Devs**

1. Run docker-compose up using the enviroment file which you want to run:
  - :whale: For develoment: `docker-compose up`
  - :whale: For testing: `docker-compose up -f docker-compose.test.yml`
  - :whale: for production: `docker-compose up -f docker-compose.prod.yml`
  * If you need to rebuild the container, use the `--build` flag.
  * Check the manual for more options: `docker-compose up --help`

2. Connect to the site using http://localhost

### FAQs

  * Q: Which changes are persistents, which are not?
    A: Any modified file in etitango will change the container too, because the etitango's folder is mounted as a bind volume. But if you change another one,like the `docker-entrypoint.sh`, or the `Dockerfiles`, you will need to restart the containers with the `--build` flag.

  * Q: My new app can't migrate!
    A: For avoid problems, migrations must be explicit. Add your new app to the `docker-entrypoint.sh` file.

  * Q: How i can modified the variables in enviroment?
    A: All variables are setted in the secret `.env` file. **:skull: NEVER PUSH IT :skull:** to the repository. Keep in mind that variables are declare as "strings", so may you need to convert that as "int", "bool", etc. inside the app.

  * Q: Can I inspect the database?
    A: Of course you can. Login inside the database's container using this command:
      `sudo docker container run etitango_db_dev_1 bash`
      then run `mysql` command as usual.

  * Q: I got a error as "address is already in use", what happened?
    A: Probably you are running some service in your host machine. nginx & apache2 use to run in port 80, mysql at 3306. May you want to stop that services before start the containers, but if you need them for another thing, change the ports at your docker-compose.yml file. Just dont push them, please. 

### Where learn more about docker?

Check this [video](https://www.youtube.com/watch?v=5z2kYFG3OfY&list=PLrb1e2Mp6N_tXQryuDVzOq4SLQKqVv1uz) to learn more about docker in development environments.

## Ready for commit?
Please check this list before commit:

1. You must be working in your branch, but first:
  - :octocat: Merge the develoment branch into your branch, so you can be sure that you are not breaking what.
  - :octocat: Work hard :coffee:
  - :octocat: When you finish, please be sure to pull and merge develoment again into your branch.
  - :octocat: If your branch works well after that, you can merge to the develoment branch.
  - :octocat: Push to github