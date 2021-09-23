mport re

list = ["guru99 get", "guru99 give", "guru Selenium"]
for element in list:
    z = re.match("(g\w+)\W(g\w+)", element)
if z:
    print((z.groups()))

patterns = ['software testing', 'guru99']
text = 'software testing is fun?'
for pattern in patterns:
    print('Looking for "%s" in "%s" ->' % (pattern, text))
    if re.search(pattern, text):
        print('found a match!')
else:
    print('no match')
abc = 'guru99@googlecom, careerguru99@hotmail.com, useryahoomail.com'
emails = re.findall(r'[\w\.]+@[\w\.]+', abc)
for email in emails:
    print(email)
