phone_book = {}

SWITCH_ON = True

while SWITCH_ON:
    print('Welcome to the phone book app')
    print('1. Add a contact')
    print('2. display contacts')
    print('3. Search contacts')
    print('4. Exit')

    user_input = int(input('What do you want to do today? '))
    
    #ADDOING CONTACTS
    if user_input == 1:
        name = input('Enter the name of the contact: ')
        phone_number = input('Enter the phone number of the contact: ')
        phone_book[name] = phone_number
        print('Contact added successfully!')
    
    #DISPLAYING CONTACTS
    elif user_input == 2:
        if len(phone_book) == 0:
            print('No contacts found.')
        else:
            print('Here are your contacts:')
            for name, phone_number in phone_book.items():
                print(f'{name}: {phone_number}')
    
    
    #SEARCHING CONTACTS
   
    elif user_input == 3:
        search_name = input('Enter the name of the contact you want to search for: ')
        if search_name in phone_book:
            print(f'{search_name}: {phone_book[search_name]}')
        else:
            print('Contact not found.')
    
    #EXITING THE APP
    
    elif user_input == 4:
        SWITCH_ON = False
        print('EXIT')
    else:
        print('Invalid input. Please try again.')