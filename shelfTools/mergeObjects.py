import hou
for node in hou.selectedNodes():
    parm = node.parm('objpath1')
    parmString = parm.eval()
    parmStringList = parmString.split('/')
    out = 'OUT'
    parmStringList = parmStringList[:-1]
    parmStringList.append(out)
    print(f'parmStringList is {parmStringList}')
    parmString = '/'.join(parmStringList)
    parm.set(parmString)