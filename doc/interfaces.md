## 接口设计文档

## 一：前端

RESTful Design

### 查询类接口：

访问用户资料：/profile/user_info
访问用户的收藏夹/profile/user_favorite
访问用户的历史纪录:/profile/user_history
搜索接口：/search

### 操作类接口：
更改用户资料：/alter/user_info，此接口用于用户访问  
修改用户的收藏夹/profile/user_favorite  
搜索接口：/search  
登陆接口：/login  
登出接口：/logout  

### 推送类接口
评论列表：/comments  
新闻列表：/news  
通知列表：/notice  

## 二：后端
### 数据类型：
 	采用json数据格式：良好的跨平台性，格式简单易读写易解析。

### 操作类接口：
 用户数据接口：添加、删除和修改（用户资料、收藏夹）

	User_info/add
	User_info/delete
	User_info/alter
评论数据接口：添加、删除和修改  
新闻数据接口：添加、删除和修改

### 查询类接口：
* 用户数据（用户资料、收藏夹）
* 评论数据
* 标题数据
* 新闻数据
