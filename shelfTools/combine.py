from importlib import reload
import hou

def run():
    nodeList = hou.selectedNodes()
    # create a geo node and create objmerge nodes for each output sop
    # fill the paths pamrameters.

    geoNode = hou.node('/obj').createNode('geo','objects_merge')
    outputSopList = []
    for node in nodeList:
        for sop in node.children():
            if 'output' in sop.type().nameWithCategory():
                outputSopList.append(sop) 
    print(f"output list is {outputSopList}")
    objmergeList = []
    for output in outputSopList:
        path = output.path()
        objmergeName = output.parent().name()
        print(f"obj merge's parent's name is {objmergeName}")
        objmergeNode = geoNode.createNode('object_merge',objmergeName)
        # objmergeNode.setName('objmergeName')
        parm = objmergeNode.parm('objpath1')
        parm.set(path)
        parmTransform = objmergeNode.parm('xformtype')
        parmTransform.set(1)
        objmergeList.append(objmergeNode)
    # create merge in geo node
    merge = geoNode.createNode('merge')
    for index, objmerge in enumerate(objmergeList):
        # connect first objmerge to merge
        merge.setInput(index,objmerge)
    merge.setSelected(True)
    merge.setDisplayFlag(True)
    merge.setRenderFlag(True)
    hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor).setCurrentNode(merge)
    #set merge visible and select 
    #layout all nodes