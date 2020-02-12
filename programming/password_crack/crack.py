import hashlib, sys

def temp_transfer(fl, array_temp):
    for i in fl:
        if i.rstrip():
            array_temp.append(i)
    return array_temp

def make_array(array_temp, array):
    for i in array_temp:
        array.append(i.replace(i[-1], ''))
    return array

m = hashlib.md5()
password_hash = "267530778aa6585019c98985eeda255f"

years_temp = []
colors_temp = []
names_temp = []

years = []
colors = []
names = []

with open("years.txt", 'r') as y, open("colors.txt",'r') as c, open("names.txt", 'r') as n:
    
    #After looking at the other solution, I came to the conclusion that it was stupid on my part not to puth them in lists from the beginning, since all I do differently is waste time to put the from files to lists. 
    colors_temp = temp_transfer(c, colors_temp)
    years_temp = temp_transfer(y, years_temp)
    names_temp = temp_transfer(n, names_temp)

    colors = make_array(colors_temp, colors)
    years = make_array(years_temp, years)
    names = make_array(names_temp, names)

    for i in colors:
        for j in years:
            for k in names:
                m = hashlib.md5()
                line = i + "-" + j + "-" +k
                m.update(line)
                word_hash = m.hexdigest()
                if(word_hash == password_hash):
                    print("The password is: " + line) 
                    sys.exit() 
