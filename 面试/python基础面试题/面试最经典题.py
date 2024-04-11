#-*- encoding: utf-8 -*-
## 问答版
# 1、TCP / UDP / HTTP / HTTPS协议区别？
    # Tcp：面向连接，是高可靠性传输层协议。发送给别人消息，对方确认收到消息才会发送下一条，没有收到会重发
    # Udp: 不可靠，数据容易丢失，无秩序的传输层协议。一直发数据，不需要回应（qq基于udp）
    # HTTP: 超文本传输协议，信息用明文传输，连接无状态。作用：是应用最广泛的一种网络协议，是一个客户端和服务端请求和应答的标准，用于从www服务器传送超文本到本地浏览器的协议
    # HTTPS：HTTP+ssl构成的可加密传输、身份认证的网络协议，比http安全。


# 3、简述一个前端请求的处理流程，在uwsgi / nginx / django之间的处理流程
    # 1 首先客户端请求服务资源，
    # 2 nginx作为直接对外的服务接口,接收到客户端发送过来的http请求,会解包、分析，
    # 3 如果是静态文件请求就根据nginx配置的静态文件目录，返回请求的资源，
    # 4 如果是动态的请求,nginx就通过配置文件,将请求传递给uWSGI；uWSGI 将接收到的包进行处理，并转发给wsgi，
    # 5 wsgi根据请求调用django工程的某个文件或函数，处理完后django将返回值交给wsgi，
    # 6 wsgi将返回值进行打包，转发给uWSGI，
    # 7 uWSGI接收后转发给nginx,nginx最终将返回值返回给客户端(如浏览器)。
    # 8 *注:不同的组件之间传递信息涉及到数据格式和协议的转换
    # 参考：https://www.cnblogs.com/makerchen/p/15364448.html

    # 扩展：django请求的生命流程
    # 请求从uWsgi里转发到django中的wsgi中----经过中间件(process_request)-----\
    # 然后匹配路由----进入相关视图函数----视图函数中进行orm获取数据---找到模版路径将模版拿到----
    # 后台进行模版渲染-----将结果返回给中间件----经过wsgi---返回给用户

# 4、redis用过哪些数据结构？怎么保存的
    # 哈希、列表、字符串、集合、有序集合
    # redis数据持久化：包含两种方式，第一种RDB快照、第二种AOF持久化。
    # 定义：RDB快照指定的时间间隔内将redis中的数据生成时间点的快照，是个dump.rdb文件；而AOF持久化是记录服务器上所有执行的操作记录，保存这个记录，在服务器重启时进行数据还原。
    # 优缺点：
    # RDB快照-优点，某时间点的数据存储的比较完整；RDB快照-缺点,数据丢失严重，由于数据量大时生成dump.rdb很耗时需要好几分钟，如果服务这会儿挂了那么就会丢失这几分钟的数据！
    # AOF-优点，耐久安全，可以设置每次执行命令就同步操作记录到日志文件里，aof文件是一个自动追加写入的文件，即使发送挂机，aof文件也不会丢失，即使磁盘满了，日志放不下了，也会自动调整日志大小，重新进行追加写入；
    # AOF-缺点-aof文件体积通常大于rdb文件体积，aof同步数据速度慢于rdb.
    # 注：这个人讲的很好 https://blog.csdn.net/weixin_52489114/article/details/123011362

# 5、celery队列
    ## celery是由，broker消息中间件，任务执行单元worker，任务结果仓库backend组成。执行流程是，首先启动celery服务，手动或者自动添加任务到broker，
    # broker将任务分发给worker，worker后台进行执行任务，执行完再将任务执行结果存储到backend中
    # https://www.cnblogs.com/louyifei0824/p/10040639.html


# 6、modelfirst与dbfirst区别？
    # Database-First模式明显性能会差点，但是它很适合初学者，或者是比较急的小型项目。还有一点，我们在做项目时可能不容易体会到它的好处，但如果做数据库结构比较成熟稳定的产品时，我们可以很轻松的使用数据库生成实体模型，从而实现快速开发。
    # Model-First模式优点是开发人员能够在模型设计完成后，可以利用VS等工具快速生成数据库脚本。缺点是设计模型时完全了解数据库的结构，在模型中手动添加表关系，并且生成的脚本有点不简洁。
    # Code-First模式优点是性能比较好，且代码较少冗余。不过它的缺点也有很多，由于都是代码编写的，比如更新数据库。

# 7、线程 / 进程 / 协程区别
    # 进程：程序运行基本单位。进程之间资源和空间独立不共享
    # 线程：cpu调度最小单元。线程之前共享所属进程的资源
    # 协程：轻量级线程。由于多线程之间实现io密集型操作切换线程时，消耗资源，协程可以解决这个问题。协程由程序调度，而不像线程和进程由操作系统调度。
    # 参考：https://www.cnblogs.com/sunlong88/p/16267055.html

# 8、tornado框架
# 9、向量化–one - hot编码 / 数据分箱
# 10、栈、堆、你知道的排序算法
# 详见-Pypro/算法/堆栈.py

# 12、MySQL优化、多表查询
    # MySQL优化:
    # 读写分离：利用数据库的主从分离，主用于删除更新，从用于查
    # 分库分表：分库-某数据库表太多，将部分的放到别的库，代价是连表查询；分表-水平分、垂直分
    # 加缓存：常用数据放到redis\memcached里

    # 扩展知识：
    # Innodb和Myisam区别：
    # Innodb支持行锁、表锁，支持事务；
    # Myisam只支持表锁，不支持事务；

    # 表锁：
        # lock table 表名 read;  -- 读锁
        # lock table 表名 write; -- 写锁
        # unlock tables; -- 释放表锁，连接断开时会自动释放表锁
    # 行锁：select name,id from user where... for update这句话，锁定特定的行，当这些符合条件的行被锁定后，其他用户只能选定而不能更改删除这些数据，直到该语句的事务被commit语句或者rollback语句结束为止。
        # select * from account lock in share mode; # 添加读锁（S 锁，共享锁）
        # select * from account for update; # 添加写锁（X 锁，排他锁）
    # 死锁：事务 A 在等待事务 B 释放 id=2 的行锁，而事务 B 在等待事务 A 释放 id=1 的行锁。
        # 解决死锁：
            # a.等待锁超时。默认超时等待时间为50s，可通过innodb_lock_wait_timeout参数来设置
            # b.死锁检测。设置参数innodb_deadlock_detect = on，开启后，系统会自动检测死锁的事务并回滚某一个事务，让其他可以事务继续执行。
    # 事务：用于将某些操作的多个sql进行原子性操作，一旦出现错误，马上会滚到开始状态，从而保证数据完整性；
    # 事务特性：原子性、一致性、隔离性、持久性

# 13、Linux下找文件
    # find /etc -name test.py 精准搜索
    # find /etc -name *test.py 模糊搜索

# 14、闭包
    # 作用域：nonlocal global
    #     def one():
    #         def two():
    #             num="11"   #在函数two的局部变量
    #         def three():
    #             nonlocal num
    #             num="22"  # 将局部函数three的变量num向上提升，数据同步
    #         def four():
    #             global num
    #             num="33"  # 将局部函数four的变量提升到全局
    #
    #         num="00"
    #         two()
    #         print(num) # 00
    #         three()
    #         print(num) # 22
    #         four()
    #         print(num) # 22
    #     one()
    #     print(num) # 33

    # 闭包：一个函数内部嵌套一个函数,内部函数可以引用外部函数的变量,会产生闭包
    # def foo():
    #     m=3
    #     n=5
    #     def bar():
    #         a=4
    #         return m+n+a
    #     return bar
    # bar =  foo()
    # bar() # 12


# 15、Django模型类继承


# 16、时间更新模型类
# 17、Settings里面设置东西
# 18、ajax请求的csrf解决方法
# 19、机器数据分析 / 建模有什么感悟？
# 20、爬虫原理
# 30、redis为什么快？除了他是内存型数据库外，还有什么原因
# 31、python2和python3的区别？
# 32、你觉得python2的项目如果迁移到python3，困难会在哪里？






## 纯问题版
# 1、TCP/UDP/HTTP协议区别？
# 2、深拷贝浅拷贝
# 3、简述一个前端请求的处理流程，在uwsgi/nginx/django之间的处理流程
# 4、redis用过哪些数据结构？怎么保存的
# 5、celery队列
# 6、modelfirst dbfirst区别？
# 7、线程/进程/协程区别
# 8、tornado框架
# 9、向量化–one-hot编码/数据分箱
# 10、栈、堆11、你知道的排序算法
# 12、MySQL优化、多表查询
# 13、Linux下找文件
# 14、闭包15、Django模型类继承
# 16、时间更新模型类
# 17、Settings里面设置东西
# 18、ajax请求的csrf解决方法
# 19、机器数据分析/建模有什么感悟？
# 20、爬虫原理
# 30、redis为什么快？除了他是内存型数据库外，还有什么原因
# 31、python2和python3的区别？
# 32、你觉得python2的项目如果迁移到python3，困难会在哪里？
