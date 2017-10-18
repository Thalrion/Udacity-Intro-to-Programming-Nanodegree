#!/usr/bin/env python2.7

import psycopg2
import sys

# Connect to database
DB_name = "news"
db = psycopg2.connect(database=DB_name)
c = db.cursor()

# First query joins 'log' and 'articles' on the according article-slug,
# groups them up by the real title and counts up all logs. It modifies the
# 'article.slug' to have a '/article/' in front of it to match the 'log.path'-
# values.

query1 = """ SELECT title, count(*) AS num
                FROM log, articles
                WHERE log.path = '/article/' || articles.slug
                GROUP BY title
                ORDER BY num DESC
                LIMIT 5; """

# Second query uses a newly created view 'articles_count_author', which was
# querried on another view 'articles_count' (see attached readme.md-file).
# It outputs the name of the author and the summed up views of all articles he/
# she wrote.

query2 = """ SELECT authors.name, sum(num) AS views
                FROM articles_count_author, authors
                WHERE authors.id = articles_count_author.author
                GROUP BY authors.name
                ORDER BY views DESC; """

# Third query uses 2 views: 'views_per_day' and 'errors_per_day'.
# It outputs the every day where the error quote is over 1%.

query3 = """ WITH errors_over_one AS (SELECT views_per_day.time::date,
                ROUND((errors_per_day.count * 1.0 /
                views_per_day.count * 1.0) * 100, 2) as quote
                FROM views_per_day, errors_per_day
                WHERE views_per_day.time = errors_per_day.time)
                SELECT *
                FROM errors_over_one
                WHERE quote > 1.0; """

# All credits for this idea goes to some awesome Udacity-reviewer who reminded
# me to check the case that something goes wrong with the connection.


def connect(database_name):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except psycopg2.Error as e:
        print "Unable to connect to database"
        # THEN perhaps exit the program
        sys.exit(1)  # The easier method
        # OR perhaps throw an error
        raise e
        # If you choose to raise an exception,
        # It will need to be caught by the whoever called this function


def query_database(query):
    """Take a postgresQL-query and output the result as a list

    Args:
        (str) A string containing a correct postgresQL-query.
    Returns:
        (list) The result from the query as a list to work with

    """
    db, c = connect(DB_name)
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def pretty_results(result):
    """Take the result from a database-query and output it a little bit prettier

    Args:
        (list) The result from a postgresQL-query as a list
    Returns:
        (str) A print statement displaying the results

    """
    number = 1
    for log in result:
        name = str(log[0])
        number_of_views = str(log[1])
        print str(number) + ". " + name + "--" + number_of_views + " views"
        number += 1
    return ""


def pretty_errors(result):
    """Take the result from the error-query and output it a little bit prettier

    Args:
        (list) The result from a the error-query (query 3) as a list
    Returns:
        (str) A print statement displaying the results

    """
    print
    for log in result:
        date = str(log[0])
        percent_errors = str(log[1])
        print " " + date + "    " + percent_errors + "% errors"
    return ""

# make sure that file was ran directly, not importe
# Call functions to output results

if __name__ == '__main__':
    print "\n5 most popular articles(article name--number of views): \n"
    print pretty_results(result=query_database(query1))
    print "\nMost popular authors(author name--number of views): \n"
    print pretty_results(result=query_database(query2))
    print "\nOn which day the error was more than 1.0%: \n"
    print pretty_errors(result=query_database(query3))
    print "\nReporting tool completed. \n"
