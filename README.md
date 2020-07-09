# 实时测试系统开发文档

## 一、开发环境

进入PyQt文件夹后，利用

```
pip3 install -r requirements.txt
```

安装相关环境

## 二、项目功能

![Picture1](./Picture1.png)

通过格式化Log文件将其导入SQL，从SQL实时提取信息，在Qt界面上显示。

## 三、UI设计

### 1.  界面布局

![Picture2](./Picture2.png)

QWidget中不能直接放置QWidget，需要使用QLayout放置多个QWidget后，再使用QWidget中的setLayout函数添加layout以达到多个QWidget嵌套的效果。

### 2. 对应文件

Chart_left_up.py文件对应左上角Widget，Chart_left_down.py文件对应左下角Widget以此类推。

Clock.py文件对应右上角显示时间，title.py文件对应右上角标题。

这些文件在main_widget.py中整合，在mian_window.py文件中显示。

## 四、结构介绍

本程序涉及MySQL数据库，涉及两个表，两个表有相同的结构。

```
+------------+--------------+------+-----+---------+-------+
| Field      | Type         | Null | Key | Default | Extra |
+------------+--------------+------+-----+---------+-------+
| sectionNum | varchar(233) | YES  |     | NULL    |       |
| caseNum    | varchar(233) | YES  |     | NULL    |       |
| result     | varchar(233) | YES  |     | NULL    |       |
| statusNum  | varchar(233) | YES  |     | NULL    |       |
| time       | varchar(233) | YES  |     | NULL    |       |
+------------+--------------+------+-----+---------+-------+
```

## 五、功能实现

### 1. 从数据库中实时提取数据

**使用模块：mysql.connector, QThread, pyqtsignal**

开启线程不断读取数据库数据，利用信号槽机制，在获取数据有改变时，刷新UI，达到实时更新的效果。

*发送信号：*

```python
class BackendThread(QThread):
    update_cloud = pyqtSignal(dict)
    def __init__(self):
        QThread.__init__(self)
        self.data = []

    def run(self):
        while True:
            accNum = Extract_SQL().fetchCaseName(chart_bottom.sectionMark)# 请求数据
            if self.data != accNum:# 发现数据不一致
                self.data = accNum
                self.update_cloud.emit(self.data)# 发射信号
            time.sleep(CONF.RefreshTime[4])
```

*接收信号：*

```python
def initUI(self):
  self.backend = BackendThread()
  self.backend.update_cloud.connect(self.handle)
  self.backend.start()

def handle(self, data):
  # update corresponding UI
```

### 2. 实现通过按钮选择Section显示的功能

在按钮区域设置多个按钮，通过点击不同按钮，获取不同section的数据。

1. 首先在定义按钮区域设置一个全局变量sectionMark。
2. 通过点击按钮，改变sectionMark的值
3. 在其他Widget中引入sectionMark，在利用Extract_sql.py文件获取数据库中值时，将sectionMark的值作为参数传入。
4. Extract_sql文件中的函数，接收到参数为0时，取全局数据，参数不为0时，根据参数值和CONF.py文件中的section表选取部分数据返回。

```python
def fetch(self, data):
		mydb = mysql.connector.connect(
			host=self.host,
			user=self.user,
			password=self.password,
			database=self.database
			)
		mycursor = mydb.cursor()
		if data == 0:
			mark = ''
		else:
			mark = ' where ' + CONF.columns[0] + ' = ' + '\"' + CONF.sectionNames[data-1] + '\"'# 参数不为0时加入筛选语句
		try:
			mycursor.execute('select * from '+ CONF.currLogTable + mark +' for update')
			myresult = mycursor.fetchall()
			if myresult == []:
				return [["Null", "Null", "Null", "Null", "Null"]]# 返回值为空时，加入默认值防止程序exit
			return myresult
		except mysql.connector.Error as e:
			print(e)
		finally:
			mycursor.close()
			mydb.close()
```

## 六、使用方法

### 复现方法

1. 需要在数据库中建立两张相同结构的表，并在CONF.py中配置其database，用户名密码等信息。
2. 需要格式化log文件将其按上文数据表类型存储入数据库，并在CONF.py中设置数据库列名及窗口中显示的列名。

### 添加底部Section项方法

1. 在CONF.py中设置sectionNames变量，包括所有的section的名称。
2. 在chart_bottom.py文件中添加如下代码

```python
# X为数字，以下代码不添加在同一个地方
self.buttonX = QRadioButton("section名称")
self.buttonX.setChecked(False)

self.buttonX.toggled.connect(self.changeMark)

self.layout.addWidget(self.buttonX)
# 在changeMark中添加
if self.buttonX.isChecked():
	sectionMark = 3
```







