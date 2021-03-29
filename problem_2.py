class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

        
person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)

a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4,
            "user": person_b,
        }
    },
}
def print_depth_2(data):
    print("\n")
    initial_depth = 1

    final_res = find_depth( data, initial_depth)
    print(final_res)
    return final_res
    

def find_depth(data, depth, return_obj={"result": ""}):
    if type(data) == dict :
        keys_list = data.keys()
        for key in keys_list:
            return_obj['result'] += key + " "+ str(depth) + "\n"
            if( type(data[key]) == Person or type(data[key]) == dict ):
                find_depth( data[key] , depth+1, return_obj)
            
    elif type(data) == Person :
        for prop, value in vars(data).items():
            return_obj['result'] += prop + " "+ str(depth) + "\n"
            if( type(value) == Person or type(value) == dict ):
                find_depth( value, depth+1, return_obj )
    return return_obj['result']
    
        

if __name__=="__main__":
    print_depth_2(a)
