import maya.OpenMaya as OM
#Creates an empty selection list.
LIST = OM.MSelectionList()
#Assign active selections to a selection list.
OM.MGlobal_getActiveSelectionList(LIST)
     
for i in range(0 ,LIST.length()):
  #Creates a pointer for an object.
  obj = OM.MObject()
  #Get a handle for the dependency node of the given element of the selection list
  #assign to pointer.
  LIST.getDependNode(i,obj)
     
  #MFnDependencyNode allows the creation and manipulation of dependency graph nodes
  #Attaches a function set to the object pointer
  node=OM.MFnDependencyNode(obj)
  #This is one of the nodes to print
  print (node.name()+"\n")
     