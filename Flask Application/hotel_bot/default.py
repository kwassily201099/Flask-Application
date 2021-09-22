
DEFAULT_SOURCE = """
+ hello
- hello

+ my name is *
- <set name=<formal>>Nice to meet you, <get name>. can you enter your phone number

+ do you have any rooms free
- we have 5 rooms free

+ *
- I don't have a reply for that.
- Try asking that a different way.

+ what are the kind of rooms in this hotel
- there are : single rooms / double / triple / queen / king rooms available in the hotel

+ i want to book a room
- what kind of room do you want

+ i want to book a single room
- how long would you want to stay

+ i want to stay for a week
- what view would you like pool view or garden view
 
+ pool view
- smoking or no smoking

+ no smoking
- ok enter your name

+ my phone number is *
- <set phone=<formal>> what is your email

+ my email is *
- all done, thank you.
"""