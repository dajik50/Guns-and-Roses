import re


def get_address(port):
    f = open('exc.txt')
    while True:
        data = ""
        for line in f:
            if line == '\n':
                break
            data += line
        if not data:
            return "没有该段落"
        obj = re.match(r'\S+', data)
        if port == obj.group():
            pattern = r'[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}'
            obj = re.search(pattern, data)
            if obj:
                return obj.group()


if __name__ == '__main__':
    port = input("端口：")
    print(get_address(port))
