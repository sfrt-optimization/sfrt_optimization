from gurobipy import *
import matplotlib.pyplot as plt
import plotly.express as px
import random
import math
import json
import pickle

def optimization(nodes, cliques):
   model = Model("optimal")  # create model

   x = model.addVars(nodes, vtype=GRB.BINARY)

   model.addConstrs(quicksum(x[i] for i in cliques[j]) <= 1 for j in range(len(cliques)))

   model.setObjective(quicksum(x[i] for i in nodes.keys()), GRB.MAXIMIZE)
   model.setParam("OutputFlag", 1)
   model.Params.TimeLimit = 36000
   #model.Params.TimeLimit = 160
   model.update()
   model.optimize()

   #if model.status == GRB.Status.OPTIMAL:
   holder = []
   holder = model.getAttr("x")

   return holder


def plot(cube, size):

   fig = plt.figure()
   ax = fig.add_subplot(projection='3d')

   for i in range(size):
       ax.scatter(cube[i][0], cube[i][1], cube[i][2], s=10, c=1)
   plt.show()

if __name__ == '__main__':


    cliques = []
    with open("../data/cliques.pkl", 'rb') as openfile:
        cliques = pickle.load(openfile)

    node_dict = {}
    with open("../data/node_data.pkl", 'rb') as openfile:
        node_dict = pickle.load(openfile)



    node_index = optimization(node_dict,cliques)

    optimal_nodes = []

    for i in range(len(node_index)):
       node_index[i] = int(node_index[i])
       if node_index[i] == 1.0:
           optimal_nodes.append(node_dict.get(str(i)))



    print(node_index)
    print(optimal_nodes)
    print(len(optimal_nodes))
    plot(optimal_nodes,len(optimal_nodes))
    x = []
    y = []
    z = []
    for i in range(len(optimal_nodes)):
        x.append(optimal_nodes[i][0])
        y.append(optimal_nodes[i][1])
        z.append(optimal_nodes[i][2])

    ifig = px.scatter_3d(x=x, y=y, z=z)
    ifig.show()
