# A Django webproject using a free bootstrap template

Dentist Website for showcasing services, doctors, blogging, and making appointments.
Based on a freely available colorlib template (https://colorlib.com/wp/template/dentacare/)

## Features:

- Dentist Website implementing a bootstrap template
- Home, About, Services, Doctors, Blog, Contact Pages
- Functional appointment and contact forms, using send_mail
- Google maps embedding
- Template tags (static, block content...)
- Template inheritance (extends base)

### Note: to run this on your local machine, you need:
- a virtual environment holding the dependencies
- a mailserver running 

Simplest variant for a mailserver is to use the minimalist mail server 
shipped with Python's send_mail module. It can be activated like this:
```python -m smtpd -n -c DebuggingServer localhost:1025```


#### I completed this project while watching this coding tutorial by John Elder:
https://www.youtube.com/watch?v=4b3yvjcPLnk&list=PL4D4DuZkCB8XxXpxOn1k9Mpx9nQ8xog86

