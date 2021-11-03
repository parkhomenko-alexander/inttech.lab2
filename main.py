from client import Client

if __name__ == '__main__':
    login = 'test'
    pas = 'test'
    url = 'http://157.230.191.9/'
    client = Client(login, pas, url)
    print(client)
    print(client.login())
    # print(client.post_todo('taskskskфывфывksk'))
    print(client.get_todo())
    # print(client.put_todo(6, 'CHANGED_TASKA'))
    print(client.delete_todo(5))
