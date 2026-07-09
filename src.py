class Hashing_array:
    def __init__(self,size):
        self.size = size
        self.arr = [None]*self.size

     
    def hashing(self,data):    
        if type(data)  == int:
            return data % self.size
            
        else:
            h = abs(hash(data)) 
            return h % self.size
    

    def insert_data(self,data):
        hash_value = self.hashing(data)

        if self.arr[hash_value] == None:
            self.arr[hash_value] = data
        else:
            print("The place already filled")
    

    def search_data(self,data):
        hash_value = self.hashing(data)
        print(f"Data : {data}, Searching in index : {hash_value}")

        if self.arr[hash_value] == data:
            print(f"Yes the item {{{data}}} is find , in index {hash_value}")
        else:
            print("The data have not in place of hash_value")
    


