x = [ [5,2,3], [10,8,9] ]
x[1][0] = 15 
print(x)
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = "Bryat"
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0]='Andres'
print(sports_directory['soccer'])

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterate_dictionary(somelist):
    for x in range(0, len(somelist)-1):
        output=""
        for key, val in somelist[x].items():
            output += f"{key} - {val},"
        print(output)
iterate_dictionary(students)

