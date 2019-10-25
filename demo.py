def fun():
    while True:
        print("二级界面")
        cmd = input(">")
        if cmd == '1':
            pass
        elif cmd == '2':
            break

while True:
    print("一级界面")
    cmd = input(">")
    if cmd == '1':
        pass
    elif cmd == '2':
        fun()
    elif cmd == '3':
        fun()