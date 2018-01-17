#! python
# encoding = utf-8
# 这是一个简单的试题生成程序，关于中国各省省会及直辖市
import random

'''
      ******   重要提示   *****
函数的使用时，一定要注意是否有返回值，是否可以将函数操作进行赋值给变量
当函数没有返回值时（返回值为None），进行赋值时，变量的值为None

此程序在编写的过程中就犯下过这样的错误，如: list.remove() ,random.shuffle()等都是没有返回值的
'''
# 全国省份及对应的省会
capitals = {
    '直辖市':['北京','天津','上海','重庆'],
    '河北':'石家庄',
    '黑龙江':'哈尔滨',
    '吉林':'长春',
    '辽宁':'沈阳',
    '内蒙古':'呼和浩特',
    '新疆':'乌鲁木齐',
    '西藏':'拉萨',
    '青海':'西宁',
    '甘肃':'兰州',
    '宁夏':'银川',
    '陕西':'西安',
    '山西':'太原',
    '河南':'郑州',
    '山东':'济南',
    '江苏':'南京',
    '安徽':'合肥',
    '湖北':'武汉',
    '四川':'成都',
    '云南':'昆明',
    '贵州':'贵阳',
    '湖南':'长沙',
    '江西':'南昌',
    '浙江':'杭州',
    '福建':'福州',
    '广东':'广州',
    '广西':'南宁',
    '海南':'三亚',
    }
dict_of_index = {0 : 'A',1 : 'B',2 : 'C',3 : 'D'  }          #ABCD数字化

def change_space(sequences):                                 #格式调整，将一个空格改成两个空格，美化输出
    change_list = list(sequences)
    for space in change_list:
        if space == ' ':
            change_list[change_list.index(space)] = '  '
    return ''.join(change_list)
    

provinces_list = list(capitals.keys())                       #将字典表的键列表化，获取省份列表
citys_list = list(capitals.values())                         #获取字典表的列表化的值
citys_list.remove(capitals['直辖市'])                        #对值列表进行处理,获得没有直辖市的列表
citys_without_zxs = citys_list
citys_list.extend(capitals['直辖市'])                        #获得所有城市列表

for paper_num in range(1,16):
    random.shuffle(provinces_list)  #对省份列表随机排序
    
    questions_file = open(r'f:\atom_text\test_of_geograpy\questions\paper-{}.txt'.format(paper_num),'w',encoding = 'utf-8')    #文件操作，写入试题
    answers_file = open(r'f:\atom_text\test_of_geograpy\answers\answer-{}.txt'.format(paper_num),'w',encoding = 'utf-8')       #文件操作，写入答案
    
    for province in provinces_list:       
        
        if province  == '直辖市':                             # 抽取到的城市为直辖市时
            
            citys_list_copy = citys_without_zxs[:]            # 复制无直辖市城市列表副本
            city_zxs = random.choice(capitals[province])      # 随机获取一个直辖市           
            answers_list = random.sample(citys_list_copy,3) + [city_zxs]
            random.shuffle(answers_list)                      # 创建答案列表，并乱序
            answer_index = answers_list.index(city_zxs)       # 获取答案在列表中下标

            #试题，答案写入及格式化
            questions_file.write(' {}.下列哪座城市是直辖市？ ( )\n'.format(provinces_list.index(province) + 1))
            question_anwers = '  A.{:<6}B.{:<6}C.{:<6}D.{:<6}\n\n'.format(answers_list[0],answers_list[1],answers_list[2],answers_list[3])
            questions_file.write(change_space(question_anwers))
            answers_file.write('第 {:>2} 题的答案是：{}. {}\n'.format(provinces_list.index(province) + 1,dict_of_index[answer_index],city_zxs))
            
        else:
            citys_list_copy = citys_list[:]
            citys_list_copy.remove(capitals[province])    # 复制无答案城市列表的副本        
            answers_list = random.sample(citys_list_copy,3) + [capitals[province]]
            random.shuffle(answers_list)                                  # 创建答案列表，并乱序
            answer_index = answers_list.index(capitals[province])         # 获取答案在列表中下标
            
            #试题，答案写入及格式化
            questions_file.write(' {}.下列哪座城市是{}省的省会城市？ ( )\n'.format(provinces_list.index(province) + 1,province))
            question_anwers = '  A.{:<6}B.{:<6}C.{:<6}D.{:<6}\n\n'.format(answers_list[0],answers_list[1],answers_list[2],answers_list[3])
            questions_file.write(change_space(question_anwers))
            answers_file.write('第 {:>2} 题的答案是：{}. {}\n'.format(provinces_list.index(province) + 1,dict_of_index[answer_index],capitals[province]))
        
    questions_file.close()
    answers_file.close()

print("试题已生成完成，请关闭程序")