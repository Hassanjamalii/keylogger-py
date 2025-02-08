print('Input your keylogger message:')
x = input()


with open('log.txt','a') as file:
  y = file.write(x + '\n')

