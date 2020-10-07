# Henry Saravia, PSID: 1853318

file1 = open('inputDates.txt', 'r')
date = file1.readlines()

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

check = 0
for string in date:
  check = check + 1
  if string == '-1':
    break

  try:
    year = string.split()
    num = len(year)
    if num != 3:
      continue
    month = year[0]
    day = year[1]
    year = year[2]
    day1, comma = day.split(',')

    for x in range(12):
      if string.find(months[x]) >= 0:
        month = str(x + 1)
        result = month + '/' + day1 + '/' + year
        if check > 0:
          file2 = open('parsedDates.txt', 'a')
          file2.write(result + "\n")
          file2.close()
        else:
          file3 = open('parsedDates.txt', 'w')
          file3.write(result + "\n")
          file3.close()
        break

  except ValueError:
    continue

file1.close()
