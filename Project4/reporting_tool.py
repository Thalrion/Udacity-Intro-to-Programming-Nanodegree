#!/usr/bin/env python2.7

import psycopg2

# Name of the database

DB_name = "news"

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
# It outputs the day and the according error-quote in percentage.

query3 = """ SELECT views_per_day.time::date, ROUND((errors_per_day.count * 1.0
                / views_per_day.count * 1.0)*100, 2) as quote
                FROM views_per_day, errors_per_day
                WHERE views_per_day.time = errors_per_day.time; """


def query_database(query):
    """Take a postgresQL-query and output the result as a list

    Args:
        (str) A string containing a correct postgresQL-query.
    Returns:
        (list) The result from the query as a list to work with

    """
    db = psycopg2.connect(database=DB_name)
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close()


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
        print str(number) + ". " + name + "--" + number_of_views
        number += 1
    return ""


def pretty_errors(result):
    """Take the result from the error-query and output it a little bit prettier

    Args:
        (list) The result from a the error-query (query 3) as a list
    Returns:
        (str) A print statement displaying the results

    """
    print "   Date " + "   " + "Percent Errors"
    print
    for log in result:
        date = str(log[0])
        percent_errors = str(log[1])
        print date + "    " + percent_errors + "%"
    return ""

# Call functions to output results

print "\n5 most popular articles(article name--number of views): \n"
print pretty_results(result=query_database(query1))
print "\nMost popular authors(author name--number of views): \n"
print pretty_results(result=query_database(query2))
print "\nHow many errors occured on each day: \n"
print pretty_errors(result=query_database(query3))
print "\nReporting tool completed. \n"
