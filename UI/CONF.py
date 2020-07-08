# 数据库中正在运行的log的表名
currLogTable = "tmplog"
# 数据库中累积log的表名
accLogTable = "accLog"
# 数据库中表的列名
columns = ['sectionNum', 'caseNum', 'result', 'statusNum' ,'time']
# 登陆数据库的信息
sqlInfo = {'host': 'localhost', 'username': 'root', 'password': 'corei3window7', 'database': 'test'}
# 窗口的标题
windowName = "SQL LOG"
# 窗口中表的列名
tableColumnName = ['SECTION', 'CASE', 'RESULT', 'STATUS', 'TIME']
# 窗口刷新频率(左上，左下，中间，右上，右下)
RefreshTime = [1,1,1,1,1]
# 词云
# 设置词云字体大小
maxFontSize = 100
minFontSize = 10
# 设置显示最多词数
maxWords = 10
# 左上图标题及xy轴名称
leftUpNames = ['累积数据', '累积Case数', '累积Fail数']
# 左下图标题及标签
leftDownNames = ['Fail数日期分布', '日期']
# 右上图标题及标签
rightUpNames = ['Fail数Section分布', 'Section']
# 数据库中section名
sectionNames = ['section1', 'section2']
# 标题
title = '实时化测试系统'
