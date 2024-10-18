# Create Custom Dictionary

class CustomDictionary:
    def __init__(self):
        self.data = []
        self.key_set = set() 
    def set(self, key, value):
        if key in self.key_set:
            print(f"The key {key} already exists, so its value will be updated")
            for i, (k, v) in enumerate(self.data):
                if k == key:
                    self.data[i] = (key, value)
                    return
        else:
            self.key_set.add(key)
        self.data.append((key, value))
    def items(self):
        return self.data
    def keys(self):
        return list(self.key_set) 
    
    

d = CustomDictionary()
d.set("name", "Arman")
d.set("lastname", "Marutyan")
d.set("lastname", "Aaa")
print(d.items())
print(d.keys())

