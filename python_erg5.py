import random



cols= int(input("Δώστε τις σειρές του πίνακα: "))
while cols < 0:
    cols = int(input("Πρέπει να δώσετε θετηκό αριθμό: "))


rows = int(input("Δώστε το μήκος του πίνακα: "))
while rows < 0:
  rows = int(input("Πρέπει να δώσετε θετηκό αριθμό: "))


sumAll= 0
for k in range(100):
    table = []
    for i in range(cols):
      table.append(["O"] * rows)


    z = 0
    str = int((cols*rows)/2)+((cols*rows) % 2 > 0)
    while z < str:
      x = random.randrange(0, cols)
      y = random.randrange(0, rows)
      if table[x][y] != "S":
          table[x][y] = "S"
          z = z + 1


    print("==================================================")
    for i in range(cols):
      print(table[i])
    print("==================================================")


    hor = 0
    ver = 0
    diag = 0
    for i in range(cols):
        for j in range(rows-2):
          if table[i][j]=="S" and table[i][j+1]=="O" and table[i][j+2]=="S":
              hor+=1
    print("Τα οριζόντια sos είναι: ",hor)


    for i in range(rows):
      n = 0
      for j in range(cols):
          if table[j][i] == "S":
              if n == 2:
                  ver+=1
              n=1
          else:
              if n==1:
                  n=2
              else:
                  n=0
    print("Τα κάθετα sos είναι: ",ver)


    for i in range(cols-2):
        for j in range(rows-2):
            if table[i][j] == "S" and table[i+1][j+1] == "O" and table[i+2][j+2] == "S":
                diag+=1

            
    for i in reversed(range(cols-2)):
        for j in reversed(range(2, rows)):
            if table[i][j] == "S" and table[i+1][j-1] == "O" and table[i+2][j-2] == "S":
                diag += 1
    print("Τα διαγώνια sos είναι: ", diag)


    sum =hor+ver+diag
    print("Τα συνολικά sos είναι: ", sum)
    print("--------------------------------------------------")
    print("")

    sumAll+=sum

print("++++++++++++++++++++++++++++++++")
print("Ο M.O όλων των πινάκων: ", sumAll/100)
print("++++++++++++++++++++++++++++++++")


