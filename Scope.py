# I have no idea if what I was doing was right but..... at least I tried right 
a = [1, 2, 4]
b = a
#input: a list of ints
# output: an int
def update_list(a_list):
    a_list[3] = "yo"
    b = a_list[4]
    b = 100
my_list = [1, 2, 3, 4, 5]
update_list(my_list)
print my_list
#it will replace 4 with yo it will mot print 100 because b is equal to 2 things
var_1 = "kittens" #global
var_2 = "cookies"#global
# input: a string
# output: a string
def my_function(my_favorite_things): #global
    song_lyrics = "rain drops on roses,"#local
    combined_song = song_lyrics + my_favorite_things#local
    return combined_song#local
# input: a string
# output: a string
def my_function_2(item, item2):#global
    full_lyrics = item + "on " + item2#local
    full_song = my_function(full_lyrics)#local
    return full_song#local
my_song = my_function_2(var_1, var_2)#global

var_1 = 'cat'
var_2 = 'dog'

def my_favorite(favorite_pet):
    if favorite_pet == var_1:
        print("My favorite pet is the cat.")
    if favorite_pet == var_2:
        print("My favorite pet is the dog.")
   # var_2 = "cat"# var2 is repeated


print my_favorite(var_1)
print(var_2)
