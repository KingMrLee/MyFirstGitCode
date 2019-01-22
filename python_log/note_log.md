# Log
- https://www.cnblogs.com/yyds/p/6901864.html
- logging
- logging模块提供模块及级别的函数记录日志
- 包括四大组件

## 1、日志相关概念
- 日志
- 日志的级别：level
    - 不同用户关注不同的程序日志信息（从上到下level越来越高）
    - DEBUG
    - INFO
    - NOTICE
    - WARNING
    - ERROR
    - CRITICAL
    - ALERT
    - EMERGENCY
- IO操作不要操作太频繁
- LOG的作用
    - 调试
    - 了解软件的运行情况
    - 分析定位问题
- 日志信息
    - time
    - 地点（对应哪个代码，哪个函数，行数）
    - level（日志级别）
    - 内容
- 成熟的第三方日志
    - log4j(java)
    - log4php(php)
    - logging(python)    

## 2、logging日志模块
- 日志级别
    - 级别可自定义（现有已够用）
    - DEBUG
    - INFO
    - WARNING
    - ERROR
    - CRITICAL
- 初始化/写日志实例需要指定级别，级别不够当前level的时候不会写当前level的日志
- 使用方式：
    - 直接使用logging（封装了其他组件，小程序基本够用）
    - logging四大组件直接定制
        组件 	            说明
l       oggers 	            提供应用程序代码直接使用的接口
        handlers 	        用于将日志记录发送到指定的目的位置
        filters 	        提供更细粒度的日志过滤功能，用于决定哪些日志记录将会被输出（其它的日志记录将会被忽略）
        formatters 	        用于控制日志信息的最终输出格式
        
## 2.1 logging模块级别的日志
- 使用以下几个函数
    函数 	                                  说明
    logging.debug(msg, *args, **kwargs) 	   创建一条严重级别为DEBUG的日志记录
    logging.info(msg, *args, **kwargs) 	   创建一条严重级别为INFO的日志记录
    logging.warning(msg, *args, **kwargs) 	   创建一条严重级别为WARNING的日志记录
    logging.error(msg, *args, **kwargs) 	   创建一条严重级别为ERROR的日志记录
    logging.critical(msg, *args, **kwargs)    创建一条严重级别为CRITICAL的日志记录
    logging.log(level, *args, **kwargs) 	   创建一条严重级别为level的日志记录
    logging.basicConfig(**kwargs) 	           对root logger进行一次性配置

-  logging.basicConfig(**kwargs)：对root logger进行一次性配置
    - 只在第一次调用的时候起作用
    - 不配置logger则使用默认值
        - 输出：sys.stderr（标准错误输出到控制台）
        - 级别：WARNING（默认）
        - 格式：level:log_name:content
        
## 2.2 logging模块定义的格式字符串字段        
- 我们来列举一下logging模块中定义好的可以用于format格式字符串中字段有哪些：
- 字段/属性名称	              使 用格式	                                             描述
    - asctime	                     %(asctime)s	                    日志事件发生的时间--人类可读时间，如：2003-07-08 16:49:45,896
    - created	                     %(created)f                       日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值
    - relativeCreated             %(relativeCreated)d	                日志事件发生的时间相对于logging模块加载时间的相对毫秒数（目前还不知道干嘛用的）
    - msecs	                     %(msecs)d	                            日志事件发生事件的毫秒部分
    - levelname	                 %(levelname)s	                       该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'）
    - levelno	                     %(levelno)s	                     该日志记录的数字形式的日志级别（10, 20, 30, 40, 50）
    - name	                     %(name)s	                            所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger
    - message	                     %(message)s	                      日志记录的文本内容，通过 msg % args计算得到的
    - pathname	                  %(pathname)s	                         调用日志记录函数的源码文件的全路径
    - filename	                  %(filename)s	                        pathname的文件名部分，包含文件后缀
    - module	                      %(module)s	                    filename的名称部分，不包含后缀
    - lineno	                      %(lineno)d	                     调用日志记录函数的源代码所在的行号
    - funcName	                  %(funcName)s	                        调用日志记录函数的函数名
    - process	                      %(process)d	                               进程ID
    - processName	                  %(processName)s	                  进程名称，Python 3.1新增
    - thread	                     %(thread)d	                          进程ID
    - threadName	                 %(thread)s	                          线程名称
    
## 2.3 