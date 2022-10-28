all_probs = [{}, {}, {}]
list_find_city = []
temperatura = []
all_size_probs = len(all_probs)

def find_city(name_city):
    for city in list_find_city:
        if name_city == city:
            return False
    return True
    
def find_max_min_by_city(name_gorod):
    temperatura = all_size_probs[index]['prob']
    pass
    
    
answer_list = []
index = 0
while index<all_size_probs:
    name_gorod = all_size_probs[index]['city']
    if find_city(name_gorod):
        list_find_city.append(name_gorod)
    
    index += 1
        
        
        
        
        
        
        
        
        
        
        
        
one_prob ={
    "day":"2022-10-19",
    "city":"Moskow",
    "prob":{
        "morning":-1,
        "afternoon":5,
        "evening":-2
    }
}
one_prob1 ={
    "day":"2022-08-20",
    "city":"Moskow",
    "prob":{
        "morning":20,
        "afternoon":25,
        "evening":16
    }
}
one_prob2 ={
    "day":"2022-10-28",
    "city":"Kazan",
    "prob":{
        "morning":0,
        "afternoon":5,
        "evening":-1
    }
}
one_data = {
    "city ":"gorod",
    "max_temp":{
        "size": 27,
        "day":"2022-07-23"
    },
    "min_temp":{
        "size": -21,
        "day":"2022-02-24"    
    }
}