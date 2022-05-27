import os
stall_message = "..."

Levels = {
0: "time to dig",
1:"small and cramped",
2:"it smells of frogs",
3:"there is mist",
4:"its hard to breathe",
5:"endless amount of cats",
6:"the walls are spongey",
7:"there is a diary here",
8:"who are you?",
9:"nice shovel kid",
10:"you hear laughter",
11:"it is a birthday party",
12:"you weren't invited",
13:"you hear voices",
14:"start dancing",
15:"stop dancing",
16:"unoptimized dig",
17:"there is no walls",
18:"there is no floor",
19:"is it really that dark",
20:"okay okay alright okay",
21:"what is 9 + 10?",
22:"uhhhhhhhhhhhhhhhhhh",
23:"cookie clicker but worse",
24:"you see flashing lights",
25:"its another uninvited party",
26:"guess we will forget that",
}

def main():
    pass

if __name__ == '__main__':
    main()

class player():
    def __init__(self):
        self.name = "jack"
        self.health = 5
        self.location = 0
        self.g = 5
        self.shovel_health = 6
        self.shovel_strength = 1

    def shop(self):
        print(
'''1 - 0g repair shovel
2 - 10g sharpen shovel''')
        print(str(self.g) + "g")
        tools = input("buy:")
        if tools == "1":
            self.shovel_health = self.shovel_health + 6
            print((self.name), "got some repairs")
        if tools == "2":
            if (self.g > 10):
                self.g = self.g - 10
                self.shovel_strength = self.shovel_strength + 1
                print((self.name), "got buffer shovel")
            else:
                print("you can't afford, dig")

    def save(self):
        savename = input("save name:")
        savename = ("saves/" + savename + ".digging")
        f = open((savename), "w")
        f.write(str(self.name) + "\n" +
        str(self.health) + "\n" +
        str(self.location)
        + "\n" + str(self.g) +
        "\n" + str(self.shovel_health) +
        "\n" + str(self.shovel_strength))
        print("saved as", savename)

    def load(self):
        loadname = input("load name:")
        loadname = ("saves/" + loadname + ".digging")
        try:
            f = open((loadname), "r")
            for i, line in enumerate(f):
                if i == 0:
                    self.name = str(line).rstrip()
                    print("name:" + str(self.name))
                if i == 1:
                    self.health = int(line)
                    print("health:" + str(self.health))
                if i == 2:
                    self.g = int(line)
                    print("g:" + str(self.g))
                if i == 3:
                    self.shovel_health = int(line)
                    print("shovel_health:" + str(self.shovel_health))
                if i == 4:
                    self.shovel_strength = int(line)
                    print("shovel_strength:" + str(self.shovel_strength))
            f.close()
        except:
            print("that probably doesn't exist")

    def help(self): print (Commands.keys(), sep =', ')


    def dig(self):
        self.g = self.g + 1
        if (self.shovel_health<0):
            print((p.name), "broke their shovel, shop now")
        else:
            self.shovel_health = self.shovel_health - 1
            self.location = self.location + self.shovel_strength
            if (self.location >= (len(Levels) - 1)):
                print(stall_message)
            else:
                print("you are at", str(self.location) + ",", (Levels[self.location]))
                print(".\n"*self.location)
                print("O")
    def location(self):
        if (self.location > (len(Levels) - 1)):
            print(stall_message)
        else:
            print("you are at", str(self.location) + ",", (Levels[self.location]))
            print(".\n"*self.location)
            print("O")

Commands = {
'dig': player.dig,
'location': player.location,
'help': player.help,
'shop': player.shop,
'save': player.save,
'load': player.load,
}


p = player()
p.name = input("name:")

try:
    while (p.health > 0):
        line = input("> ")
        os.system('cls' if os.name == 'nt' else 'clear')
        args = line.split()
        if len(args) > 0:
            commandFound = False
            for c in Commands.keys():
                if args[0] == c[:len(args[0])]:
                    Commands[c](p)
                    commandFound = True
                    break
            if not commandFound:
                print((p.name), "didn't understand that")
except KeyboardInterrupt:
    print("\ngoodnight")
else:
    print("whoops")
