# asset library
## 资产预览器,资产路径:
<br /> AssetPath = 'C:\Asset' #资产路径
<br /> AssetModule = 'Mods','Rigs' #资产模块
<br /> AssetType = ‘Char’,'Prop','Envs' #资产类型
<br /> AssetName = 'name' #资产名称

<br /> 修改AssetName目录(原来Image/Texture保留),新增资产通道Fbx(其他绑定道具存放路径)和Abc(AssetMat存放路径)和History(版本迭代)
<br /> 新增AssetName Mat材质档,AssetMat = 'Material'

<br /> 取消前期AssetLevel = 'Low','Hight'


### 资产描述

### 模型层级:
1.角色和道具通用大纲
<br />Grp(main组)
<br />rig_grp(绑定组)
<br />nouser_grp(角色模型切头，保留头和身体)
<br />root_grp(骨架组,暂时不需要)
<br />geo_grp(模型组)
##模型规范:
<br />body_grp(包含身体，眼睛，眉毛，睫毛)
<br />hair_grp(包含头发，指甲)
<br />cloth_grp(包含衣服，盔甲和饰品)


### 自动检项:
<br />1.检查模型(包括组级)是否有属性位移(有，冻结)
<br />2.检查模型(包括组级)是否属性冻结(有，解锁)
<br />3.检查是否存在display层级(有，清除)
<br />4检查namespace是否存在(有，清除)
<br />5.检查重名命(有，提示)
<br />6.检查是否自定义材质(无，提示)
<br />7.检查法线是否翻转
<br />8.检查模型是否对称
<br />9.检查模型是否存在历史

<br /> 参考案例(https://github.com/JakobJK/modelChecker)
<br />D:\Mya_ScriptCode\modelChecker\modelChecker
<br />https://www.highend3d.com/maya/script/file-browser-for-maya-for-maya



5. 功能ui：
<br />1.创建资产(资产根路径,资产名称，生产图片)
<br />2.资产上传(资产存在，替换并另存为His路径下的版本迭代)
<br />3.资产图片预览
<br />4.模型资产打开、导入和上传(版本迭代到His文件夹内)
<br />5.模型资产切换成绑定资产(新增引用功能)
<br />6.搜索资产
6. UI参考:
<br />pass

7. 修改历史
2022.12.15
<br />.~~鼠标右键显示资产(Open,Iport,Reference,go to file)~~
<br />.~~图片名称显示~~
<br />.~~创建资产,enter确认~~

8. 新增需求:
<br />.添加提交Button功能,资产检查
<br />.Line自能搜索功能
<br />.创建资产即时更新图标
<br />.双击图片打开文件
<br />.切换到Rigs模块,双击文件引用进来
<br />.Maya截图保存到image
<br />.资产名称安装正常顺序排序
<br />.https://stackoverflow.com/questions/40493996/how-to-customize-qpushbutton-to-only-popup-menu-when-clicked-around-the-arrow