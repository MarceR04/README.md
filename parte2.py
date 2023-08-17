import readchar

while True:
    key = readchar.readkey()
    if key == readchar.key.UP:
        print(key)
        break
    print("Presionaste la Tecla: {key}")
 
