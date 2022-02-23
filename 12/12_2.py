# Has to be a list. simple variable types (i.e. non object pointer) are
# not referenced correctly as globals
validRoutes = 0
smallNodeDoneTwice = ''


def selectValidEdge(route, nodeToJoin, nodesInRoute, rest, validRoutes, smallNodeDoneTwice):

    for edge in rest:
        # Only check those edges not already added
        addEdge = False
        if nodeToJoin in edge: # This edge can join
            # only check edges where lower case nodes have
            # not already turned up somewhere
            addEdge = True
            for node in edge:
                if node == node.lower() and node in nodesInRoute:
                    if node != nodeToJoin:
                        if smallNodeDoneTwice != '':
                            # Don't want this one, it has a lower case node already added
                            # that isn't the node we are trying to join to.
                            addEdge = False
                            break
            
            if addEdge:
                # If this is marked for adding, then add it
                route.append(edge)
                for node in edge:
                    if node != nodeToJoin:
                        # If this is a lower case node that has already been added once,
                        # make a note of it.
                        if node == node.lower() and node in nodesInRoute and node != nodeToJoin:
                            smallNodeDoneTwice = node
                        nodesInRoute.append(node)
                        newNodeToJoin = node                       

            # Check to see if an end has been reached
            if 'end' in edge:
                validRoutes += 1
                #print(route)
                # Remove edge from route
                route.pop()
                # remove node from the node list
                node = nodesInRoute.pop()
                if node == smallNodeDoneTwice and node != nodeToJoin:
                    smallNodeDoneTwice = '' # Remove second instance of small node
                # This can't go further so revoke the addEdge
                addEdge = False
            
            if addEdge:
                # Move recursively into this loop
                validRoutes, smallNodeDoneTwice = selectValidEdge(
                    route, newNodeToJoin, nodesInRoute, 
                    rest, validRoutes, smallNodeDoneTwice)

    # Finished outer loop, strip off last edge and nodes.
    # Remove edge from route
    route.pop()
    # remove node from the node list
    node = nodesInRoute.pop()
    if node == smallNodeDoneTwice:
        smallNodeDoneTwice = '' # Remove second instance of small node
    return validRoutes, smallNodeDoneTwice

input = []

with open('12\\12.txt') as f:
    for line in f.readlines():
        input.append(line.strip('\n'))

# Input data is individual edges from a graph, each connecting 2 nodes.
# Gather the data into known start points and everything else
starts = []
rest = []
for line in input:
    edge = line.split('-')
    if 'start' in edge:
        starts.append(edge)
    else:
        rest.append(edge)

# for each start, begin selecting edges from rest that can join to it. then
# repeat recursively walking down the line until an edge with end is met or until
# no more progress can be made. Then count if it was at an end, and step back one
# and repeat. Note that no single edge can appear twice as they all contain
# a 'small' cave so valid edges can be checked against those already in the graph
for start in starts:
    # Add the start of the route
    route = []
    nodesInRoute = []
    route.append(start)
    # record the nodes used
    for node in start:
        nodesInRoute.append(node)

    caveToJoin = [cave for cave in start if cave != 'start'][0]
    smallNodeDoneTwice = ''
    validRoutes, smallNodeDoneTwice = selectValidEdge(
        route, caveToJoin, nodesInRoute, 
        rest, validRoutes, smallNodeDoneTwice)

    print(validRoutes)
