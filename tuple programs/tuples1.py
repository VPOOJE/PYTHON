'''Write a python program that scans an email address
and forms a tuple of user name and domain
Sample Input:
22cs453@kpriet.ac.in
Sample output:
User name: 22cs452
Domain name: kpriet.ac.in'''
def domain(email):
    username, domain = email.split('@')
    return username, domain
email_ad = '22cs453@kpriet.ac.in'
username, domain = domain(email_ad)
print("User name:", username)
print("Domain name:", domain)
