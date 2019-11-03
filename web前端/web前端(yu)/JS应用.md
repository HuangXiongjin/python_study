# JS应用   

## 1. 原生js

### 1.1 DOM操作

#### 节点操作 - 获取节点

**1.直接获取节点**

a.通过标签的id值来获取指定的标签: document.getElementById(id值)

b.通过标签名来获取指定的标签:  document.getElementsByTagName(标签名)

c.通过类名来获取指定的标签:  document.getElementsByClassName(类名)  

d.通过name属性的值来获取指定的标签(了解):  document.getElementsByName('username')

 **2.获取父节点**  

a.获取子节点对应的父节点:  子节点.parentElement  

**3.获取子节点**  

a.获取所有的子节点:  父节点.children  / 父节点.childNodes

b.获取第一个子节点:  父节点.firstElementChild  

c.获取最后一个子节点: 父节点.lastElementChild  



### 节点操作 - 创建添加和删除  

1.创建节点:  document.createElement(标签名)

2.添加节点:  父节点.appendChild(需要添加的节点)  /  父节点.insertBefore(新节点, 指定节点)

3.删除节点:  父节点.removeChild(子节点)  /  节点.remove()

4.拷贝节点:  节点.cloneNode()  /  节点.cloneNode(true)  

5.替换节点:  父节点.replaceChild(新节点, 子节点)



练习: 删除广告、动态添加和删除

作业: 成都汽车限号查询



### 1.2 BOM操作  

**1.window基本操作**  

a.打开新窗口：window.open(网页地址) / window.open('','','width=x?,height=y?')  

b.关闭窗口:  window.close()  

c.移动当前窗口: 窗口对象.moveTo(x坐标, y坐标)  

d.获取浏览器的宽度和高度:  window.innerWidth, window.innerHeight / window.outerWidth, window.outerHeight  

**2.弹框**

a.  alert(提示信息) - 弹出提示信息(带确定按钮)

b. confirm(提示信息) - 弹出提示信息(带确定和取消按钮),返回值是布尔值，取消-false, 确定-true

c. prompt(提示信息,输入框中的默认值) - 弹出一个带输入框和取消，确定按钮的提示框; 点取消，返回值是null;点确定返回值是输入框中输入的内容  

**3.定时**  

a.  setInterval(函数,时间)  /  clearInterval(定时对象)  

b. setTimeout(函数,时间) / clearTimeout(定时对象)  

### 1.3 事件

**1.事件绑定**

a.  在标签内部给事件源的事件属性赋值  

b. 通过节点绑定事件1:  标签节点.事件属性 = 函数  

c. 通过节点绑定事件2:  标签节点.事件属性 = 匿名函数  

d. 通过节点绑定事件3:  节点.addEventListener(事件名,函数)  



**2.常见事件类型**  

a..onload - 页面加载完成对应的事件(标签加载成功)

window.onload = 函数

b.鼠标事件:  onclick  / onmouseover / onmouseout

c.键盘事件:  onkeypress / onkeydown / onkeyup

d.输入框内容改变:  'onchange' - 输入框输入状态结束



**3.事件捕获**

事件对象.stopPropagation()



## 2. jQuery

### 2.1 基本操作

===========节点=============

1.获取节点

$(选择器)   

console.log($('#div2>a'))  	 //和后代选择器效果一样

console.log($('p + a'))   		//获取紧跟着p标签的a标签

console.log($('#p1~*'))   		//获取和id是p1的标签的后面的所有同级标签

console.log($('div:first'))  	 //第一个div标签

console.log($('p:last'))   		  //最后一个p标签

console.log($('div *:first-child'))   		//找到所有div标签中的第一个子标签   



2.创建标签  

$('HTML标签语法') ,例如：$('<div style="color: red">我是div</div>')  


3.添加标签  

父标签.append(子标签) - 在父标签的最后添加子标签

父标签.prepend(子标签) - 在父标签的最前面添加子标签

标签.before()

标签.after()  


4.删除标签

标签.empty() - 清空指定标签

标签.remove() - 删除指定标签  


==============属性================

1.普通属性的获取和修改 - 除了innerHTML(html),    innerText(text)以及value(val)

标签.attr(属性名)  - 获取指定的属性值

标签.attr(属性名, 值) - 修改/添加属性  

//2.标签内容属性
// 双标签.html()
// 双标签.text()
// 单标签.val()
//注意：上面的函数不传参就是获取值，传参就是修改值



2.class属性 - HTML中一个标签可以有多个class值，多个值用空格隔开

标签.addClass(class值) - 给标签添加class值

标签.removeClass(class值) - 移除标签中指定的class值  



3.样式属性  

a.获取属性值

标签.css(样式属性名) - 获取样式属性值 

b.修改和添加

标签.css(样式属性名, 值) - 修改属性值

标签.css({属性名:值, 属性名2:值2...}) - 同时设置多个属性



==============事件=============

1.标签.on(事件名,回调函数) - 给标签绑定指定的事件（和js中的addEventLinsenner一样）

事件名不需要要on


2.父标签.on(事件名,选择器,回调函数) - 在父标签上添加事件，传递给选择器对应的子标签

选择器 - 前面标签的后代标签(子标签/子标签的子标签)



### 2.2 Ajax

语法：

​	1.get请求

​	$.get(url,data,回调函数,返回数据类型)  

​	- url：请求地址（字符串）

​	- data：参数列表 (对象)

​	- 回调函数：请求成功后自动调用的函数(函数名，匿名函数)

​	- 返回数据类型：请求到的数据的格式(字符串，例如：'json')  

​	

​	2.post请求

​	$.post(url,data,回调函数,返回数据类型)  

​	- url：请求地址（字符串）

​	- data：参数列表 (对象)

​	- 回调函数：请求成功后自动调用的函数(函数名，匿名函数)

​	- 返回数据类型：请求到的数据的格式(字符串，例如：'json')  

​	

​	3.ajax

​	$.ajax({

​		'url':请求地址,

​		'data':{参数名1:值1, 参数名2:值2}，

​		'type':'get'/'post',

​		'dataType':返回数据类型,

​		'success':function(结果){

​			请求成功后要做的事情

​		}

​	})





## 3. Vue.js