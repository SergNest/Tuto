def get_credentials_users(path):    
    with open(path, 'rb') as file:
            list_return = []
            while True:
                line = file.readline()
                if not line:
                    break              
              
                list_return.append(line.decode('utf-8').replace('\n',''))
            return list_return

            

print(get_credentials_users('WorkWithFiles/output.bin'))
