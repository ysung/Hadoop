# Hadoop

How many hits were mad to the page
    1. MapReduce
    2. grep "the-associates.js" access_log | wc -l
    A: 2456

How many hits were made by the IP address 10.99.99.186
    1. MapReduce
    2. grep "10.99.99.186" access_log | wc -l
    A: 6

Most popular file's pathname and number of occurrences:
    *Be sure to remove the portion "http://www.the-associates.co.uk" from pathnames in your mapper so that all occurrences of a file are counted together
    A: /assets/css/combined.css, 117352(117348+4)