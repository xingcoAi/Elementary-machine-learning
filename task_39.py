#日志的应用
import logging#导入日志包

#日志的常用级别
"""
1.debug 调试级别的日志
2.info 信息级别的日志
3.warning 警告级别的日志
4.error 错误级别的日志
"""

# logging.basicConfig(level = logging.DEBUG)#配置日志等级为DEBUG级
# logging.debug("This is a debug log")
# logging.info("This is a info log")
# logging.warning("This is a warning log")
# logging.error("This is a error log")

# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# DATE_FORMAT = "%Y/%m/%d  %H:%M:%S"
# logging.basicConfig(filename = "my_log", level = logging.DEBUG, format = LOG_FORMAT, datefmt=DATE_FORMAT)
# # logging.basicConfig(level = logging.DEBUG)#配置日志等级为DEBUG级
# logging.debug("This is a debug log")
# logging.info("This is a info log")
# logging.warning("This is a warning log")
# logging.error("This is a error log")


# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
#  DATE_FORMAT = "%Y/%m/%d  %H:%M:%S"

logger = logging.getLogger()
logger.setLevel("DEBUG")#设置等级

#文件处理器,输入到文件
file_handler = logging.FileHandler("all_greedyai.log", mode = "a", encoding = "UTF-8")
#流处理器,控制输出到控制台
stream_handler = logging.StreamHandler()

#错误日志单独输出到一个文件
error_handler = logging.FileHandler("error.log", mode ="a", encoding = "UTF-8")
error_handler.setLevel(logging.ERROR)

#将所有的处理器添加到logger中
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.addHandler(error_handler)

#格式化
formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s",datefmt= "%Y/%m/%d  %H:%M:%S")

#设置格式化器,需要针对每一个处理器进分别设置
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

logger.info("贪心学院日志打印")
logger.debug("调试日志")
logger.error("这里是一个错误日志")