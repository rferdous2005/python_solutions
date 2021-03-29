a = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4
            }
        }
    }


def print_depth(dictionary):
    print("\n")
    initial_depth = 1

    return find_depth( dictionary, initial_depth)
    

def find_depth(dictionary, depth, return_obj={"result": ""}):
    keys_list = dictionary.keys()
    for key in keys_list:
        print(key, depth)
        return_obj['result'] += key + " "+ str(depth) + "\n"
        if( type(dictionary[key]) == dict ):
            find_depth( dictionary[key] , depth+1, return_obj)
    return return_obj['result']
    
        

if __name__=="__main__":
    print_depth(a)
