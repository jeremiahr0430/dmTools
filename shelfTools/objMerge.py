import hou
def run():
    def setpos(refNode,node):
        selnodePos = refNode.position()
        # Create position for the node to be created
        position   = [selnodePos[0]-1,selnodePos[1]-2]
        node.setPosition(position)


    nodeSelect = hou.selectedNodes()[0]
    nullNode = nodeSelect.parent().createNode('null')

    nullNode.setInput(0,nodeSelect)
    setpos(nodeSelect,nullNode)

    objMergePath = nullNode.path()
    objMerge = nodeSelect.parent().createNode('object_merge')
    objMerge.parm("objpath1").set(objMergePath)
    objMerge.parm("xformtype").set(1)
    setpos(nullNode,objMerge)
    nodeSelect.setCurrent(False)
    objMerge.setCurrent(True) 

