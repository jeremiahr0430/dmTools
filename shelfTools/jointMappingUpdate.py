#import dmTools.shelfTools.jointMappingUpdate as jmu
#from importlib import reload
#reload(jmu)
def updateString(parm):
    parmString = parm.eval()
    # print(f'original: {parmString}')
    pList = parmString.split('_')
    parmString = '@name=' + '_'.join(pList[4:])
    # print(parmString)
    return parmString
node = hou.selectedNodes()[0]
#numberOfParms = node.parm('mapping')
parmRange = range(17)
# print( parmRange )
for n in parmRange:
    parmName = f'from{n}'
    parm = node.parm(parmName)
    parmValue = updateString(parm)
    print(f'parmValue is {parmValue}')
    parm.set(parmValue)