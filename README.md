# 緣由
在學習演算法時，了解到二元搜尋樹的存在，便開始思索如何實現，一開始打算使用串列、字典來實現，但越想越覺得不對勁，可行性低又過
於複雜，在毫無頭緒的情況下，決定求助於網路尋找實現方法，發現可以使用類別的方式實現，在了解基本的邏輯後，開始獨自設計編寫程式碼，
在編寫的過程中，對於何謂物件導向有了更深的體會，也認知到原來類別還可以這樣使用!
# 開始使用
首先使用我編寫的類別建立物件，而這個物件便是一個二元搜尋樹。例如:
```
tree = BinarySearchTree()
```
### 插入新值(節點)
![](/structure.jpg)\
以上圖的結構為例:
```
for i in [50,40,20,25,45,60,55,70,80]:
    tree.insert(i)
```
我在設計時，深度是從根節點開始，起始值為0。
### 查看總深度及各層的節點數量
```
print(tree.total_depth)   #查看總深度
print(tree.depth_count)   #查看各層的節點數量
"""
輸出:
3                         ->int
{'1': 2, '2': 4, '3': 2}  ->dict,鍵:第depth層,值:對應總節點數
""
```
### 查看整體結構
```
tree.show()
print("---------------------------")
tree.show(True)    #接受一個參數,True:印出各節點所在depth值,False(預設值):不印出depth值,
"""
輸出:
50是root_node
50 -> left_node(40)
50 -> right_node(60)
40 -> left_node(20)
40 -> right_node(45)
20 -> left_node(None)   ->None表示沒有節點
20 -> right_node(25)
60 -> left_node(55)
60 -> right_node(70)
70 -> left_node(None)
70 -> right_node(80)
---------------------------
50是root_node
50 -> left_node(40)
50 -> right_node(60)
0 1 1                ->由左至右:50,40,60節點對應depth值
40 -> left_node(20)
40 -> right_node(45)
1 2 2
20 -> left_node(None)
20 -> right_node(25)
2 3                  ->由左至右:20,25節點對應depth值
60 -> left_node(55)
60 -> right_node(70)
1 2 2
70 -> left_node(None)
70 -> right_node(80)
2 3                 
"""
```
### 搜尋值
搜尋單一值:
```
tree.search(20)
tree.search(100)
"""
輸出:
True exist in depth=2.    
False! Doesn't exist.   ->被搜尋的值不存在
"""
```
搜尋最大值:
```
tree.search_max()
"""
輸出:
Exist in depth=3 value=80.
"""
```
搜尋最小值:
```
tree.search_min()
"""
輸出:
Exist in depth=2 value=20.
"""
```
### 刪除值
```
tree.delete(40)
tree.show()
print(tree.depth_count)
"""
輸出:
50是root_node
50 -> left_node(25)
50 -> right_node(60)
25 -> left_node(20)
25 -> right_node(45)
60 -> left_node(55)
60 -> right_node(70)
70 -> left_node(None)
70 -> right_node(80)
{'1': 2, '2': 4, '3': 1}
"""
```
可以看到node(40)確實被刪除，並被node(25)取代。而且第depth=3層的總節點數也更新了。\
更多驗證:
```
tree.delete(20)
tree.show()
print(tree.depth_count)
"""
輸出:
50是root_node
50 -> left_node(40)
50 -> right_node(60)
40 -> left_node(25)
40 -> right_node(45)
60 -> left_node(55)
60 -> right_node(70)
70 -> left_node(None)
70 -> right_node(80)
{'1': 2, '2': 4, '3': 1}
"""
```
```
tree.delete(60)
tree.show()
print(tree.depth_count)
"""
輸出:
50是root_node
50 -> left_node(40)
50 -> right_node(55)
40 -> left_node(20)
40 -> right_node(45)
20 -> left_node(None)
20 -> right_node(25)
55 -> left_node(None)
55 -> right_node(70)
70 -> left_node(None)
70 -> right_node(80)
{'1': 2, '2': 3, '3': 2}
"""
```
```
tree.delete(25)
tree.delete(80)
tree.show()
print(tree.depth_count)
print(tree.total_depth)
"""
輸出:
50是root_node
50 -> left_node(40)
50 -> right_node(60)
40 -> left_node(20)
40 -> right_node(45)
60 -> left_node(55)
60 -> right_node(70)
{'1': 2, '2': 4}
2
"""
```
