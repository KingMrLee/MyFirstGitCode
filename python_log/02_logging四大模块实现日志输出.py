'''
1. 需求
现在有以下几个日志记录的需求：
    1）要求将所有级别的所有日志都写入磁盘文件中
    2）all.log文件中记录所有的日志信息，日志格式为：日期和时间 - 日志级别 - 日志信息
    3）error.log文件中单独记录error及以上级别的日志信息，日志格式为：日期和时间 - 日志级别 - 文件名[:行号] - 日志信息
    4）要求all.log在每天凌晨进行日志切割

2. 分析
    1）要记录所有级别的日志，因此日志器的有效level需要设置为最低级别--DEBUG;
    2）日志需要被发送到两个不同的目的地，因此需要为日志器设置两个handler；另外，两个目的地都是磁盘文件，因此这两个handler都是与FileHandler相关的；
    3）all.log要求按照时间进行日志切割，因此他需要用logging.handlers.TimedRotatingFileHandler; 而error.log没有要求日志切割，因此可以使用FileHandler;
    4）两个日志文件的格式不同，因此需要对这两个handler分别设置格式器；
'''

import logging.handlers
import logging
import datetime

# 获取logger实例
my_logger = logging.getLogger("MyLogger")
# 设置logger从最低日志级别DEBUG开始处理，默认是从WARNING开始处理，此处先做初始最低级别处理设置
my_logger.setLevel(logging.DEBUG)

# all.log
# backupCount是设置日志保留的天数，超过这个值，过去的旧日志就删除，开始新的日志保留 delay是日志保留延迟时间，默认为不延迟
all_handlers = logging.handlers.TimedRotatingFileHandler("all.log", when='midnight', interval=1, backupCount=7, encoding="GBK", delay=False, utc=False, atTime=datetime.time(0, 0, 0, 0))
ALL_LOG_FORMAT = logging.Formatter("%(asctime)s--%(levelname)s--%(message)s	")
all_handlers.setFormatter(ALL_LOG_FORMAT)

# error.log
error_handlers = logging.FileHandler("error.log", mode='a', encoding=None, delay=False)
ERROR_LOG_FORMAT = logging.Formatter("%(asctime)s--%(levelname)s--%(filename)s--%(lineno)d--%(message)s")
error_handlers.setFormatter(ERROR_LOG_FORMAT)
# 将error.log的日志级别设置为error，其他级别的日志过滤掉不做输出
error_handlers.setLevel(logging.ERROR)

# 添加上述两个日志handlers处理器
my_logger.addHandler(all_handlers)
my_logger.addHandler(error_handlers)

my_logger.debug('debug message')
my_logger.info('info message')
my_logger.warning('warning message')
my_logger.error('error message')
my_logger.critical('critical message')




