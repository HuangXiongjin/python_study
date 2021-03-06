## 列表(list)

> **定义**：列表是容器型数据类型（序列）, 将[ ]作为容器的标志，多个元素用逗号隔开。
>
> **特点**：可变的（指的列表中元素可变  -> 元素支持CRUD）
>
> ​			有序的（支持下标操作）
>
> **声明列表**：变量名 = [元素1, 元素2, 元素3,....]    [ ] -> 空列表
>
> **列表中的元素类型**：任何类型的数据都可以作为列表元素; 同一个列表中数据的类型可以不一样

### 获取列表中的元素（查）

- 获取单个元素
  a.语法: 
  列表[下标]  - 获取列表中指定下标对应的元素

  b.说明
  列表  -  结果是列表的表达式(列表数据、列表变量等)
  []  -  固定写法
  下标  -  下标又叫索引; 列表中每个元素都有固定的下标值来表示元素在列表中的位置。
           范围1: 0, 1, 2 ~ 长度-1 (从前往后的第一个元素、第二个元素、...)
           范围2: -1, -2, -3, ~ -长度 (从后往前数，倒数第一个元素，倒数第二个元素,...) 

  注意: 下标不能越界(超过范围)

- 获取部分元素(切片)
  列表切片的结果是小列表
  a.语法:
  列表[开始下标: 结束下标: 步长]  -  从开始下标开始，每次下标增加步长去取下一个元素，直到取到结束下标前为止 (在列表中获取range(开始下标,结束下标,步长)产生的数字序列作为下标的元素)

> 注意:
> 步长为正表示开始下标到结束下标是从前往后取，所以开始下标对应的元素必须在结束下标对应的元素的前面, 否则结果是[]
> 步长为负表示开始下标到结束下标是从后往前取，所以开始下标对应的元素必须在结束下标对应的元素的后面, 否则结果是[]

- 遍历

  - 直接遍历元素

    ```
    for 变量 in 列表:
        循环体
    ```

  - 通过遍历下标来遍历列表元素

    ```
    len(列表) - 获取列表中元素的个数
    for index in range(len(列表)):
        循环体
    ```

    