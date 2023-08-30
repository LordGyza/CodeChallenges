def spell (txt):
    if len(txt)== 1:
        print(txt)
    else:
        spell(txt[1:])
        print(txt[0])
 
 txt = input()
 spell(txt)