try:
    f = open('revise codes.txt')
    if f.name != 'mohana.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("Error! dude")

else:
    print(f.read())
    f.close()
finally:
    print("you run you code! congrats!")
