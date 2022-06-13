# -*- encoding: utf-8 -*-
'''
_______________________    _________________________________________
__  __ \__  /____  _/_ |  / /__    |__  __ \___  _/_  ____/__  ____/
_  / / /_  /  __  / __ | / /__  /| |_  / / /__  / _  /    __  __/   
/ /_/ /_  /____/ /  __ |/ / _  ___ |  /_/ /__/ /  / /___  _  /___   
\____/ /_____/___/  _____/  /_/  |_/_____/ /___/  \____/  /_____/   

@File      :   helpDocData.py
@Author    :   lunzhiPenxil仑质
@Contact   :   lunzhipenxil@gmail.com
@License   :   AGPL
@Copyright :   (C) 2020-2021, OlivOS-Team
@Desc      :   None
'''

import OlivOS
import OlivaDiceCore

import os
import json

dictHelpDoc = {}

dictHelpDocDefault = {}

dictHelpDocTemp = {
    'default': '''若需要使本机器人退群,请使用[.bot exit]
输入[.bot on]/[.bot off]可以开关骰子功能
(如群内有多个骰子,请在@后追加指令)
[.help指令] 查看指令列表
[.help管理] 查看管理指令
[.help链接] 查看源码文档
[.help更新] 查看更新日志
有问题请联系(请优先加群)
青果核心用户群：661366095''',

    'OlivaDiceCore': '''[OlivaDiceCore]
OlivaDice核心模块
本模块为青果跑团掷骰机器人(OlivaDice)基础核心模块，集成跑团相关的核心功能（包括OneDice标准库、人物卡引擎、配置符号表、用户记录引擎等），并向其他子模块提供挂载点。
核心开发者: lunzhiPenxil仑质
[.help OlivaDiceCore更新] 查看本模块更新日志
注: 本模块为必需模块。''',

    '更新': '''[OlivaDiceCore]
3.1.18: 人物卡锁定
3.1.17: 自动分段
3.1.16: 用户记录指令
3.1.15: 旁观功能
3.1.13: 人物卡模板功能扩充
3.1.11: 消息过滤选项
3.1.10: 指令解析优化
3.1.7: 指令重载
3.1.6: 掷骰体验优化
3.1.5: 用户记录优化
3.1.4: 骰主指令增强
3.1.3: 人物卡成长
3.1.2: 人物作成优化
3.1.1: 模块化优化
3.0.8: 对接官方频道
3.0.7: 属性增量
3.0.6: 心跳系统
3.0.5: 固化版本
3.0.4: 细化指令
3.0.3: 优化控制流
3.0.2: 对接频道
3.0.1: 审核模式
3.0.0: 基础版本实现''',

    '指令': '''@后接指令可以指定单独响应，如[@机器人.bot off]
多数指令需要后接参数，请.help对应指令 获取详细信息，如[.help bot]
多数指令支持大小写混用
.bot exit 退群
.bot 版本信息
.bot on 启用指令
.bot off 停用指令
.coc COC7人物作成
.st 人物卡记录
.nn 设置人物卡名称
.r 掷骰
.ra 检定
.sc 理智检定
.en 成长检定
.ti/li 临时/总结症状
.name 随机名称
.ob 旁观''',

    '管理': '''管理指令
在插件启动时将会显示有关骰子认主指令的具体提示，每完成一次认主，口令将会刷新
.master [验证口令]  骰子认主
.master master (del) [ID]  添加(删除)骰主
.master notice (del) [群号]  添加(删除)通知群
.master pulse [TOKEN]  添加心跳TOKEN
.master pulse del [URL/TOKEN]  删除心跳配置
.master pulse [URL] [TOKEN]  添加第三方心跳TOKEN
.master [配置项] [配置值]  修改配置项
.master remote [on/off] [群组ID]  远程在群中停用
.master remote host [on/off] [频道ID]  远程在频道中停用
.master remote host default [on/off] [频道ID]  远程在频道中默认关闭
.str[配置项] [配置值]  修改对应的自定义配置
.str[配置项]  查看对应的自定义配置
.helpdoc [帮助名称] [帮助内容]  设置帮助文档
.helpdoc [帮助名称]  删除帮助文档''',

    '链接': '''查看源码: https://github.com/OlivOS-Team/OlivaDiceCore
OneDice标准: https://github.com/OlivOS-Team/onedice
OlivOS项目: https://github.com/OlivOS-Team/OlivOS
青果核论坛: https://forum.olivos.run''',

    'dismiss': '''dismiss [dɪsˈmɪs]
vt.	不予考虑; 摒弃; 对…不屑一提; 去除，消除，摒除(思想、感情等); 解雇; 免职; 开除;
[例句]
He dismissed the dismiss as worthless.
他认为dismiss毫无用处。
[其他]
第三人称单数：dismisses
现在分词：dismissing
过去式：dismissed
过去分词：dismissed

若需要使本机器人退群,请使用[.bot exit]''',

    'bot': '''@后接指令可以指定单独响应，如@机器人.bot off
.bot exit 退群
.bot 版本信息
.bot on 启用指令
.bot off 停用指令''',

    'st': '''.st [人物卡名]-[技能名][技能值][技能名][技能值]……    人物卡批量录入
.nn [人物卡名]    重命名人物卡
.st list    显示人物卡列表
.st set [人物卡名]    切换人物卡
.st lock/unlock    锁定/解锁人物卡
.st show    显示人物卡
.st temp [人物卡模版名]    切换人物卡模版
    默认可选：COC7，DND5E，FATE
.st init (force)    人物卡作成
    将依照当前人物卡进行作成，作成前请先行切换人物卡
.st rule [人物卡模版规则名]    切换人物卡规则
更多请使用[.help 人物卡模板]进行查看
.st del [人物卡名]    删除人物卡
    默认删除当前人物卡
.st clear    清空当前人物卡
.st rm [技能名]    删除对应技能''',

    'r': '''通用掷骰指令
表达式支持OneDice标准:
https://github.com/OlivOS-Team/onedice
基于先进的OneDice标准，你不再需要除[.r]指令以外的其他掷骰指令（哪怕规则书告诉你应该那么做）。
例如：
[.r20a10]等同于[.ww20a10]
[.r10c7]等同于[.dx10a7]
指令用法：
.r [掷骰表达式] [理由]    掷骰子
.rh [掷骰表达式] [理由]    掷暗骰
.r[次数]#[掷骰表达式] [理由]    多轮掷骰''',

    'ra': '''检定指令
.ra [技能名] [技能值]    技能检定
.rah [技能名] [技能值]    暗技能检定
.ra[次数]#[技能名] [技能值]    多轮检定
.ra(b/p)[技能名] [技能值]    奖惩检定''',


    'sc': '''理智检定
.sc [成功表达式]/[失败表达式] [san值]   理智检定''',

    'en': '''成长检定
.en [技能名] [技能值]   成长检定
省略技能值时将从人物卡中读取技能值
省略技能名等时，将依据检定历史进行自动成长检定''',

    '疯狂症状': '''疯狂症状：
.ti 临时疯狂症状
.li 总结疯狂症状''',

    'nn': '''命名
.nn [新人物卡名]    重命名人物卡
当与已有其它人物卡重名时，将覆盖旧卡''',

    'coc': '''人物作成
.coc [数量]    COC7人物作成
推荐使用[.st init]指令进行人物卡作成，详情请使用[.help st]查看''',

    'dnd': '''人物作成
.dnd [数量]    DND5E人物作成
推荐使用[.st init]指令进行人物卡作成，详情请使用[.help st]查看''',

    'helpdoc': '''自定义帮助文档:
.helpdoc [帮助名称] [帮助内容]  设置帮助文档
.helpdoc [帮助名称]  删除帮助文档''',

    'str': '''自定义回复词:
.str[配置项] [配置值]  修改对应的自定义配置
.str[配置项]  查看对应的自定义配置
本核心内置了一套str回复词配置工具，可以通过以上指令进行骰子回复词的配置，例如：
使用
[.strPcSkillCheckFailed 哈哈，失败，哈哈]
即可将检定失败回复词进行设置。

更多可以设置的回复词请看文档：
https://wiki.dice.center/OlivOS_Login.html#%E8%87%AA%E5%AE%9A%E4%B9%89%E5%9B%9E%E5%A4%8D%E8%AF%8D--customreplyjson''',

    'draw': '''抽牌:
.draw [牌堆名称]  抽牌堆
.drawh [牌堆名称]  暗抽牌堆''',

    'ob': '''旁观模式：
.ob  切换旁观模式
.ob join 加入旁观模式
.ob exit 退出旁观模式
.ob exit all 退出所有已旁观
.ob clear 清空本群旁观列表''',

    'uinfo': '''用户记录/群记录：
.uinfo 查询自己的用户记录
.uinfo user 查询自己的用户记录
.uinfo group 查询本群的群记录
.uinfo user [id] 查询对应的用户记录
.uinfo group [id] 查询对应的群记录''',

    '人物卡模板': '''1、为自己的人物卡指定COC模版（目前可选为COC7，DND5E，FATE）
指令: [.st temp COC7]
2、为自己的人物卡指定COC模版下的规则
指令: [.st rule C2]

其中[COC7]可选参数如下：
[default]
等同C0
[C0]
出1大成功
不满50出96 - 100大失败，满50出100大失败
[C1]
不满50出1大成功，满50出1 - 5大成功
不满50出96 - 100大失败，满50出100大失败
[C2]
出1 - 5且 <= 成功率大成功
出100或出96 - 99且 > 成功率大失败
[C3]
出1 - 5大成功
出96 - 100大失败
[C4]
出1 - 5且 <= 十分之一大成功
不满50出 >= 96 + 十分之一大失败，满50出100大失败
[C5]
出1 - 2且 < 五分之一大成功
不满50出96 - 100大失败，满50出99 - 100大失败
[DeltaGreen]
小于等于检定目标成功，若结果为1或两骰相同为大成功（相当于整除11）
大于检定目标失败，若结果为100或两骰相同为大失败（相当于整除11）
没有极难成功/困难成功''',

    'setcoc': '''为当前群或频道组设置COC房规
如[.setcoc 1],当前参数0-6

0:[C0]
出1大成功
不满50出96 - 100大失败，满50出100大失败
1:[C1]
不满50出1大成功，满50出1 - 5大成功
不满50出96 - 100大失败，满50出100大失败
2:[C2]
出1 - 5且 <= 成功率大成功
出100或出96 - 99且 > 成功率大失败
3:[C3]
出1 - 5大成功
出96 - 100大失败
4:[C4]
出1 - 5且 <= 十分之一大成功
不满50出 >= 96 + 十分之一大失败，满50出100大失败
5:[C5]
出1 - 2且 < 五分之一大成功
不满50出96 - 100大失败，满50出99 - 100大失败
6:[DeltaGreen]
小于等于检定目标成功，若结果为1或两骰相同为大成功（相当于整除11）
大于检定目标失败，若结果为100或两骰相同为大失败（相当于整除11）
没有极难成功/困难成功

如果其他房规可向开发者反馈，或是使用人物卡模板扩展系统
群内检定会优先调用群内设置''',


    'name': '''随机姓名：
.name (cn/jp/en/enzh)
    后接cn/jp/en/enzh则限定生成中文/日文/英文/英文中译名''',

    'random': '''OlivaDice默认随机数生成器一概采用由random.org提供的真随机数，基于量子源于大气噪声，如对随机数结果有异议请向random.org发起质疑''',

    'onedice': '''OneDice 意为 通用掷骰串标准 ，是一个面向计算机行业的数学表达式标准，旨在统一不同用户级随机数描述时所涉及的应用交互界面设计，使开发者们无需在这类细枝末节的设计中浪费精力或相互争吵，乃至产生过多不合理设计；亦可使用户在使用不同开发者所开发的产品时，能够拥有一个更便捷直接、符合直觉且功能强大的统一表达方式。
表达式支持OneDice标准:
https://github.com/OlivOS-Team/onedice
基于先进的OneDice标准，你不再需要除[.r]指令以外的其他掷骰指令（哪怕规则书告诉你应该那么做）。
例如：
[.r20a10]等同于[.ww20a10]
[.r10c7]等同于[.dx10a7]
[.r5f]等同于[.r5d3-5*2]''',


    'OlivaDiceCore更新': '&更新',
    'ww': '&r',
    'dx': '&r',
    'rc': '&ra',
    'ti': '&疯狂症状',
    'li': '&疯狂症状',
    'help': '&default',
    '帮助': '&default',
    '掷骰': '&r',
    '检定': '&ra',
    '理智检定': '&sc',
    '成长检定': '&en',
    '命名': '&nn',
    '人物卡': '&st',
    '车卡coc': '&coc',
    '车卡dnd': '&dnd',
    '随机数': '&random',
    '随机数算法': '&random',
    '村规': '&setcoc',
    '自定义回复词': '&str',
    '旁观': '&ob',
    '旁观模式': '&ob',
    '用户记录': '&uinfo',
    '群记录': '&uinfo'
}
