def have(obj, *arg):
    # print(obj)
    # print(arg)
    stand = obj
    try:
        for i in range(0, len(arg)):
            # print("stand")
            # print(stand)
            # print("arg[i]")
            # print(arg[i])
            stand = stand[arg[i]]
            # print("stand ==")
            # print(stand)
        return True
    except Exception as e:
        # print('error')
        return False


#
# g = {'h':{'d':1}}
# g
# g.d
# have(g.d)
# jss(g,"h.d")
# stand = jss2(g,"h","d")
# stand
