# ETITANGO

## Install

**for windows, linux and mac:**

1. Install docker and docker-compose using **[THIS GUIDE](https://docs.docker.com/compose/install/)**

2. Clone our repository:

`git clone https://github.com/schrottgerardo/etitango.git`


### How run docker-compose

**Linux:**
1. Open a shell.
2. Go to the repository path
3. Run docker-compose up, you could prefer usng the -d flag:

 `sudo docker-compose up -d`

**Windows:**
  1. Open the docker desktop which you installed before.
  2. Run docker-compose up:
    `sudo docker-compose up`

    note: may need more examples in windows? check this [video](https://www.youtube.com/watch?v=_9AWYlt86B8).

  3. If everything goes well, the site can be visited at `127.0.0.1:8000`

### FAQs

  * Q: Changes are not persistent?
    A: There are, but if is not working, check the `docker-compose.yml` file, you can decomment the volumes. It gonna mount a persisent volume. But take care of others changes can be not works well if the old volume is still up.

  * Q: My new app can't migrate!
    A: For avoid problems, migrations must be explicit. Add your new app to the `docker-entrypoint.sh` file. Take care of dont keep up the old persistent configurations again.

  * Q: I registred a new user but is not active, what is happening with the validation emails?
  * A: We lost our email account at etitango.com.ar. So please, add your own email credentials
    at .env file.

  * Q: Can I active it from the database?
    A: Of course you can, just connect to it using this command:
      `sudo docker container run etitango_db_1 bash`
      then use `mysql` as usual and active the flag.

  * Q: May I need a administrator account, but there is no admin panel.
    A: There are not admin panel, and even if you active it, it dont work in that way, yet.
      You need to use the `data.perms` functions to generate that kind of account. We gonna improve that feature in the future. For now, if you need use that, please read the docs at data py files.

### Where learn more about docker?

Check this [video](https://www.youtube.com/watch?v=5z2kYFG3OfY&list=PLrb1e2Mp6N_tXQryuDVzOq4SLQKqVv1uz) to learn more about docker in development environments.

## How Commit
Please check this list before commit:

1. You must be working in a branch from developer, not from master.
2. Merge the master into your branch, so you can be sure that you are not breaking what
 actually works.
3. If everything goes well, you can push your branch.
4. Pull request to Master will be check here. Must pass the test.
