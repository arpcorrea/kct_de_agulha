# -*- coding: utf-8 -*-
import numpy as np
from .mesh import Mesh
from .fields import Field

class Mesher():

    def __init__(self,  problem):
        self.mesh_domains( problem)
        self.initialize_fields(problem)
# 
    def mesh_domains(self, problem):
        self.meshes = []
        nx=0
        ny=0
        for domain in problem.domains:
            self.meshes.append( Mesh(domain) )
            nx = domain.mesh["Number of Elements in X"]
            ny = ny + domain.mesh["Number of Elements in Y"]
        # self.Total_elements_X = nx
        # self.Total_elements_Y = ny
        self.M= np.zeros((ny, nx))
        
    def initialize_fields(self, problem):
        self.fields = {}
        for field_name in problem.required_fields:
            # import pdb; pdb.set_trace()
            self.fields[field_name] = Field(field_name, self.M, problem)
    #         # import pdb; pdb.set_trace()
                        

                    
                
        