#!/usr/bin/env python2

import psycopg2
conn = psycopg2.connect("dbname=news")
cursor = conn.cursor()

# Problem 1: 3 most popular articles of all time
cursor.execute("""
                WITH log AS (
                SELECT path, count(path) AS views
                FROM log
                GROUP BY log.path
              )
                SELECT title, views
                FROM articles INNER JOIN log
                ON log.path = '/article/' || articles.slug
                ORDER BY views DESC
                LIMIT 3;
               """)

article_ranking = cursor.fetchall()
print ""
print "Problem #1 - 3 most popular articles of all time:"
for title, views in article_ranking:
    print "\"" + title + "\"" + " -- " + str(views) + " views"
print ""


# Problem 2: Most popular article authors of all time
cursor.execute("""
               WITH log AS (
                SELECT path, count(path) AS views
                FROM log
                GROUP BY log.path
              ),
                author_views AS (
                SELECT author, views
                FROM articles INNER JOIN log
                ON log.path = '/article/' || articles.slug
              )

               SELECT name, SUM(author_views.views) AS total
               FROM authors JOIN author_views
               ON authors.id = author_views.author
               GROUP BY name
               ORDER BY total DESC;
               """)

author_ranking = cursor.fetchall()
print "Problem #2 - Most popular article authors of all time:"
for author, views in author_ranking:
    print author + " -- " + str(views) + " views"

print ""


# Problem 3: Days with > 1% of requests resulting in errors
cursor.execute("""
               WITH requests_per_day AS (
               SELECT time::date AS date,
               count(*) AS requests
               FROM log
               GROUP BY date),

               errors_per_day AS (
               SELECT time::date AS date,
               count(*) AS errors
               FROM log
               WHERE NOT status = '200 OK'
               GROUP BY date),

               rate_per_day AS (
               SELECT requests_per_day.date,
               round(errors::numeric/requests * 100, 2) AS error_pct
               FROM requests_per_day JOIN errors_per_day on
               requests_per_day.date = errors_per_day.date)

               SELECT to_char(rate_per_day.date, 'FMMonth DD, YYYY'), error_pct
               FROM rate_per_day
               WHERE error_pct > 1.00
               ORDER BY date;
               """)

high_error_days = cursor.fetchall()
print "Problem #3 - Days with error rates higher than 1%:"
for date, rate in high_error_days:
    print date + " -- " + str(rate) + "%"

print ""

conn.close()
