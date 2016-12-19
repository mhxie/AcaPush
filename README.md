## 项目简介

四川大学计算机学院软件工程课程作业，开发出能够抓取所有四川大学学院的新闻通知的全平台客户端（包括安卓，iOS，网页），目前作为后端开展项目。


## 项目开发进度预计(Last Modification, Dec 19)
预计开发时长：两个月（Oct 19 - Dec 19）

* 教学周第七周
	* [需求设计](https://github.com/Yetocome/AcaPush/tree/master/doc/Scenario-based%20models)[completed]
	* [接口设计](https://github.com/Yetocome/AcaPush/blob/master/doc/interfaces.md)[completed, still poor]
	* 进度规划[completed]
* 教学周第八周
	* 完善讨论需求[completed]
		* 完成了基本的用例设计，见`\doc\Scenario-based models\`[跳转](https://github.com/Yetocome/AcaPush/tree/master/doc/Scenario-based%20models)
		* 完成了对应用例的用例图绘制，见`\doc\pic\`[跳转](https://github.com/Yetocome/AcaPush/tree/master/doc/pic)
	* 设计数据库[completed]
		* 完成数据库基本设计，包括结构设计和逻辑设计，[文档](https://github.com/Yetocome/AcaPush/blob/master/doc/database/%E6%95%B0%E6%8D%AE%E5%BA%93%E8%AE%BE%E8%AE%A1%E8%AF%B4%E6%98%8E%E4%B9%A6.docx)
		* Crow's food图绘制，[跳转](https://github.com/Yetocome/AcaPush/blob/master/doc/pic/database-overview.png)
* 教学周第九周
	* 部分视图和路由代码的编写[up to Zhoufan Jia, completed]
	* 数据库插入新闻通知、初始化学院表代码，以及爬虫组数据交互格式[up to Zhijing Wu, completed]
	* 部分单元测试和视图代码编写[up to Minghao Xie, completed]
* 教学周第十周
	* 添加视图测试，完成基本的部署[up to Minghao Xie, completed]
	* 接入爬虫组数据[up to Zhijing Wu, completed]
	* 完成json测试服务器的编写，将路由和视图改通[up to Zhoufan Jia, completed]
* 教学周第十一周
	* 修改了获取与搜索的四个views[up to Zhoufan Jia, completed]
	* 完成剩余视图测试编写以及云服务器的主要部署[up to Minghao Xie, completed]
	* 修改完善后端数据[up to Zhijing Wu, completed]
* 教学周第十二周
	* 和其他小组协商改进接口
	* 开启admin——后台数据库管理系统
	* bug修复：
		* json格式
		* 解决django异构代码问题
* 教学周第十三周
	* 大量BUG修复
	* 接口微调
*  教学周第十四周
	* 对项目进行回顾总结，完成剩余的文档编写
	* 调整部署，修改bug

## TO-DO
* 数据库设计（和爬虫组协商）[done]
* 小组分工[done]
* 完成关键部分的活动图[canceled]
* 完成关键数据的流图[canceled]
* 完善数据库设计[done]
* 视图测试、数据库测试[partly done]
* 代码部署[Done]


## 部署
staging api: api-staging.xmhtest.cn

old api: xmhtest.cn

api closed time: Sun, Jan 1, 2017