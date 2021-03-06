1. 创建数据库
```
-- 如果存在名为school的数据库就删除它
drop database if exists school;

-- 创建名为school的数据库并设置默认的字符集和排序方式
create database school default charset utf8;

-- 切换到school数据库上下文环境
use school;

-- 创建学院表
create table tb_college
(
collid		int auto_increment comment '编号',
collname	varchar(50) not null comment '名称',
intro	    varchar(500) default '' comment '介绍',
primary key (collid)
);

-- 创建学生表
create table tb_student
(
stuid		int not null comment '学号',
stuname		varchar(20) not null comment '姓名',
sex		    boolean default 1 comment '性别',
birth	    date not null comment '出生日期',
addr		varchar(255) default '' comment '籍贯',
collid		int not null comment '所属学院',
primary key (stuid),
foreign key (collid) references tb_college (collid)
);

-- 添加外键约束
alter table tb_student add constraint fk_student_collid foreign key (collid) references tb_college (collid);

-- 创建教师表
create table tb_teacher
(
teaid		int not null comment '工号',
teaname		varchar(20) not null comment '姓名',
title	varchar(10) default '助教' comment '职称',
collid		int not null comment '所属学院',
primary key (teaid),
foreign key (collid) references tb_college (collid)
);

alter table tb_teacher add constraint fk_teacher_collid foreign key (collid) references tb_college;

-- 创建课程表
create table tb_course
(
couid		int not null comment '编号',
couname		varchar(50) not null comment '名称',
credit	    int not null comment '学分',
teaid		int not null comment '授课老师',
primary key (couid),
foreign key (teaid) references tb_teacher (teaid)
);

-- 添加外键约束
alter table tb_course add constraint fk_course_teaid foreign key (teaid) references tb_teacher (teaid);

-- 创建选课记录表
create table tb_record
(
recid		int auto_increment comment '选课记录编号',
sid			int not null comment '选课学生',
cid			int not null comment '所选课程',
seldate		datetime default now() comment '选课时间日期',
score		decimal(4,1) comment '考试成绩',
primary key (recid),
foreign key (sid) references tb_student (stuid),
foreign key (cid) references tb_course (couid),
unique (sid, cid)
);

alter table tb_record add constraint uni_record_sid_cid unique(sid,cid);
```

2. 创建数据
```
-- 插入学院数据
insert into tb_college (collname) values 
('计算机学院'),
('外国语学院'),
('经济管理学院');

-- 插入学生数据
insert into tb_student (stuid, stuname, sex, birth, addr, collid) values
(1001, '杨逍', 1, '1990-3-4', '四川成都', 1),
(1002, '任我行', 1, '1992-2-2', '湖南长沙', 1),
(1033, '王语嫣', 0, '1989-12-3', '四川成都', 1),
(1572, '岳不群', 1, '1993-7-19', '陕西咸阳', 1),
(1378, '纪嫣然', 0, '1995-8-12', '四川绵阳', 1),
(1954, '林平之', 1, '1994-9-20', '福建莆田', 1),
(2035, '东方不败', 1, '1988-6-30', null, 2),
(3011, '林震南', 1, '1985-12-12', '福建莆田', 3),
(3755, '项少龙', 1, '1993-1-25', null, 3),
(3923, '杨不悔', 0, '1985-4-17', '四川成都', 3),
(4040, '隔壁老王', 1, '1989-1-1', '四川成都', 2);

-- 删除学生数据
delete from tb_student where stuid=4040;

-- 更新学生数据
update tb_student set stuname='杨过', addr='湖南长沙' where stuid=1001;

-- 插入老师数据
insert into tb_teacher (teaid, teaname, title, collid) values 
(1122, '张三丰', '教授', 1),
(1133, '宋远桥', '副教授', 1),
(1144, '杨逍', '副教授', 1),
(2255, '范遥', '副教授', 2),
(3366, '韦一笑', '讲师', 3);

-- 插入课程数据
insert into tb_course (couid, couname, credit, teaid) values 
(1111, 'Python程序设计', 3, 1122),
(2222, 'Web前端开发', 2, 1122),
(3333, '操作系统', 4, 1122),
(4444, '计算机网络', 2, 1133),
(5555, '编译原理', 4, 1144),
(6666, '算法和数据结构', 3, 1144),
(7777, '经贸法语', 3, 2255),
(8888, '成本会计', 2, 3366),
(9999, '审计学', 3, 3366);

-- 插入选课数据
insert into tb_record (sid, cid, seldate, score) values 
(1001, 1111, '2017-09-01', 95),
(1001, 2222, '2017-09-01', 87.5),
(1001, 3333, '2017-09-01', 100),
(1001, 4444, '2018-09-03', null),
(1001, 6666, '2017-09-02', 100),
(1002, 1111, '2017-09-03', 65),
(1002, 5555, '2017-09-01', 42),
(1033, 1111, '2017-09-03', 92.5),
(1033, 4444, '2017-09-01', 78),
(1033, 5555, '2017-09-01', 82.5),
(1572, 1111, '2017-09-02', 78),
(1378, 1111, '2017-09-05', 82),
(1378, 7777, '2017-09-02', 65.5),
(2035, 7777, '2018-09-03', 88),
(2035, 9999, default, null),
(3755, 1111, default, null),
(3755, 8888, default, null),
(3755, 9999, '2017-09-01', 92);
```

3. 基本操作
```
-- 查询所有学生信息
select * from tb_student;
-- 查询所有老师信息
select * from tb_teacher;
-- 查询所有课程信息
select * from tb_course;

-- 查询所有课程名称及学分(投影和别名)
select couname, credit from tb_course;

-- 查询所有学生的姓名和性别(投影和别名)
select stuname as 姓名, sex as 性别 from tb_student;

select stuname as 姓名, case sex when 1 then '男' else '女' end as 性别 from tb_student;

select stuname as 姓名, if(sex, '男', '女') as 性别 from tb_student;

-- 查询老师的姓名和职称 concat() 将字符串连接起来
select concat(teaname, title) as 全称 from tb_teacher;

-- 查询所有女学生的姓名和出生日期(筛选)
select stuname, birth from tb_student where sex=0;

-- 查询女学生的姓名和年龄 floor()向下取整 / ceil()向上取整 /datediff()计算时间函数
select stuname as 姓名, floor(datediff(now(), birth)/365) as 年龄 from tb_student where sex=0;

-- 查询所有80后学生的姓名、性别和出生日期(筛选)
select stuname, sex, birth from tb_student where birth>='1980-1-1' and birth<='1989-12-31';

select stuname, sex, birth from tb_student where birth between '1980-1-1' and '1989-12-31';

-- 查询姓”杨“的学生姓名和性别(模糊)
select stuname, sex from tb_student where stuname like '杨%';

-- 查询姓”杨“名字两个字的学生姓名和性别(模糊)
select stuname, sex from tb_student where stuname like '杨_';

-- 查询姓”杨“名字三个字的学生姓名和性别(模糊)
select stuname, sex from tb_student where stuname like '杨__';

-- 查询名字中有”不“字或“嫣”字的学生的姓名(模糊)
select stuname from tb_student where stuname like '%不%' or stuname like '%嫣%';

-- 查询没有录入家庭住址的学生姓名(空值)
select stuname from tb_student where addr is null;

-- 查询录入了家庭住址的学生姓名(空值)
select stuname from tb_student where addr is not null;

-- 查询学生选课的所有日期(去重)
select distinct seldate from tb_record;

-- 查询学生的家庭住址(去重)
select distinct addr from tb_student where addr is not null;

-- 查询男学生的姓名和生日按年龄从大到小排列(排序)
select stuname, birth, floor(datediff(now(), birth)/365) as age from tb_student where sex=1 order by age desc;

select stuname, birth from tb_student order by sex asc, birth desc;

-- max / min / sum / avg / count
-- 查询年龄最大的学生的出生日期(聚合函数)
select min(birth) from tb_student;

-- 查询年龄最小的学生的出生日期(聚合函数)
select max(birth) from tb_student;

-- 查询男女学生的人数(分组和聚合函数)
select if(sex, '男', '女') as 性别, count(stuid) as 人数 from tb_student group by sex;

select '男' as 性别, count(stuid) as 人数 from tb_student where sex=1
union
select '女' as 性别, count(stuid) as 人数 from tb_student where sex=0;

-- 统计学生的籍贯和人数
select addr, count(stuid) as total from tb_student where addr is not null group by addr order by total desc;

-- 查询课程编号为1111的课程的平均成绩(筛选和聚合函数)
select count(cid) from tb_record where cid=1111;
select count(score) from tb_record where cid=1111;
select avg(score) from tb_record where cid=1111;

-- 查询学号为1001的学生所有课程的平均分(筛选和聚合函数)
select avg(score) from tb_record where sid=1001;

-- 查询每个学生的学号和平均成绩(分组和聚合函数)
select sid, avg(score) from tb_record group by sid;

-- 查询平均成绩大于等于90分的学生的学号和平均成绩
-- where子句代表分组以前的筛选，所以写在group by子句的前面
-- having子句代表分组以后的筛选，所以写在group by子句的后面
select sid, avg(score) as avgscore from tb_record group by sid having avgscore>=90 order by avgscore desc;

-- 查询年龄最大的学生的姓名(子查询/嵌套查询)
-- 把一个查询的结果作为另外一个查询的一部分来使用
select stuname from tb_student where birth=(
select min(birth) from tb_student);

-- 查询选了两门以上的课程的学生姓名(子查询/分组条件/集合运算)
select stuname from tb_student where stuid in (select sid from tb_record group by sid having count(sid)>2);

-- 查询学生姓名、课程名称以及成绩(连接查询)
-- 如果没有连接条件会形成笛卡尔积
select stuname, couname, score from tb_student, tb_course, tb_record where stuid=sid and couid=cid;

select stuname, couname, score from tb_student inner join tb_record on stuid=sid inner join tb_course on couid=cid;

-- 查询选课学生的姓名和平均成绩(子查询和连接查询)
select stuname, avgscore from tb_student t1 inner join 
(select sid, avg(score) as avgscore from tb_record group by sid) t2 on stuid=sid;

-- 查询每个学生的姓名和选课数量(左外连接和子查询)
-- left outer join 左表（写在前面的表）不满足连表条件的列用null进行填充 / right outer join 右表（写在后面的表）不满足连表条件的列用null填充 / full outer join 全外连接（MySQL不支持）
select stuname, ifnull(total, 0) as total from tb_student t1 left join (select sid, count(sid) as total from tb_record group by sid) t2 on stuid=sid order by total desc limit 5 offset 3;
-- limit 3, 5;
```