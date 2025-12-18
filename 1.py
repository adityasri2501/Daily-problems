# take input from user until the user enters an empty line

i = 1
final_para = ""
while(True):
    line = input()
    if (i == 1):
        final_para = line + "\t"
        i+=1
    else:
        final_para = final_para + line + "\t"
    if(line == ""):
        break
print(f"{final_para}")