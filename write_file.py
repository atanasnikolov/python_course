def add_list(text):
    f = open('list.txt', 'a')
    real_text = text + "\n"
    f.write(real_text)
    f.closed
    return None

while True:
    user_input = input('Add stuff to list: ')
    if user_input == 'exit':
        break
    else:
        add_list(user_input)
