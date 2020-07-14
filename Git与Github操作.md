#### Git命令

---

##### Git操作的三个步骤

![](D:\WorkSpace\typora\微信图片_20200622012029.jpg)



- 工作区域的操作

  - 新建文件

    > touch  文件名
    >
    > vim(vi)  文件名/当在vim模式下，默认在command模式下，按i或insert进入插入模式，此时可编辑文件；当编辑完按esc键再按：号在底部等待输入：
    >
    > - w 保存
    > - w  filename   另存为filename
    > - wq  保存退出
    > - wq filename 以filename为文件名保存并退出
    > - q 不保存退出

  - 删除文件

    > git rm 文件名

  - 将文件上传到暂存区

    > git add * (上传全部文件)
    >
    > git add 文件全名

  - 将文件从暂存区提交到git库

    > git commit -m "提交描述"

##### Git管理远程仓库

- 将项目从本地上传到远程仓库示意图

  ![](D:\WorkSpace\typora\微信图片_20200622014927.jpg)

1. 初始化git

   > git init

2. 创建SSH Key

   > ssh-keygen -t rsa -C "仓库的SSH"

3. 将密钥添加到github的SSH设置中

4. 验证是否成功

   > ssh -T git@github.com

5. 配置username和Email

   > git config  --global user.name  "Github用户名"
   >
   > git config --global user.email  "Github邮箱"

6. 关联远程仓库

   > git remote add origin  仓库的SSH
   >
   > *若当前add仓库被提交过会报错*
   >
   > *需要先删除再添加*
   >
   > git remote rm origin
   >
   > git remote add origin git@github.com:xingcoAi/SSH.git

7. 上传本地仓库到Github中

   > git push -u origin master
   >
   > *创建仓库时创建了readme文件会出问题，执行下面两句命令*
   >
   > git pull --rebase origin master
   >
   > git push -u origin master