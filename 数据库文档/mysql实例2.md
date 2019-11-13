```
drop database if exists hrs;

create database hrs default charset utf8;

create table tb_dept
(
dno int not null comment '编号',
dname varchar(10) not null comment '名称',
dloc varchar(20) not null comment '所在地',
primary key (dno)
);

insert into tb_dept values 
	(10, '会计部', '北京'),
	(20, '研发部', '成都'),
	(30, '销售部', '重庆'),
	(40, '运维部', '深圳');

create table tb_emp
(
eno int not null comment '员工编号',
ename varchar(20) not null comment '员工姓名',
job varchar(20) not null comment '员工职位',
mgr int comment '主管编号',
sal int not null comment '员工月薪',
comm int comment '每月补贴',
dno int comment '所在部门编号',
primary key (eno )
);

--constraint 约束，添加外键约束 fk_emp_dno 是自己指定的约束名称
alter table tb_emp add constraint fk_emp_dno foreign key (dno) references tb_dept (dno);

insert into tb_emp values 
	(7800, '张三丰', '总裁', null, 9000, 1200, 20),
	(2056, '乔峰', '分析师', 7800, 5000, 1500, 20),
	(3088, '李莫愁', '设计师', 2056, 3500, 800, 20),
	(3211, '张无忌', '程序员', 2056, 3200, null, 20),
	(3233, '丘处机', '程序员', 2056, 3400, null, 20),
	(3251, '张翠山', '程序员', 2056, 4000, null, 20),
	(5566, '宋远桥', '会计师', 7800, 4000, 1000, 10),
	(5234, '郭靖', '出纳', 5566, 2000, null, 10),
	(3344, '黄蓉', '销售主管', 7800, 3000, 800, 30),
	(1359, '胡一刀', '销售员', 3344, 1800, 200, 30),
	(4466, '苗人凤', '销售员', 3344, 2500, null, 30),
	(3244, '欧阳锋', '程序员', 3088, 3200, null, 20),
	(3577, '杨过', '会计', 5566, 2200, null, 10),
	(3588, '朱九真', '会计', 5566, 2500, null, 10);


-- 查询月薪最高的员工姓名和工资
select ename as 姓名, sal 工资 from tb_emp where  sal=(select  max(sal ) from tb_emp );


-- 查询员工的姓名和年薪((月薪+补贴)*13)
select ename as 姓名, (sal+ifnull(comm, 0))*13 as 年薪 from tb_emp order by 年薪 desc;


-- 查询有员工的部门的编号和人数
select dno, count(eno) from tb_emp group by dno;
--
select dno, count(dno) from tb_emp group by dno;

-- 查询所有部门的名称和人数
select dname, total from tb_dept t1 left join (select dno, count(eno) as total from tb_emp group by dno)
t2 on t1.dno=t2.dno;

-- 查询月薪最高的员工(Boss除外)的姓名和月薪
select ename, sal from tb_emp where sal=(select max(sal) from tb_emp where mgr is not null); 


-- 查询薪水超过平均薪水的员工的姓名和工资
select ename, sal from tb_emp where sal>(select avg(sal) from tb_emp) order by sal desc;


-- 查询薪水超过其所在部门平均薪水的员工的姓名、部门编号和工资
select ename, t1.dno,sal from tb_emp as t1 inner join (select dno, avg(sal) as avgsal from tb_emp group by dno) as t2 on t1.dno=t2.dno where sal>avgsal;

-- 查询部门中月薪最高的人姓名、工资和所在部门名称
select ename, sal, dname from tb_dept t3 inner join (select ename, sal, t1.dno from tb_emp t1 inner join (select dno,max(sal) as maxsal from tb_emp group by dno) t2 on t1.dno=t2.dno where sal=maxsal) t4 on t3.dno=t4.dno;

-- 查询主管的姓名和职位
select ename, job from tb_emp where eno in (select distinct mgr from tb_emp where mgr is not null);


-- 查询月薪排名4~6名的员工姓名和工资
select ename, sal from tb_emp order by sal desc, ename limit 3, 3;

```

