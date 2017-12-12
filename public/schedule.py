#coding=utf-8

done = [
    '京东金融签到领金币',
    '京东金融领取每周提额包',
    '京东APP签到领京豆',
    '网易云音乐签到',
    '联通营业厅签到',
    '掌上生活签到领积分',
    '尤果网APP'
]

in_process = [
    'IT之家每日金币和经验',
    '飞猪每日签到领流量'
]

def process():
    print('=' * 10 + '打造自己的任务自动处理池' + '=' * 10)
    print('已经完成的任务:')
    for i in done:
        print('\t'+i)

    print('\n'+'正在开发的任务:')
    for i in in_process:
        print('\t'+i)

    print('=' * 43)
