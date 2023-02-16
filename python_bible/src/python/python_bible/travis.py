users = ['Chris', 'Jill', 'Ada', 'Leon', 'Claire', 'Wesker', 'Barry']

print len (users)

while True:
    print 'Hi! I am Travis.'
    name = raw_input ('What is your name? \n').strip().capitalize()
    if name == 'Travis':
        print 'Nice try :)'
    elif name in users:
        print 'Welcome {}.'.format(name)
        print 'Number of users = {}.'.format(len(users))
        remove = raw_input('Do you want to be removed from the system? Please enter Yes or No. \n').strip().capitalize()
        while remove not in {'Yes', 'Y', 'No', 'N'}:
            remove = raw_input('Do you want to be removed from the system? Please enter Yes or No. \n').strip().capitalize()
        if remove is 'Yes' or 'Y':
            print 'Okay. I will remove you from the system.'
            users.remove(name)
            print 'Number of users = {}.'.format(len(users))
        else:
            print 'Okay. I will not remove you from the system.'
    else:
        print 'Welcome {}.'.format(name)
        print 'Number of users = {}.'.format(len(users))
        add = raw_input('Do you want to be added to the system? Please enter Yes or No. \n').strip().capitalize()
        while add not in {'Yes', 'Y', 'No', 'N'}:
            add = raw_input('Do you want to be added from the system? Please enter Yes or No. \n').strip().capitalize()
        if add is 'Yes' or 'Y':
            print 'Okay. I will add you to the system.'
            users.append(name)
            print 'Number of users = {}.'.format(len(users))
        else:
            print 'Okay. I will not add you to the system.'