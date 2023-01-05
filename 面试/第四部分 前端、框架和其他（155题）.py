#-*- encoding: utf-8 -*-
# 1、谈谈你对http协议的认识。
#
# 2、谈谈你对websocket协议的认识。
#
# 3、什么是magic
# string ？
#
# 4、如何创建响应式布局？
#
# 5、你曾经使用过哪些前端框架？
#
# 6、什么是ajax请求？并使用jQuery和XMLHttpRequest对象实现一个ajax请求。
#
# 7、如何在前端实现轮训？
#
# 8、如何在前端实现长轮训？
#
# 9、vuex的作用？
#
# 10、vue中的路由的拦截器的作用？
#
# 11、axios的作用？
#
# 12、列举vue的常见指令。
#
# 13、简述jsonp及实现原理？
#
# 14、是什么cors ？
#
# 15、列举Http请求中常见的请求方式？
#
# 16、列举Http请求中的状态码？
#
# 17、列举Http请求中常见的请求头？
#
# 18、看图写结果：
#
# 2
# b741a2efd88dc3c298087e0e7d988a4.png
#
# 19、看图写结果：
#
# 3
# b98cac1b5ba53e30a4130c0e93af103.png
#
# 20、看图写结果：
#
# c77d19b207050ee086b2576229f850c0.png
#
# 21、看图写结果：
#
# c0a0cdbc63fce75df509ff10d146014e.png
#
# 22、看图写结果：
#
# 9223685
# d58e189866ebc6c856864fdfd.png
#
# 23、看图写结果：
#
# d4189728bfd86ab3202c35562f6d6ade.png
#
# 24、django、flask、tornado框架的比较？
#
# 25、什么是wsgi？
#
# 26、django请求的生命周期？
#
# 27、列举django的内置组件？
#
# 28、列举django中间件的5个方法？以及django中间件的应用场景？
#
# 29、简述什么是FBV和CBV？
#
# 30、django的request对象是在什么时候创建的？
#
# 31、如何给CBV的程序添加装饰器？
#
# 32、列举django
# orm
# 中所有的方法（QuerySet对象的所有方法）
#
# 33、only和defer的区别？
#
# 34、select_related和prefetch_related的区别？
#
# 35、filter和exclude的区别？
#
# 36、列举django
# orm中三种能写sql语句的方法。
#
# 37、django
# orm
# 中如何设置读写分离？
#
# 38、F和Q的作用?
#
# 39、values和values_list的区别？
#
# 40、如何使用django
# orm批量创建数据？
#
# 41、django的Form和ModeForm的作用？
#
# 42、django的Form组件中，如果字段中包含choices参数，请使用两种方式实现数据源实时更新。
#
# 43、django的Model中的ForeignKey字段中的on_delete参数有什么作用？
#
# 44、django中csrf的实现机制？
#
# 45、django如何实现websocket？
#
# 46、基于django使用ajax发送post请求时，都可以使用哪种方法携带csrf
# token？
#
# 47、django中如何实现orm表中添加数据时创建一条日志记录。
#
# 48、django缓存如何设置？
#
# 49、django的缓存能使用redis吗？如果可以的话，如何配置？
#
# 50、django路由系统中name的作用？
#
# 51、django的模板中filter和simple_tag的区别？
#
# 52、django - debug - toolbar的作用？
#
# 53、django中如何实现单元测试？
#
# 54、解释orm中
# db
# first
# 和
# code
# first的含义？
#
# 55、django中如何根据数据库表生成model中的类？
#
# 56、使用orm和原生sql的优缺点？
#
# 57、简述MVC和MTV
#
# 58、django的contenttype组件的作用？
#
# 59、谈谈你对restfull
# 规范的认识？
#
# 60、接口的幂等性是什么意思？
#
# 61、什么是RPC？
#
# 62、Http和Https的区别？
#
# 63、为什么要使用django
# rest
# framework框架？
#
# 64、django
# rest
# framework框架中都有那些组件？
#
# 65、django
# rest
# framework框架中的视图都可以继承哪些类？
#
# 66、简述
# django
# rest
# framework框架的认证流程。
#
# 67、django
# rest
# framework如何实现的用户访问频率控制？
#
# 68、Flask框架的优势？
#
# 69、Flask框架依赖组件？
#
# 70、Flask蓝图的作用？
#
# 71、列举使用过的Flask第三方组件？
#
# 72、简述Flask上下文管理流程?
#
# 73、Flask中的g的作用？
#
# 74、Flask中上下文管理主要涉及到了那些相关的类？并描述类主要作用？
#
# 75、为什么要Flask把Local对象中的的值stack
# 维护成一个列表？
#
# 76、Flask中多app应用是怎么完成？
#
# 77、在Flask中实现WebSocket需要什么组件？
#
# 78、wtforms组件的作用？
#
# 79、Flask框架默认session处理机制？
#
# 80、解释Flask框架中的Local对象和threading.local对象的区别？
#
# 81、Flask中
# blinker
# 是什么？
#
# 82、SQLAlchemy中的
# session和scoped_session
# 的区别？
#
# 83、SQLAlchemy如何执行原生SQL？
#
# 84、ORM的实现原理？
#
# 85、DBUtils模块的作用？
#
# 86、以下SQLAlchemy的字段是否正确？如果不正确请更正：
#
# from datetime import datetime
# from sqlalchemy.ext.declarative
# import declarative_base
# from sqlalchemy import Column, Integer, String, DateTime
#
# Base = declarative_base()
#
#
# class UserInfo(Base):
#     __tablename__ = 'userinfo'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(64), unique=True)
#     ctime = Column(DateTime, default=datetime.now())
#
#
# 87、SQLAchemy中如何为表设置引擎和字符编码？
#
# 88、SQLAchemy中如何设置联合唯一索引？
#
# 89、简述Tornado框架的特点。
#
# 90、简述Tornado框架中Future对象的作用？
#
# 91、Tornado框架中如何编写WebSocket程序？
#
# 92、Tornado中静态文件是如何处理的？如： < link
# href = "{{static_url("
# commons.css
# ")}}"
# rel = "stylesheet" / >
#
# 93、Tornado操作MySQL使用的模块？
#
# 94、Tornado操作redis使用的模块？
#
# 95、简述Tornado框架的适用场景？
#
# 96、git常见命令作用：
#
# 97、简述以下git中stash命令作用以及相关其他命令。
#
# 98、git
# 中
# merge
# 和
# rebase命令
# 的区别。
#
# 99、公司如何基于git做的协同开发？
#
# 100、如何基于git实现代码review？
#
# 101、git如何实现v1
# .0 、v2
# .0
# 等版本的管理？
#
# 102、什么是gitlab？
#
# 103、github和gitlab的区别？
#
# 104、如何为github上牛逼的开源项目贡献代码？
#
# 105、git中.gitignore文件的作用?
#
# 106、什么是敏捷开发？
#
# 107、简述
# jenkins
# 工具的作用?
#
# 108、公司如何实现代码发布？
#
# 109、简述
# RabbitMQ、Kafka、ZeroMQ的区别？
#
# 110、RabbitMQ如何在消费者获取任务后未处理完前就挂掉时，保证数据不丢失？
#
# 111、RabbitMQ如何对消息做持久化？
#
# 112、RabbitMQ如何控制消息被消费的顺序？
#
# 113、以下RabbitMQ的exchange
# type分别代表什么意思？如：fanout、direct、topic。
#
# 114、简述
# celery
# 是什么以及应用场景？
#
# 115、简述celery运行机制。
#
# 116、celery如何实现定时任务？
#
# 117、简述
# celery多任务结构目录？
#
# 118、celery中装饰器 @ app.task
# 和 @ shared_task的区别？
#
# 119、简述
# requests模块的作用及基本使用？
#
# 120、简述
# beautifulsoup模块的作用及基本使用？
#
# 121、简述
# seleninu模块的作用及基本使用?
#
# 122、scrapy框架中各组件的工作流程？
#
# 123、在scrapy框架中如何设置代理（两种方法）？
#
# 124、scrapy框架中如何实现大文件的下载？
#
# 125、scrapy中如何实现限速？
#
# 126、scrapy中如何实现暂定爬虫？
#
# 127、scrapy中如何进行自定制命令？
#
# 128、scrapy中如何实现的记录爬虫的深度？
#
# 129、scrapy中的pipelines工作原理？
#
# 130、scrapy的pipelines如何丢弃一个item对象？
#
# 131、简述scrapy中爬虫中间件和下载中间件的作用？
#
# 132、scrapy - redis组件的作用？
#
# 133、scrapy - redis组件中如何实现的任务的去重？
#
# 134、scrapy - redis的调度器如何实现任务的深度优先和广度优先？
#
# 135、简述
# vitualenv
# 及应用场景?
#
# 136、简述
# pipreqs
# 及应用场景？
#
# 137、在Python中使用过什么代码检查工具？
#
# 138、简述
# saltstack、ansible、fabric、puppet工具的作用？
#
# 139、B
# Tree和B + Tree的区别？
#
# 140、请列举常见排序并通过代码实现任意三种。
#
# 141、请列举常见查找并通过代码实现任意三种。
#
# 142、请列举你熟悉的设计模式？
#
# 143、有没有刷过leetcode？
#
# 144、列举熟悉的的Linux命令。
#
# 145、公司线上服务器是什么系统？
#
# 146、解释
# PV、UV
# 的含义？
#
# 147、解释
# QPS的含义？
#
# 148、uwsgi和wsgi的区别？
#
# 149、supervisor的作用？
#
# 150、什么是反向代理？
#
# 151、简述SSH的整个过程。
#
# 152、有问题都去那些找解决方案？
#
# 153、是否有关注什么技术类的公众号？
#
# 154、最近在研究什么新技术？
#
# 155、是否了解过领域驱动模型？