class Client:
    def __init__(self, name, second_name, status=True,**extra):
        self.name = name
        self.second_name = second_name
        self.status = status
        self.extra = extra

    def __str__(self):
        if self.status == True:
            return f"{self.name} {self.second_name}: активен"
        else:
            return f"{self.name} {self.second_name}: заблокирован"

class Clients:
    def __init__(self):
        self.clients = []
    def add_client(self, client):
        self.clients.append(client)

    def find(self, condition, limit=None):
        result = []
        for client in self.clients:
            if limit is not None and len(result) >= limit:
                break
            if condition(client):
                result.append(client)
        return result  
          
def is_active(client):
    return client.status 

def from_minsk(client):
    if "city" in client.extra and client.extra["city"] == "Минск":
        return True
    else:
        return False   









c1 = Client("Анна", "Петрова", city="Минск", phone_number="123")
c2 = Client("Борис", "Иванов", status=False)


print(c1)  # Анна Петрова: активен
print(c2)  # Борис Иванов: заблокирован

book = Clients()
book.add_client(c1)
book.add_client(c2)
print(len(book.clients))  # 2
print(book.clients[0])    # Анна Петрова: Активен

book = Clients()
book.add_client(c1)
book.add_client(c2)

active = book.find(is_active)
print(len(active))      # 1
print(active[0])        # Анна Петрова: Активен

minsk_clients = book.find(from_minsk)
print(len(minsk_clients))   # 1

print(len(book.find(is_active)))              # 1 (у нас один активный)
print(len(book.find(is_active, limit=1)))     # 1
print(len(book.find(is_active, limit=0)))     # 0 