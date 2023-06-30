# -*- encoding: utf-8 -*-
'''
_______________________    _________________________________________
__  __ \__  /____  _/_ |  / /__    |__  __ \___  _/_  ____/__  ____/
_  / / /_  /  __  / __ | / /__  /| |_  / / /__  / _  /    __  __/   
/ /_/ /_  /____/ /  __ |/ / _  ___ |  /_/ /__/ /  / /___  _  /___   
\____/ /_____/___/  _____/  /_/  |_/_____/ /___/  \____/  /_____/   

@File      :   msgCustom.py
@Author    :   lunzhiPenxil仑质
@Contact   :   lunzhipenxil@gmail.com
@License   :   AGPL
@Copyright :   (C) 2020-2021, OlivOS-Team
@Desc      :   None
'''

import OlivOS
import OlivaDiceCore

dictStrCustomDict = {}

dictStrCustomUpdateDict = {}

dictStrCustom = {
    'strBotName': 'Bot',
    'strForGroupOnly': '此功能仅对群聊开放',
    'strSetStr': '回复词[{tStrName}]已更新',
    'strBecomeMaster': '口令正确，[{tName}]已成为Master',
    'strBecomeMasterAlready': '你已经拥有Master权限，无需再次认证',
    'strCantBecomeMaster': '无Master权限且口令错误，拒绝认证',
    'strMasterSystemRestart': '[{tName}]远程调用重载',
    'strMasterConsoleShow': '[{tConsoleKey}]当前为[{tConsoleValue}]',
    'strMasterConsoleShowList': '[{tConsoleKey}]当前为:\n{tConsoleValue}',
    'strMasterConsoleSet': '[{tName}]已将[{tConsoleKey}]设置为[{tConsoleValue}]',
    'strMasterConsoleAppend': '[{tName}]已修改[{tConsoleKey}]条目',
    'strMasterConsoleSetInvalid': '非法的配置值',
    'strMasterConsoleNotFound': '无法访问的配置项',
    'strMasterRemoteOn': '已在[{tId}]远程开启',
    'strMasterRemoteOff': '已在[{tId}]远程关闭',
    'strMasterRemoteOnAlready': '[{tId}]已处于开启状态',
    'strMasterRemoteOffAlready': '[{tId}]已处于关闭状态',
    'strMasterRemoteDefaultOn': '已在[{tId}]远程默认开启',
    'strMasterRemoteDefaultOff': '已在[{tId}]远程默认关闭',
    'strMasterRemoteDefaultOnAlready': '[{tId}]已处于默认开启状态',
    'strMasterRemoteDefaultOffAlready': '[{tId}]已处于默认关闭状态',
    'strMasterRemoteNone': '设置失败，未找到[{tId}]的相关记录',
    'strAddCensor': '敏感词已添加',
    'strDelCensor': '敏感词已移除',
    'strCensorReplace': '*',
    'strNeedMaster': '需要Master权限',
    'strNeedAdmin': '需要管理员以上权限',
    'strWelcomeSet': '欢迎词已设置',
    'strWelcomeDel': '欢迎词已清除',
    'strHello': '欢迎使用本机器人! 请使用[.help]查看帮助',
    'strBot': '欢迎使用本机器人! 请使用[.help]查看帮助',
    'strBotExit': '即将退出本群',
    'strBotExitRemote': '收到远程控制, 即将退出本群',
    'strBotExitRemoteShow' : '即将远程退出群[{tGroupId}]',
    'strBotAddFriendNotice': '好友添加请求, 来自[{tUserId}]\n备注:{tComment}\n{tResult}',
    'strBotAddGroupNotice' : '群添加请求，来自群[{tGroupId}], 邀请者[{tInvaterId}]\n{tResult}',
    'strBotAddGroupNoticeIgnoreResult' : '已忽略\n请输入[{tAcceptCommand}]以远程接受请求',
    'strBotAddGroupRemoteAcceptShow' : '已远程接受请求[{tInvateFlag}]',
    'strAccept' : '已接受',
    'strIgnore' : '已忽略',
    'strReject' : '已驳回',
    'strBotOn' : '开启成功',
    'strBotAlreadyOn' : '已经处于开启状态',
    'strBotOff' : '关闭成功',
    'strBotAlreadyOff' : '已经处于关闭状态',
    'strBotNotUnderHost' : '无所属主频道',
    'strBotHostLocalOn' : '本主频道开启成功',
    'strBotAlreadyHostLocalOn' : '本主频道已经处于开启状态',
    'strBotHostLocalOff' : '本主频道关闭成功',
    'strBotAlreadyHostLocalOff' : '本主频道已经处于关闭状态',
    'strBotHostOn' : '本主频道进入默认开启模式',
    'strBotAlreadyHostOn' : '本主频道已经处于默认开启模式',
    'strBotHostOff' : '本主频道进入默认关闭模式',
    'strBotAlreadyHostOff' : '本主频道已经处于默认关闭模式',
    'strHelpDoc' : '已为你找到以下条目:\n{tHelpDocResult}',
    'strHelpDocRecommend' : '已为你找到以下相似条目:\n{tHelpDocResult}',
    'strHelpDocNotFound' : '未找到匹配条目',
    'strDrawTi' : '[{tName}]疯狂发作-临时症状:\n{tResult}',
    'strDrawLi' : '[{tName}]疯狂发作-总结症状:\n{tResult}',
    'strDrawName' : '[{tName}]的随机名称:\n{tResult}',
    'strDrawDeck' : '你抽到了:\n{tDrawDeckResult}',
    'strDrawDeckHideShow' : '[{tName}]进行了暗抽牌',
    'strDrawDeckRecommend' : '已为你找到以下相似牌堆:\n{tDrawDeckResult}',
    'strDrawDeckNotFound' : '牌堆未找到',
    'strRollRecord' : '按照[{tRollFormatType}]重新显示的上次掷骰:\n{tRollResult}',
    'strRoll' : '[{tName}]掷骰: {tRollResult}',
    'strRollWithReason' : '[{tName}]由于[{tRollReason}]掷骰: {tRollResult}',
    'strRollHide' : '于群[{tGroupId}]中[{tName}]掷骰: {tRollResult}',
    'strRollHideWithReason' : '于群[{tGroupId}]中[{tName}]由于[{tRollReason}]掷骰: {tRollResult}',
    'strRollHideShow' : '[{tName}]掷暗骰',
    'strRollHideShowWithReason' : '[{tName}]由于[{tRollReason}]掷暗骰',
    'strRollRange' : '表达式: {tRollPara}\n细节: {tRollResultDetail}\n结果: {tRollResultInt}\n范围: {tRollResultIntRange}',
    'strRollError01' : '表达式[{tRollPara}]掷骰错误！无法解析的表达式！',
    'strRollError02' : '表达式[{tRollPara}]掷骰错误！无法计算的表达式！',
    'strRollError03' : '表达式[{tRollPara}]掷骰错误！输入了非法的表达式！',
    'strRollError04' : '表达式[{tRollPara}]掷骰错误！输入了非法的子参数！',
    'strRollError05' : '表达式[{tRollPara}]掷骰错误！输入了非法的运算符！',
    'strRollError06' : '表达式[{tRollPara}]掷骰错误！发现未定义运算符！',
    'strRollError07' : '表达式[{tRollPara}]掷骰错误！解析到空语法树！',
    'strRollError08' : '表达式[{tRollPara}]掷骰错误！错误的左值！',
    'strRollError09' : '表达式[{tRollPara}]掷骰错误！错误的右值！',
    'strRollError10' : '表达式[{tRollPara}]掷骰错误！错误的子参数！',
    'strRollError11' : '表达式[{tRollPara}]掷骰错误！计算极值时出错！',
    'strRollError12' : '表达式[{tRollPara}]掷骰错误！解析技能变量时出错！',
    'strRollErrorUnknown' : '表达式[{tRollPara}]掷骰错误！未知的错误: {tResult}',
    'strRollErrorHelp' : '\n请使用[.help r]查看掷骰帮助，或使用[.help onedice]查看先进的OneDice标准。',
    'strSetGroupTempRule' : '已设置本群套用模板[{tPcTempName}]的规则[{tPcTempRuleName}]{tLazyResult}',
    'strDelGroupTempRule' : '已清除本群套用模板与规则，将按照人物卡设置各自进行检定',
    'strSetGroupTempError' : '试图套用的模板不存在',
    'strSetGroupTempRuleError' : '试图套用的模板规则不存在',
    'strSetGroupMainDice' : '已设置本群套用主骰[{tResult}]',
    'strShowGroupMainDice' : '本群已套用主骰[{tResult}]',
    'strShowGroupMainDiceNone' : '本群未设置主骰',
    'strDelGroupMainDice' : '已清除本群套用主骰',
    'strSnSet' : '已将群名片修改为[{tResult}]',
    'strSnPcCardNone' : '未设置人物卡，无法进行名片设置',
    'strPcSetMapValueError' : '[{tResult}]不是合法的表达式',
    'strPcInitSet' : '先攻列表已设置:\n{tResult}',
    'strPcInitShow' : '当前先攻列表:\n{tResult}',
    'strPcInitReset' : '重新生成先攻列表:\n{tResult}',
    'strPcInitClear' : '已清空先攻列表',
    'strPcInitShowNode' : '{tId}. [{tSubName}]: {tSubResult}',
    'strPcInitDel' : '已从先攻列表中删除[{tName}]',
    'strPcInit' : '[{tPcTempName}]人物卡作成:{tPcInitResult}',
    'strPcUpdateSkillValue' : '[{tName}]的人物卡已更新:\n[{tSkillName}]: {tSkillUpdate}',
    'strPcSetSkillValue' : '[{tName}]的人物卡已保存',
    'strPcGetSingleSkillValue' : '[{tName}]的[{tSkillName}]: {tSkillValue}',
    'strPcShow' : '人物卡[{tName}]:\n{tPcShow}',
    'strPcList' : '[{tName}]的人物卡:\n{tPcList}\n当前选择:{tPcSelection}',
    'strPcLock' : '已在此成功锁定人物卡[{tName}]',
    'strPcLockError' : '在此锁定人物卡[{tName}]失败',
    'strPcLockNone' : '试图锁定的人物卡不存在',
    'strPcUnLock' : '已在此成功解除锁定人物卡[{tName}]',
    'strPcUnLockNone' : '当前没有已锁定的人物卡',
    'strPcInitSt' : '人物卡[{tName}]已按照[{tPcTempName}]完成人物卡作成:{tPcInitResult}',
    'strPcSet' : '人物卡已切换至[{tPcSelection}]',
    'strPcSetError' : '试图切入的人物卡不存在',
    'strPcNew' : '人物卡[{tPcSelection}]已创建',
    'strPcNewError' : '请附带需要创建的人物卡名称',
    'strPcDel' : '人物卡[{tPcSelection}]已删除',
    'strPcDelError' : '试图删除的人物卡不存在',
    'strPcDelNone' : '人物卡列表为空',
    'strPcClear' : '当前人物卡[{tPcSelection}]已清空',
    'strPcClearNone' : '当前没有人物卡',
    'strPcRm' : '人物卡[{tPcSelection}]的[{tSkillName}]已删除',
    'strPcRmNone' : '人物卡[{tPcSelection}]的[{tSkillName}]不存在',
    'strPcRmCardNone' : '人物卡不存在',
    'strPcTemp' : '人物卡[{tPcSelection}]套用模板[{tPcTempName}]',
    'strPcTempShow' : '人物卡[{tPcSelection}]:\n模板[{tPcTempName}]{tResult}',
    'strPcTempError' : '试图套用的模板不存在，或是未设置人物卡',
    'strPcTempRule' : '人物卡[{tPcSelection}]套用模板[{tPcTempName}]的规则[{tPcTempRuleName}]',
    'strPcTempRuleShow' : '人物卡[{tPcSelection}]:\n模板[{tPcTempName}]\n规则[{tPcTempRuleName}]{tResult}',
    'strPcTempRuleError' : '试图套用的模板规则不存在，或是未设置人物卡',
    'strPcGroupTempRuleShow' : '\n\n但本群已全局套用:\n模板[{tPcTempName}]\n规则[{tPcTempRuleName}]',
    'strPcRename' : '[{tPcSelection}]已重命名为[{tPcSelectionNew}]',
    'strPcSkillCheck' : '[{tName}]进行技能[{tSkillValue}]检定: {tRollResult} {tSkillCheckReasult}',
    'strPcSkillCheckHide' : '于群[{tGroupId}]中[{tName}]进行技能[{tSkillValue}]检定: {tRollResult} {tSkillCheckReasult}',
    'strPcSkillCheckHideShow' : '[{tName}]进行技能[{tSkillValue}]暗检定',
    'strPcSkillCheckWithSkillName' : '[{tName}]进行技能[{tSkillName}:{tSkillValue}]检定: {tRollResult} {tSkillCheckReasult}',
    'strPcSkillCheckHideWithSkillName' : '于群[{tGroupId}]中[{tName}]进行技能[{tSkillName}:{tSkillValue}]检定: {tRollResult} {tSkillCheckReasult}',
    'strPcSkillCheckHideShowWithSkillName' : '[{tName}]进行技能[{tSkillName}:{tSkillValue}]暗检定',
    'strPcSkillEnhanceCheck' : '[{tName}]进行技能[{tSkillName}:{tSkillValue}]成长检定: {tRollResult} {tSkillCheckReasult}',
    'strPcSkillEnhanceContent' : '\n该技能发生了增长: {tRollSubResult}',
    'strPcSkillEnhanceAll' : '[{tName}]进行技能自动成长检定:\n共有[{tSkillEnhanceCount}]个技能进行了检定，其中成功[{tSkillEnhanceSucceedCount}]个: {tSkillEnhanceSucceedList}',
    'strPcSkillEnhanceError' : '未设置人物卡，无法进行自动成长检定',
    'strSanCheck' : '[{tName}]进行理智检定[{tSkillValue}]:\n{tRollResult} {tSkillCheckReasult}\n理智减少{tRollSubResult}点,当前剩余[{tSkillValueNew}]点',
    'strSanCheckGreatFailed' : '[{tName}]进行理智检定[{tSkillValue}]:\n{tRollResult} {tSkillCheckReasult}\n理智减少{tRollSubResult}的最大值[{tRollSubResultIntMax}]点,当前剩余[{tSkillValueNew}]点',
    'strSanCheckError' : '[{tName}]进行理智检定[{tSkillValue}]:\n{tRollResult} {tSkillCheckReasult}\n掷骰表达式[{tRollSubResult}]存在错误',
    'strIntPositiveInfinite' : '正无穷大',
    'strIntNegativeInfinite' : '负无穷大',
    'strPcSkillCheckSucceed' : '成功',
    'strPcSkillCheckHardSucceed' : '困难成功',
    'strPcSkillCheckExtremeHardSucceed' : '极难成功',
    'strPcSkillCheckGreatSucceed' : '大成功',
    'strPcSkillCheckFailed' : '失败',
    'strPcSkillCheckGreatFailed' : '大失败',
    'strPcSkillCheckFate01' : '[-2 拙劣]',
    'strPcSkillCheckFate02' : '[-1 差劲]',
    'strPcSkillCheckFate03' : '[+0 二流]',
    'strPcSkillCheckFate04' : '[+1 一般]',
    'strPcSkillCheckFate05' : '[+2 尚可]',
    'strPcSkillCheckFate06' : '[+3 良好]',
    'strPcSkillCheckFate07' : '[+4 极佳]',
    'strPcSkillCheckFate08' : '[+5 卓越]',
    'strPcSkillCheckFate09' : '[+6 惊异]',
    'strPcSkillCheckFate10' : '[+7 史诗]',
    'strPcSkillCheckFate11' : '[+8 传奇]',
    'strPcSkillCheckNope' : '需要解释',
    'strPcSkillCheckError' : '发生错误',
    'strRAVShow' : '[{tName}]与[{tName01}]进行技能[{tSkillName}]对抗:\n[{tSkillValue} - {tSkillValue01}]\n[{tName}]: {tRollResult} {tSkillCheckReasult}\n[{tName01}]: {tRollResult01} {tSkillCheckReasult01}\n{tRAVResult}',
    'strRAVResult01' : '前者，[{tName}]获胜',
    'strRAVResult02' : '后者，[{tName01}]获胜',
    'strRAVResult03' : '平手',
    'strHelpdocSet' : '自定义帮助文档已设置',
    'strHelpdocDel' : '自定义帮助文档已删除',
    'strObList' : '当前旁观列表:\n{tResult}',
    'strObListNone' : '当前旁观列表为空',
    'strObUserObList' : '当前旁观列表:\n{tResult}',
    'strObUserObListNone' : '当前旁观列表为空',
    'strObJoin' : '[{tUserName}]现已加入旁观',
    'strObJoinAlready' : '[{tUserName}]已在旁观中',
    'strObExit' : '[{tUserName}]现已退出旁观',
    'strObExitAlready' : '[{tUserName}]不在旁观中',
    'strObExitAll' : '[{tUserName}]现已退出所有旁观',
    'strObClear' : '已清空旁观列表'
}

dictStrConst = {
    'strToBeMaster' : '请使用[{tInitMasterKey}]指令以获取Master权限',
    'strInitTempDataError' : '加载人物卡模板文件[{tInitDataName}]至[{tName}]时出错，请检查文件格式或软件版本！',
    'strInitData' : '[{tInitDataCount}]条[{tInitDataType}]数据已加载',
    'strInitDeckData' : '[{tInitDataCount}]个牌堆已加载至[{tName}]，共[{tInitDataCount01}]个牌堆',
    'strInitDeckDataError' : '加载牌堆文件[{tInitDataName}]至[{tName}]时出错，请检查文件格式或软件版本！',
    'strInitCensor' : '已生成敏感词检测模型至[{tName}]，耗时[{tInitDataTimeCost}]，包含[{tInitDataCount}]条',
    'strPatchCensor' : '已补充敏感词检测模型至[{tName}]，耗时[{tInitDataTimeCost}]，新增[{tInitDataCount}]条',
    'strRunCensorError' : '检测敏感词时发生错误，将按原样回复：\n{tResult}',
    'strInitBakData' : '[{tInitDataCount}]条[{tInitDataType}]数据已备份',
    'strSaveData' : '[{tInitDataCount}]条[{tInitDataType}]数据已写入',
    'strShowVersionOnLog' : '当前版本为[{tVersion}]'
}

dictGValue = {
    'gBotName' : '我'
}

dictTValue = {
    'tAdapter': 'Native',
    'tRandomMode': '未知',
    'tVersion' : 'N/A',
    'tBotHash' : 'unity',
    'tId' : 'N/A',
    'tName' : 'N/A',
    'tName01' : 'N/A',
    'tSubName' : 'N/A',
    'tStrName' : 'N/A',
    'tUserId' : 'N/A',
    'tUserName' : '用户',
    'tGroupName' : '私聊',
    'tGroupId' : '私聊',
    'tInvaterName' : 'N/A',
    'tInvaterId' : 'N/A',
    'tInvateFlag' : 'N/A',
    'tComment' : 'N/A',
    'tResult' : 'N/A',
    'tLazyResult' : '',
    'tSubResult' : '',
    'tAcceptCommand' : 'N/A',
    'tRollFormatType' : 'N/A',
    'tRollResult' : '',
    'tRollResult01' : '',
    'tRollSubResult' : '',
    'tRollSubResultIntMax' : 'N/A',
    'tRollReason' : '',
    'tRollPara' : '',
    'tRollResultInt' : 'N/A',
    'tRollResultDetail' : 'N/A',
    'tRollResultIntRange' : 'N/A',
    'tSkillName' : '',
    'tSkillValue' : '',
    'tSkillValue01' : '',
    'tSkillValueNew' : '',
    'tSkillCheckReasult' : '',
    'tSkillCheckReasult01' : '',
    'tSkillUpdate' : 'N/A',
    'tPcInitResult' : 'N/A',
    'tPcShow' : '',
    'tPcList' : '',
    'tPcSelection' : 'N/A',
    'tPcSelectionNew' : 'N/A',
    'tPcTempName' : '',
    'tPcTempRuleName' : '',
    'tSkillEnhanceCount' : 'N/A',
    'tSkillEnhanceSucceedCount' : 'N/A',
    'tSkillEnhanceSucceedList' : 'N/A',
    'tInitDataCount' : '0',
    'tInitDataCount01' : '0',
    'tInitMasterKey': '不可用',
    'tInitDataType': '未知',
    'tInitDataName': 'N/A',
    'tInitDataTimeCost': 'N/A',
    'tHelpDocResult': 'N/A',
    'tDrawDeckResult': 'N/A',
    'tConsoleKey': 'N/A',
    'tConsoleValue': 'N/A',
    'tRAVResult': '未定义结果'
}

dictSetCOCDetail = {
    'C0': '''出1大成功
不满50出96 - 100大失败，满50出100大失败''',
    'C1': '''不满50出1大成功，满50出1 - 5大成功
不满50出96 - 100大失败，满50出100大失败''',
    'C2': '''出1 - 5且 <= 成功率大成功
出100或出96 - 99且 > 成功率大失败''',
    'C3': '''出1 - 5大成功
出96 - 100大失败''',
    'C4': '''出1 - 5且 <= 十分之一大成功
不满50出 >= 96 + 十分之一大失败，满50出100大失败''',
    'C5': '''出1 - 2且 < 五分之一大成功
不满50出96 - 100大失败，满50出99 - 100大失败''',
    'DeltaGreen': '''小于等于检定目标成功，若结果为1或两骰相同为大成功（相当于整除11）
大于检定目标失败，若结果为100或两骰相同为大失败（相当于整除11）
没有极难成功/困难成功''',
    'CG': '''出1 - 3大成功
出98 - 100大失败'''
}

dictAdapterMapper = {
    'qq': {
        'onebot': {
            'default': 'onebotV11',
            'shamrock_default': 'Shamrock',
            'para_default': 'onebotV11',
            'onebotV12': 'onebotV12',
            'gocqhttp': 'GoCqhttp',
            'gocqhttp_hide': 'GoCqhttp',
            'gocqhttp_show': 'GoCqhttp',
            'gocqhttp_show_Android_Phone': 'GoCqhttp.aPhone',
            'gocqhttp_show_Android_Pad': 'GoCqhttp.aPad',
            'gocqhttp_show_Android_Watch': 'GoCqhttp.aWatch',
            'gocqhttp_show_iPad': 'GoCqhttp.iPad',
            'gocqhttp_show_iMac': 'GoCqhttp.iMac',
            'gocqhttp_show_old': 'GoCqhttp',
            'walleq': 'WalleQ',
            'walleq_hide': 'WalleQ',
            'walleq_show': 'WalleQ',
            'walleq_show_Android_Phone': 'WalleQ.aPhone',
            'walleq_show_Android_Pad': 'WalleQ.aPad',
            'walleq_show_Android_Watch': 'WalleQ.aWatch',
            'walleq_show_iPad': 'WalleQ.iPad',
            'walleq_show_iMac': 'WalleQ.iMac',
            'walleq_show_old': 'WalleQ',
            'red': 'Chronocat',
            'opqbot_default': 'OPQBot',
            'opqbot_auto': 'OPQBot',
            'opqbot_port': 'OPQBot',
            'opqbot_port_old': 'OPQBot',
            'napcat': 'NapCat',
            'napcat_hide': 'NapCat',
            'napcat_show': 'NapCat',
            'napcat_show_new': 'NapCat',
            'napcat_show_old': 'NapCat'
        }
    },
    'kaiheila': {
        'kaiheila_link': {
            'default': 'KOOK',
            'text': 'KOOK'
        }
    },
    'terminal': {
        'terminal_link': {
            'ff14': 'FF14'
        }
    }
}
