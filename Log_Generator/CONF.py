# 要读取的log文件地址
currentlyRunningLog = "test.log"
# 数据库中正在运行的log的表名
currLogTable = "tmplog"
# 数据库中累积log的表名
accLogTable = "accLog"
# 数据库中表的列名
columns = ['sectionNum', 'caseNum', 'result', 'statusNum' ,'time']
# 登陆数据库的信息
sqlInfo = {'host': 'localhost', 'username': 'root', 'password': 'corei3window7', 'database': 'test'}