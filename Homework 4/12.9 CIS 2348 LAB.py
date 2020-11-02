#Henry Saravia, PSID: 1853318

input_data = input().split()
input_name = input_data[0]
while input_name != '-1':
    try:
        age = int(input_data[1]) + 1
    except ValueError:
        age = 0
    print(str(input_name) + " " + str(age))

    input_data = input().split()
    input_name = input_data[0]
