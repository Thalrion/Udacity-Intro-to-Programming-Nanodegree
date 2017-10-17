# Project Overview

This project was build for the **Udacity-Intro-to-programming Nanodegree Course**.

Given a database containing 3 tables and more than a million datapoints, the
challange was to right `postgresQL`-queries in `Python` (using the `Python-DB-API`)
to answer 3 questions.

This *documentation*  tells you:

- what steps you need to take to reproduce the results
- which views were created to get to the results
- which code-design decisions were made


## Prerequisites

Basic/advanced Python & SQL-Knowledge is preferable to reproduce the results.

### Installation step 1: Virtual Machine

This project makes use of Linux-based virtual machine (VM) to run a SQL database server and a web app that uses it.

To manage the VM, you need to install following first:

- [Vagrant](https://www.vagrantup.com/downloads.html)
- [Virtual Machine](https://www.virtualbox.org/wiki/Downloads)

### Installation step 2: Terminal

To run & execute the code, you need a Unix-style terminal on your computer.
If you are a Mac/Linux user, your regular terminal program will do just fine. On Windows, Udacity recommends using the **Git Bash terminal** that comes with the [Git software](https://git-scm.com/downloads).

### Installation step 3: Download VM configuration

After all necessary installations have been made, you need to download
the **VM configuration** given from the Udacity-Team by either:

- Fork and clone the [github repository](https://github.com/udacity/fullstack-nanodegree-vm).
- Download the [FSND-Virtual-Machine.zip](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip).

### Installation step 4: VM configuration

After downloading the **VM configuration**, change to this directory in your
terminal and find the `vagrant`-file. :

```bash
Mats@Mats-PC MINGW64 ~
$ cd Downloads/

Mats@Mats-PC MINGW64 ~/Downloads
$ cd fsnd-virtual-machine

Mats@Mats-PC MINGW64 ~/Downloads/fsnd-virtual-machine
$ cd FSND-Virtual-Machine/

Mats@Mats-PC MINGW64 ~/Downloads/fsnd-virtual-machine/FSND-Virtual-Machine
$ ls
README.md  vagrant/

Mats@Mats-PC MINGW64 ~/Downloads/fsnd-virtual-machine/FSND-Virtual-Machine
$ cd vagrant/

Mats@Mats-PC MINGW64 ~/Downloads/fsnd-virtual-machine/FSND-Virtual-Machine/vagrant
$ vagrant up

```
When you are in the right directory, type in `vagrant up` to start the **VM**.
This will cause **Vagrant** to download the **Linux operating system** and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

### Installation step 5: Log into the VM

When you get your terminal back, just run `vagrant ssh` to log into the
installed **linux VM**.

### Installation step 6: Download the Data

After successfully connecting to the **VM**, you should see something like this:

```bash
Mats@Mats-PC MINGW64 ~/Downloads/fsnd-virtual-machine/FSND-Virtual-Machine/vagrant
$ vagrant ssh
Welcome to Ubuntu 16.04.3 LTS (GNU/Linux 4.4.0-75-generic i686)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

0 packages can be updated.
0 updates are security updates.


The shared directory is located at /vagrant
To access your shared files: cd /vagrant
Last login: Mon Oct 16 12:02:20 2017 from 10.0.2.2
vagrant@vagrant:~$
```
Now it's time to download the [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) on which the querries are running.

Unzip the folder and pull the file called `newsdata.sql` into the `vagrant`
folder-directory.

To create and connect to the database, you finally need to run following command:

`psql -d news -f newsdata.sql`

It will connect you to the database and execute the `SQL` commands in the downloaded file, creating tables and populating them with data.

## Create Views

Congrats, your setup is ready to go! Before executing the `python` code,
there is a little bit more to do in the terminal.

Because the asked querries were kind of complicated, I had to create `views`
of the `tables` to build the reporting tool. They are not contained in the
original database, so you need to create them first by just copy&paste the code into your terminal:

After creating a `view`, your terminal should output `CREATE VIEW`.

#### View 1

```sql
create view articles_count as
select title, count(*) as num
from log, articles
where log.path = '/article/' || articles.slug
group by title
order by num desc;
```

#### View 2

```sql
create view articles_count_author as
select articles.title, articles_count.num, articles.author
from articles, articles_count
where articles_count.title = articles.title;
```
#### View 3

```sql
create view views_per_day as
SELECT log.time::date, count(*) from log group by log.time::date;
```

#### View 4

```sql
create view errors_per_day as
SELECT log.time::date, count(*) from log where status = '404 NOT FOUND' group by log.time::date;

```

After creating all `views`, please log out by pressing `CTRL+D`.

## Execute code

The written `Python`-code can be found [here](https://github.com/Thalrion/Udacity-Intro-to-Programming-Nanodegree/tree/master/Project4).

Make sure that this file is located into the `vagrant`-directory before
executing it:

```bash
vagrant@vagrant:/vagrant$ python reporting_tool.py
```

When everything worked out just fine, it should display the
output documented in [this text file](https://github.com/Thalrion/Udacity-Intro-to-Programming-Nanodegree/blob/master/Project4/output.txt).

## Design decisions

This part is especially dedicated to the **Udacity-Reviewer**.

The `Python`-code is splitted into 4 parts:

1. A shebang-line to indicate `python`-version / importing neccessary packages (i.e. `psycopg2` to access `postgresQL`-database)
2. All 3 **querries** with explaining comments as string-text on the top. They are ordered according to the task they try to solve. Please note that this part only contains the **querries** in string-format - they do not actually do a **query** to the _database_
3. The 3rd part contains 3 _functions_. The 1st one takes in a **query-textstring** (documented on the top) and outputs the results as a **list**. 2nd and 3rd _function_ are used to display the results a little bit nicer.
4. The last part combines _Part 1_ + _Part 2_ and execute the _functions_ with
the appropiate _input_ to print out the **results**.
