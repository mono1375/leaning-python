import datetime

default_names = ['Justin', 'John','Emilee','Jim','Ron','Sandra','Veronica','Whitney']
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

unf_message = """Hi {name}!

Thank you for the purchase on {date}.
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}
Have a great one!

Team CFE
"""

def make_Messeges(names,amounts):
    messages = []
    if len(names) == len(amounts):
        i= 0
        today = datetime.date.today()
        new_date = '{today.month}/{today.day}/{today.year}'.format(today=today)
        for name in names:
            name = name[0].upper() + name[1:].lower()
            new_amount ='%.2f' %(amounts[i])
            new_msg = unf_message.format(
                    name=name,
                    date=new_date,
                    total= new_amount

            )
            i+=1
            print(new_msg)

make_Messeges(default_names,default_amounts)
print(len(unf_message))
