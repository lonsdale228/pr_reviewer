import threading


def print_hi(name):
  thread = threading.Thread(target=lambda:print_hi('PyCharm'))
  thread.start()
  print(f'Hi, {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
