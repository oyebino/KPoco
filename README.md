
## 工程目录：

- Project/:  系统名称
  - interface   接口基础类
  - Pages  UI测试基础类
  - common  公共方法类(日志,数据库等)
  - Config 配置文件
  - driver 浏览器驱动
  - lib 依赖插件库
  - report/： 存储测试结果
  - result  存放运行截图
  - Log  执行日志
  - test_case/： 接口测试用例
  - run_test:  执行接口测试入口

## 说明
1.Pages文件夹存放页面元素定位，以及封装业务方法。

2.interface文件存放部分业务接口文件，对测试接口相关的封装，在特殊的业务需通过接口的方式来埋数，或前置条件的业务

3.test_case文件保存按模块的执行用例，用例文件及用例方法必须以test为前缀

```
def test_CarIn(self):
	pass
```

4.report存放测试报告

5.run_test批量执行测试案例的触发文件；

6.web-report.bat 该文件是自动生成报告显示

## 使用方法：
--
#####1.安装python3环境(未在python2上运行过，不知道有没有问题）
#####2.clone代码到本地
#####3.cmd到根目录下载相关依赖包

```
pip install -r requirements.txt
```
#####4.配置allure报告插件
  - 解压allure压缩包

    ```
    lib\allure-2.7.0.zip
    ```

  - 配置环境变量 
  ```
  path = E:\allure-2.7.0\bin;
  ```

