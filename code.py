# -*- coding: utf-8 -*-


class Node():
    def __init__(self,data,depth,past=None):
        self.node_data = data
        self.left_node = None
        self.right_node = None
        self.past_node = past
        self.depth = depth
       
        

class BinarySearchTree():
    def __init__(self):
        self.root_node = None
        self.total_depth = 0
        self.depth_count = {}

    
    def __depth_number_check(self,depth):
        if depth in self.depth_count:
            self.depth_count[depth]+=1
        else:
            self.depth_count[depth] = 1
 
        
    def check_root_node(func):
        def check(self,*args):
            if self.root_node is None:
                print("False! First you need to insert value.")
                return
            return func(self,*args)
        return check

        
    def insert(self,data,node=None):
        if node is None:
            if self.root_node is None:   
                self.root_node = Node(data,0)
            else:
                self.insert(data,self.root_node)
        else:
            if data < node.node_data:
                if  node.left_node is None:                    
                    node.left_node = Node(data,node.depth+1,node)
                    self.__depth_number_check(str(node.depth+1))
                    if self.total_depth < node.depth+1:
                        self.total_depth = node.depth+1
                else:
                    self.insert(data,node.left_node)
            elif data > node.node_data:
                if node.right_node  is None:
                    node.right_node = Node(data,node.depth+1,node)
                    self.__depth_number_check(str(node.depth+1))
                    if self.total_depth < node.depth+1:
                        self.total_depth = node.depth+1
                else:
                    self.insert(data,node.right_node)

    
    def __search_control(self,mode,node,data=0):
        if mode == "Normal":
            if data == node.node_data:
                return node
            elif node.left_node is None and node.right_node is None:
                pass
            elif data < node.node_data and node.left_node is not None:
                return self.__search_control(mode,node.left_node,data)
            elif data > node.node_data and node.right_node is not None:
                return self.__search_control(mode,node.right_node,data)
            return 
        elif mode == "max":
            if node.right_node is None:
                return node
            else:
                return  self.__search_control("max",node.right_node)
        elif mode == "min":
            if node.left_node is None:
                return node
            else:
                return  self.__search_control("min",node.left_node)

                
    @check_root_node
    def search(self,data,*args):
        result = self.__search_control("Normal",self.root_node,data)
        if result is None:
            print("False! Doesn't exist.")
        else:
            print("True exist in depth={}.".format(result.depth))
 
        
    @check_root_node
    def search_max(self):
        result = self.__search_control("max",self.root_node)
        print("Exist in depth={} value={}.".format(result.depth,result.node_data))


    @check_root_node
    def search_min(self):
        result = self.__search_control("min",self.root_node)
        print("Exist in depth={} value={}.".format(result.depth,result.node_data))

    
    def __judge_left_or_right_clean(self,node):       
        if node.node_data < node.past_node.node_data:
            node.past_node.left_node = None
        else:
            node.past_node.right_node = None
    
    def __judge_left_or_right_replace(self,node,new):
        if node.node_data < node.past_node.node_data:
            node.past_node.left_node = new
        else:
            node.past_node.right_node = new
        new.past_node = node.past_node
    
    def __reset_depth(self,node):
        if node is None:
            return 
        if node.left_node is None and node.right_node is None:
            self.depth_count[str(node.depth)]-=1
            if node.depth == self.total_depth:
                if self.depth_count[str(node.depth)] == 0:
                    self.total_depth-=1
                    del self.depth_count[str(node.depth)]
        elif node.left_node is not None and node.right_node is not None:
            self.depth_count[str(node.depth)]+=1
        node.depth-=1
        self.__reset_depth(node.left_node)
        self.__reset_depth(node.right_node)
    
    
    def __replace_set(self,old_node,new_node):
        new_node.left_node = old_node.left_node
        new_node.right_node = old_node.right_node
        new_node.depth = old_node.depth            
        new_node.left_node.past_node = new_node
        new_node.right_node.past_node = new_node
    
        
    def __del_node(self,node_deleted):       
        if node_deleted.left_node is None and node_deleted.right_node is None:
            self.__judge_left_or_right_clean(node_deleted)
            self.__reset_depth(node_deleted)
        elif node_deleted.left_node is not None and node_deleted.right_node is None:
            self.__judge_left_or_right_replace(node_deleted,node_deleted.left_node)
            self.__reset_depth(node_deleted.left_node)
        elif node_deleted.left_node is None and node_deleted.right_node is not None:
            self.__judge_left_or_right_replace(node_deleted,node_deleted.right_node)
            self.__reset_depth(node_deleted.right_node)
        else:
            replce_node = self.__search_control("max",node_deleted.left_node)
            if replce_node.depth - node_deleted.depth == 1:
                self.__judge_left_or_right_replace(node_deleted,replce_node)
                self.__reset_depth(node_deleted.left_node)
                replce_node.right_node = node_deleted.right_node
                replce_node.right_node.past_node = replce_node
            else:
                if node_deleted is self.root_node:
                    self.__del_node(replce_node)
                    self.__replace_set(node_deleted,replce_node)
                    replce_node.past_node = None
                    self.root_node = replce_node
                else:
                    self.__del_node(replce_node)
                    self.__judge_left_or_right_replace(node_deleted,replce_node)
                    self.__replace_set(node_deleted,replce_node)

            
    @check_root_node
    def delete(self,data,*args):        
        node_deleted = self.__search_control("Normal",self.root_node,data)
        if node_deleted is None:
            print("False! Doesn't exist.")
        else:
            self.__del_node(node_deleted)
            
     
    def __show_node(self,node,left,right):   
        print("{} -> left_node({})".format(node,left))
        print("{} -> right_node({})".format(node,right))

    
    def __next_node_check(self,node,show_depth):
        if node is None:
            return
        elif node.left_node is None and node.right_node is None:
            return
        elif node.left_node is not None and node.right_node is None:
            self.__show_node(node.node_data,node.left_node.node_data,None)
            if show_depth:
                print(node.depth,node.left_node.depth)
        elif node.left_node is None and node.right_node is not None:
            self.__show_node(node.node_data,None,node.right_node.node_data)
            if show_depth:
                print(node.depth,node.right_node.depth)
        else:
            self.__show_node(node.node_data,node.left_node.node_data,node.right_node.node_data)
            if show_depth:
                print(node.depth,node.left_node.depth,node.right_node.depth)
        self.__next_node_check(node.left_node,show_depth)
        self.__next_node_check(node.right_node,show_depth)

    
    @check_root_node
    def show(self,show_depth=False):
        print("{}是root_node".format(self.root_node.node_data))
        self.__next_node_check(self.root_node,show_depth)
        