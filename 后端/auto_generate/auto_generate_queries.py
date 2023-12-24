from auto_generate.auto_generate_nodes import *
from auto_generate.auto_generate_edges import *
from database.db import *



knowledges = [
#     Node("knowledge", {"name": 'influenza', 'chinese_name': '流行性感冒', 'link': 'https://www.cma.org.cn/art/2018/6/8/art_1542_243.html', 'path': '''根据《流行性感冒诊断与治疗指南》（卫生部流行性感冒诊断与治疗指南编撰专家组，2011年版），流感流行或非流行时期出现发热伴上呼吸道症状或原有慢性肺部疾病急性加重，具有以下1种或1种以上病原学检测阳性的患者，可以确诊为流感：
#
# （1）     流感病毒核酸检测阳性（可采用实时RT-PCR和RT-PCR方法）；
#
# （2）     流感病毒快速抗原检测阳性（可采用免疫荧光法和胶体金法），需结合流行病学史进行综合判断；
#
# （3）     流感病毒分离培养阳性；
#
# （4）     急性期和恢复期双份血清的流感病毒特异性IgG抗体水平呈4倍或4倍以上升高。'''}),
#     Node("knowledge", {"name": 'bronchopneumonia', 'chinese_name': '支气管肺炎','link': 'https://www.cma.org.cn/art/2018/10/17/art_1542_205.html', 'path': '''根据《临床诊疗指南－呼吸病学分册》（中华医学会编著，人民卫生出版社）,《内科学（8版）》（人民卫生出版社）。
#
# 1.呼吸道症状与体征：咳嗽、咳痰，或原有呼吸道症状加重。重症表现为鼻翼扇动、口周发绀及三凹征。两肺可闻及固定性湿罗音。
#
# 2.全身临床表现：起病多较急，常伴发热，可有神志或意识改变、腹泻或呕吐、心率增快等多系统症状。多见于老年或伴随严重基础疾病如COPD患者。
#
#   3.胸部X线：沿肺纹理分布的不规则斑片状阴影，边缘浅而模糊，无实变征象，以两肺下野多见。
#
#   4.实验室检查：
#
# （1）外周血常规和降钙素原（PCT）、C反应蛋白（CRP）：细菌感染时，白细胞总数和中性粒细胞增多，CRP和PCT多升高；病毒性肺炎时，白细胞总数正常或减少，CRP上升不明显，PCT大多正常。
#
# （2）呼吸道病原学检测：本病可由不同病原所致，推荐根据不同病原体和医院情况选择合适的方法进行检查。需要鉴别的病原包括常见的呼吸道病毒（如流感病毒、呼吸道合胞病毒感染、腺病毒等）、支原体、衣原体、军团菌、细菌等。'''}),
#     Node("knowledge", {"name": 'chronic_bronchitis', 'chinese_name': '慢性支气管炎', 'link': 'https://www.cma.org.cn/art/2018/6/8/art_1542_236.html',
#                        'path': '''根据《临床诊疗指南–呼吸病学分册》（中华医学会编著，人民卫生出版社），《内科学（8版）》（人民卫生出版社）。
#
# 1.慢性或反复咳嗽、咳痰或伴有喘息，每年发病持续3个月，并连续2年或以上者。
#
# 2.如每年发病持续不足3个月，而有明确的客观检查依据（如X线、肺功能等）亦可诊断。
#
# 3.排除其他心、肺疾患（如肺结核、肺尘埃沉着病、支气管哮喘、支气管扩张、肺癌、心脏病、心功能不全、慢性鼻炎等）引起的咳嗽、咳痰或伴有喘息等。'''}),
#     Node("knowledge", {"name": 'spontaneous_pneumothorax', 'chinese_name': '自发性气胸', 'link': 'https://www.cma.org.cn/art/2018/10/17/art_1542_201.html',
#                        'path': '''根据《临床诊疗指南－呼吸病学分册》（中华医学会编著，人民卫生出版社）
#
# 1.症状：胸痛、呼吸困难、刺激性咳嗽。
#
# 2.体征：患侧呼吸音减弱、叩诊呈鼓音或过清音、气管向健侧移位。
#
# 3.影像学检查：X线胸片检查见气胸线，肺组织受压。'''}),
#     Node("knowledge", {"name": 'benign_chest_wall_tumor', 'chinese_name': '胸壁良性肿瘤', 'link': 'https://www.cma.org.cn/art/2018/10/17/art_1542_146.html',
#                        'path': '''根据《临床诊疗指南-胸外科分册》(中华医学会编著，人民卫生出版社)。
#
# 1.临床症状：可无症状，也可有不同程度局部压迫症状
#
#  2.体征：位于浅表的可触及肿块，局部可有压痛。
#
# 3.辅助检查：胸部影像学检查，经皮穿刺活检等。'''}),
#     Node("knowledge", {"name": 'bronchogenic_carcinoma', 'chinese_name': '支气管肺癌', 'link': 'https://www.cma.org.cn/art/2018/10/17/art_1542_145.html',
#                        'path': '''根据国家卫生计生委《中国原发性肺癌诊疗规范（2015年版）》、《临床诊疗指南-胸外科分册》(中华医学会编著，人民卫生出版社)
#
# 1.高危因素：吸烟指数>400，年龄>45岁，环境与职业因素。
#
# 2.临床症状：刺激性咳嗽、血痰或咯血、胸痛。
#
# 3.临床体征：早期不显著。
#
# 4.辅助检查：胸部影像学检查，纤维支气管镜，肺穿刺活检等提示。'''}),
#     Node("knowledge", {"name": 'bronchiectasis', 'chinese_name': '支气管扩张症', 'link': 'https://www.cma.org.cn/art/2018/10/17/art_1542_144.html',
#                        'path': '''根据《临床诊疗指南-胸外科分册》（中华医学会编著，人民卫生出版社）。
#
# 1.临床症状：反复咳嗽、咳脓痰、咯血，慢性感染或中毒症状。
#
# 2.体征：肺部感染较重者或咯血时，可闻及哮鸣音或湿罗音。病变累及双肺时可有呼吸困难、紫绀，病程较长者可见杵状指（趾）等慢性缺氧改变。
#
# 3.辅助检查：影像学检查显示支气管扩张的异常改变。'''}),
#     Node("knowledge", {"name": 'bronchiolitis',
#                        'chinese_name': '毛细支气管炎',
#                        'link': 'https://www.cma.org.cn/art/2018/10/17/art_1542_126.html',
#                        'path': '''根据《临床诊疗指南－小儿内科分册》（中华医学会编著，人民卫生出版社）。
#
#   本病诊断要点为：发病年龄小（<2岁），发病初期即出现明显喘憋，体检两肺闻及哮鸣音及细湿罗音；胸片提示肺纹理增粗或肺气肿或肺不张或小片状阴影。
#
#   1.病史：多见于2岁以内，尤其以6个月左右婴儿最为多见。大多数有接触呼吸道感染病人的病史。
#
#   2.症状：初始出现上呼吸道感染的症状，多表现为低热、流涕、鼻塞、咳嗽，部分可有高热、精神不振、食欲减退。2－3天出现下呼吸道症状，症状轻重不等，咳嗽明显加重，并有喘息发作，重者出现发作性喘憋及紫绀。
#
#   3.体征：大多数婴儿有发热，体温高低不一。喘憋发作时呼吸加速，呻吟并伴呼气延长和呼气性喘憋。胸部检查可见胸廓饱满，叩诊呈鼓音（或过清音），听诊可闻及哮鸣音。当喘憋缓解时，可有细湿罗音、中湿罗音。部分患儿可有明显呼吸困难，出现烦燥不安、鼻翼扇动、三凹征及口唇发绀。
#
#   4.外周血象：外周血白细胞多偏低或正常，合并细菌感染时多增高。
#
#   5.胸部X线：表现不均一，大部分病例变现为全肺程度不等的阻塞性肺气肿，约半数表现为肺纹理增厚，可出现小点片阴影，小部分病例出现肺不张。
#
#   6.肺功能：患儿急性期小气道存在阻塞，在恢复期，小气道阻塞缓解。
#
#   7.呼吸道病原学检测：本病可由不同病原所致，呼吸道合胞病毒（RSV）最常见，其次为副流感病毒、腺病毒等。
#
#     8.血气分析：血气分析显示PaO2 不同程度下降，PaCO2正常或增高，pH值与疾病严重性相关，病情较重的患儿可有代谢性酸中毒，可发生I型或II型呼吸衰竭。'''}),
#     Node("knowledge", {"name": 'mycoplasma_pneumonia',
#                        'chinese_name': '支原体肺炎',
#                        'link': 'https://www.cma.org.cn/art/2018/10/17/art_1542_123.html',
#                        'path': '''根据《临床诊疗指南－小儿内科分册》（中华医学会编著，人民卫生出版社），《诸福棠实用儿科学（第七版）》（人民卫生出版社）
#
# 1.年龄为6月-14岁。
#
# 2.咳嗽突出而持久。
#
# 3.肺部体征少而X线胸片改变出现早且明显。
#
# 4.使用青霉素无效，大环内酯类抗生素治疗效果好。
#
# 5.外周血白细胞数正常或升高。
#
# 6.血清肺炎支原体IgM抗体阳性或血清冷凝集滴度＞1:32或咽拭子分离支原体阳性，可作为临床确诊的依据。'''}),
#     Node("knowledge", {"name": 'noninvasive_thymoma',
#                        'chinese_name': '非侵袭性胸腺瘤',
#                        'link': 'https://www.cma.org.cn/art/2018/10/17/art_1542_95.html',
#                        'path': '''根据《临床诊疗指南-胸外科分册》（中华医学会编著，人民卫生出版社）。
#
# 1.病史。
#
# 2.经体检CT或者X线检查发现有前上纵膈占位性病变。
#
# 3.鉴别诊断：生殖细胞肿瘤、淋巴瘤、胸骨后甲状腺肿、侵袭性胸腺瘤等。'''}),
#     Node("knowledge", {"name": 'benign_pulmonary_tumor',
#                        'chinese_name': '肺良性肿瘤',
#                        'link': 'https://www.cma.org.cn/art/2018/10/17/art_1542_95.html',
#                        'path': '''根据《临床诊疗指南-胸外科分册》（中华医学会编著，人民卫生出版社）。
#
# 1.病史。
#
# 2.经体检CT或者X线检查发现有前上纵膈占位性病变。
#
# 3.鉴别诊断：生殖细胞肿瘤、淋巴瘤、胸骨后甲状腺肿、侵袭性胸腺瘤等。'''}),
#     Node("knowledge", {"name": 'acute_respiratory_distress_syndrome',
#                        'chinese_name': '急性呼吸窘迫综合征',
#                        'link': 'https://www.cma.org.cn/art/2018/6/8/art_1542_250.html',
#                        'path': '''根据《急性肺损伤/急性呼吸窘迫综合征诊断与治疗指南》（中华医学会重症医学分会，2006年版），同时将“柏林定义”（欧洲急危重症医学学会组建专家小组，2012年）作为补充。
#
# 1.起病时间
#
# 已知临床诱因后，1周之内或新发或原有呼吸系统症状加重。
#
# 2.胸部影像学
#
# 胸片或CT扫描，可见双肺浸润影，且不能完全用胸腔积液、肺叶/肺不张、结节解释。
#
# 3.肺水肿原因
#
# 无法用心功能衰竭或液体负荷过多解释的呼吸衰竭，如果没有危险因素，需要客观评估（如心脏超声检查）除外高静水压性肺水肿。
#
# 4.低氧血症
#
# ①轻度：200mmHg<PaO2/FiO2≤300mmHg，PEEP或CPAP≥5cmH2O（轻度ARDS患者可能采用无创通气）；②中度：100mmHg<PaO2/FiO2≤200mmHg，PEEP≥5cmH2O；③重度：PaO2/FiO2≤100mmHg，PEEP≥5cmH2O。
#
# 如果所在地区纬度高于1000米，应引入校正因子计算：[PaO2/FiO2(气压/760)]。
#
# 注：FiO2：吸入氧浓度；PaO2：动脉氧分压；PEEP：呼气末正压；CPAP：持续气道正压。'''}),
#     Node("knowledge", {"name": 'acute_upper_respiratory_infection',
#                        'chinese_name': '急性上呼吸道感染',
#                        'link': 'https://www.cma.org.cn/art/2018/6/8/art_1542_248.html',
#                        'path': '''急性上呼吸道感染的病原体以病毒最常见，包括鼻病毒、冠状病毒、肠道病毒等，细菌如流感嗜血杆菌、卡他莫拉菌、链球菌等，
#                        支原体，衣原体等亦是上呼吸道感染的病原体，
#                        前者以普通感冒为主要表现，后者以咽炎为主要表现。
#
#                        根据《普通感冒规范诊治的专家共识》（中国医师协会呼吸医师分会，中国医师协会急诊医师分会，2012年版），
#                        普通感冒一般急性起病，以鼻部卡他症状为主，可伴有发热、喷嚏、鼻塞、咽部不适等症状，
#                        在排除流行性感冒、急性细菌性鼻窦炎、过敏性鼻炎等疾病的前提下确诊。根据第八版《内科学》（葛均波，徐永健主编），
#                        非病毒感染引起的上呼吸道感染，一般以咽干不适、咽痛等咽炎症状为主，可伴有或随后出现发热、咳嗽、咳黄痰、咽部脓苔，查血常规示白细胞升高。'''}),
#     Node("knowledge", {"name": 'acute_bronchitis',
#                        'chinese_name': '急性气管支气管炎',
#                        'link': 'https://www.cma.org.cn/art/2018/6/8/art_1542_249.html',
#                        'path': '''根据全国高等学校教材《内科学》（人民卫生出版社，2013年，第8版）及《临床诊疗指南呼吸病分册》（中华医学会，人民卫生出版社）：
#
# 1、症状：起病急，通常全身症状较轻，可有发热。初为干咳或少量粘液痰，随后痰量逐渐增多，咳嗽加剧，偶伴血痰等。
#
# 2、体征：查体可无明显阳性表现。也可在两肺闻及散在干、湿性啰音，部位不固定，咳嗽后减少或消失。
#
# 3、实验室检查：白细胞计数可正常。伴有感染者，可伴有中性粒细胞百分比升高，血沉加快。X线胸片一般无异常或仅有肺纹理增粗。
#
# 4、无慢性肺部疾病者需除外肺炎。'''}),
#     Node("knowledge", {"name": 'obstructive_sleep_apnea_syndrome',
#                        'chinese_name': '阻塞性睡眠呼吸暂停综合征',
#                        'link': 'https://www.cma.org.cn/art/2018/6/8/art_1542_229.html',
#                        'path': '''根据《阻塞性睡眠呼吸暂停低通气综合征诊治指南（基层版）》（中华医学会呼吸病学分会睡眠呼吸障碍学组编著）。
#
# 主要根据病史、体征发现诊断线索；进行便携式睡眠呼吸监测确定初步诊断；有条件的可应用多导睡眠监测（PSG）确定诊断。
#
# 发现诊断线索：通过了解患者睡眠状况的家人或朋友辅助采集病史。（1）晨起口干（2）响亮而高低不均的鼾声（3）家人发现睡眠中出现呼吸中断现象（4）白天犯困。可以利用问卷评估、发现OSA高危患者。
#
# 确定初步诊断：主要利用II~IV型便携式睡眠监测设备进行初步诊断。记录参数包括呼吸气流、胸/腹运动、ECG/HR和血氧饱和度。需要有经验的专业人员判读结果。
#
# 确定诊断：有条件的单位可根据多导睡眠监测（PSG）结果确定诊断：全夜7小时的睡眠中发生呼吸暂停和/或低通气达30次以上或每小时超过5次,即睡眠呼吸暂停低通气指数（AHI）≥5次/h者，可诊断为阻塞性睡眠呼吸暂停低通气综合征（SAHS）。常伴夜间打鼾、呼吸暂停和白天嗜睡等临床症状。'''}),
]

adding_nodes = [
    # [
    #      Node('disease', {"name": 'influenza', 'chinese_name': '流行性感冒'}),
    #      Node('symptom', {"name": 'fever', 'chinese_name': '发热'}),
    #      Node('symptom', {"name": 'upper_respiratory_tract_symptoms', 'chinese_name': '上呼吸道症状'}),
    #      Node('symptom', {"name": 'original_acute_exacerbation_of_chronic_lung_diseases', 'chinese_name': '原有慢性肺部疾病急性加重'}),
    #      Node('symptom', {"name": 'Influenza_virus_nucleic_acid_test_positive', 'chinese_name': '流感病毒核酸检测阳性'}),
    #      Node('symptom', {"name": 'Influenza_virus_rapid_antigen_test_positive', 'chinese_name': '流感病毒快速抗原检测阳性'}),
    #      Node('symptom', {"name": 'Flu_viruses_isolated_culture_positive', 'chinese_name': '流感病毒分离培养阳性'}),
    #      Node('symptom', {"name": 'IgG_4_fold_or_more', 'chinese_name': '急性期和恢复期双份血清的流感病毒特异性IgG抗体水平呈4倍或4倍以上升高'}),
    #      Node('item', {"name": 'item_influenza'}),
    #      Node('item', {"name": 'item_influenza1'}),
    #      Node('item', {"name": 'item_influenza2'}),
    #      Node('item', {"name": 'item_influenza3'})
    # ],
    # [
    #     Node('disease', {"name": 'bronchopneumonia', 'chinese_name': '支气管肺炎'}),
    #     Node('symptom', {"name": 'high_fever', 'chinese_name': '高热'}),
    #     Node('symptom', {"name": 'cough', 'chinese_name': '咳嗽'}),
    #     Node('symptom', {"name": 'sputum_production', 'chinese_name': '咳痰'}),
    #     Node('symptom', {"name": 'worsening_of_preexisting_respiratory_symptoms', 'chinese_name': '原有呼吸道症状加重'}),
    #     Node('symptom', {"name": 'nasal_flaring', 'chinese_name': '鼻翼扇动'}),
    #     Node('symptom', {"name": 'cyanosis_and_triad_of_physiologic_signs', 'chinese_name': '口周发绀及三凹征'}),
    #     Node('symptom', {"name": 'bilateral_fine_creptations_in_lungs', 'chinese_name': '两肺可闻及固定性湿罗音'}),
    #     Node('symptom', {"name": 'acute_onset', 'chinese_name': '起病多较急'}),
    #     Node('symptom', {"name": 'fever', 'chinese_name': '常伴发热'}),
    #     Node('symptom', {"name": 'altered_mental_status', 'chinese_name': '可有神志或意识改变'}),
    #     Node('symptom', {"name": 'diarrhea', 'chinese_name': '腹泻'}),
    #     Node('symptom', {"name": 'vomiting', 'chinese_name': '呕吐'}),
    #     Node('symptom', {"name": 'tachycardia', 'chinese_name': '心率增快'}),
    #     Node('item', {"name": 'item_bronchopneumonia1'}),
    #     Node('item', {"name": 'item_bronchopneumonia2'}),
    #     Node('item', {"name": 'item_bronchopneumonia3'}),
    #     Node('item', {"name": 'item_bronchopneumonia4'})
    # ],
    # [
    #     Node('disease', {"name": 'chronic_bronchitis', 'chinese_name': '慢性支气管炎'}),
    #     Node('symptom', {"name": 'chronic_cough', 'chinese_name': '慢性咳嗽'}),
    #     Node('symptom', {"name": 'recurrent_cough', 'chinese_name': '反复咳嗽'}),
    #     Node('symptom', {"name": 'wheezing', 'chinese_name': '伴有喘息'})
    # ],
    # [
    #     Node('symptom', {"name": 'chest_pain', 'chinese_name': '胸痛'}),
    #     Node('symptom', {"name": 'shortness_of_breath', 'chinese_name': '呼吸困难'}),
    #     Node('symptom', {"name": 'cough', 'chinese_name': '刺激性咳嗽'}),
    #     Node('symptom', {"name": 'decreased_breath_sounds', 'chinese_name': '呼吸音减弱'}),
    #     Node('symptom', {"name": 'hyperresonance_or_dullness_on_percussion', 'chinese_name': '叩诊呈鼓音或过清音'}),
    #     Node('symptom', {"name": 'tracheal_shift', 'chinese_name': '气管向健侧移位'}),
    #     Node('symptom', {"name": 'pneumothorax_line', 'chinese_name': 'X线胸片检查气胸线'}),
    #     Node('symptom', {"name": 'lung_compression', 'chinese_name': 'X线胸片检查肺组织受压'}),
    #     Node('item', {"name": 'item_spontaneous_pneumothorax_2017'}),
    #
    # ],
    # [
    #     Node('disease', {"name": 'benign_chest_wall_tumor', 'chinese_name': '胸壁良性肿瘤'}),
    #     Node('symptom', {"name": 'local_compression_symptoms', 'chinese_name': '局部压迫症状'}),
    #     Node('symptom', {"name": 'no_symptom', 'chinese_name': '无症状'}),
    #     Node('symptom', {"name": 'palpable_mass', 'chinese_name': '可触及肿块'}),
    #     Node('symptom', {"name": 'local_tenderness', 'chinese_name': '局部压痛'}),
    #     Node('item', {"name": 'item_benign_chest_wall_tumor'}),
    # ],
    # [
    #     Node('disease', {"name": 'bronchogenic_carcinoma', 'chinese_name': '支气管肺癌'}),
    #     Node('symptom', {"name": 'smoking_history', 'chinese_name': '吸烟史'}),
    #     Node('symptom', {"name": 'old', 'chinese_name': '年龄较大'}),
    #     Node('symptom', {"name": 'cough', 'chinese_name': '刺激性咳嗽'}),
    #     Node('symptom', {"name": 'hemoptysis', 'chinese_name': '血痰或咯血'}),
    #     Node('symptom', {"name": 'chest_pain', 'chinese_name': '胸痛'}),
    #     Node('item', {"name": 'item_bronchogenic_carcinoma'})
    # ],
    # [
    #     Node('disease', {"name": 'bronchiectasis', 'chinese_name': '支气管扩张症'}),
    #     Node('symptom', {"name": 'recurrent_cough', 'chinese_name': '反复咳嗽'}),
    #     Node('symptom', {"name": 'productive_cough', 'chinese_name': '咳脓痰'}),
    #     Node('symptom', {"name": 'hemoptysis', 'chinese_name': '咯血'}),
    #     Node('symptom', {"name": 'chronic_infection', 'chinese_name': '慢性感染'}),
    #     Node('symptom', {"name": 'toxic', 'chinese_name': '中毒症状'}),
    #     Node('symptom', {"name": 'wheezing', 'chinese_name': '哮鸣音'}),
    #     Node('symptom', {"name": 'rhonchi', 'chinese_name': '湿罗音'}),
    #     Node('symptom', {"name": 'dyspnea', 'chinese_name': '呼吸困难'}),
    #     Node('symptom', {"name": 'cyanosis', 'chinese_name': '紫绀'}),
    #     Node('symptom', {"name": 'clubbing', 'chinese_name': '杵状指（趾）'}),
    #     Node('symptom', {"name": 'abnormal_bronchiectasis_changes', 'chinese_name': '支气管扩张的异常改变'}),
    #     Node('item', {"name": 'item_bronchiectasis'}),
    #     Node('item', {"name": 'item_bronchiectasis1'}),
    # ],
    # [
    #     Node('disease', {"name": 'bronchiolitis', 'chinese_name': '毛细支气管炎'}),
    #     Node('symptom', {"name": 'young_age', 'chinese_name': '年龄小'}),
    #     Node('symptom', {"name": 'low_grade_fever', 'chinese_name': '低热'}),
    #     Node('symptom', {"name": 'runny_nose', 'chinese_name': '流涕'}),
    #     Node('symptom', {"name": 'nasal_congestion', 'chinese_name': '鼻塞'}),
    #     Node('symptom', {"name": 'cough', 'chinese_name': '咳嗽'}),
    #     Node('symptom', {"name": 'high_fever', 'chinese_name': '高热'}),
    #     Node('symptom', {"name": 'malaise', 'chinese_name': '精神不振'}),
    #     Node('symptom', {"name": 'loss_of_appetite', 'chinese_name': '食欲减退'}),
    #     Node('symptom', {"name": 'lower_respiratory_tract_symptoms', 'chinese_name': '下呼吸道症状'}),
    #     Node('symptom', {"name": 'aggravated_cough', 'chinese_name': '咳嗽明显加重'}),
    #     Node('symptom', {"name": 'wheezing', 'chinese_name': '喘息发作'}),
    #     Node('symptom', {"name": 'significant_dyspnea', 'chinese_name': '明显喘憋'}),
    #     Node('symptom', {"name": 'wheezing', 'chinese_name': '哮鸣音'}),
    #     Node('symptom', {"name": 'fine_crackles', 'chinese_name': '细湿罗音'}),
    #     Node('symptom', {"name": 'upper_respiratory_tract_infection_symptoms', 'chinese_name': '上呼吸道感染的症状'}),
    #     Node('symptom', {"name": 'fever', 'chinese_name': '发热'}),
    #     Node('symptom', {"name": 'cough', 'chinese_name': '咳嗽'}),
    #     Node('symptom', {"name": 'respiratory_distress', 'chinese_name': '喘憋发作'}),
    #     Node('symptom', {"name": 'cyanosis', 'chinese_name': '紫绀'}),
    #     Node('symptom', {"name": 'tachypnea', 'chinese_name': '呼吸加速'}),
    #     Node('symptom', {"name": 'prolonged_expiration', 'chinese_name': '呼气延长'}),
    #     Node('symptom', {"name": 'expiratory_wheezing', 'chinese_name': '呼气性喘憋'}),
    #     Node('symptom', {"name": 'full_chest', 'chinese_name': '胸廓饱满'}),
    #     Node('symptom', {"name": 'hyperresonance', 'chinese_name': '叩诊呈鼓音'}),
    #     Node('symptom', {"name": 'dyspnea', 'chinese_name': '呼吸困难'}),
    #     Node('symptom', {"name": 'restlessness', 'chinese_name': '烦燥不安'}),
    #     Node('symptom', {"name": 'flaring_nostrils', 'chinese_name': '鼻翼扇动'}),
    #     Node('symptom', {"name": 'triangular_nasal_flaring', 'chinese_name': '三凹征'}),
    #     Node('symptom', {"name": 'cyanotic_lips', 'chinese_name': '口唇发绀'}),
    #     Node('symptom', {"name": 'leukopenia_white_blood_cell_count', 'chinese_name': '外周血白细胞偏低'}),
    #     Node('symptom', {"name": 'obstructive_emphysema_of_varying_degree_in_all_lungs', 'chinese_name': '全肺程度不等的阻塞性肺气肿'}),
    #     Node('symptom', {"name": 'thickening_of_lung_markings', 'chinese_name': '肺纹理增厚'}),
    #     Node('symptom', {"name": 'small_patches_of_shadows', 'chinese_name': '出现小点片阴影'}),
    #     Node('symptom', {"name": 'lung_atelectasis', 'chinese_name': '肺不张'}),
    #     Node('symptom', {"name": 'obstructive_airway_disease_in_acute_phase', 'chinese_name': '急性期小气道存在阻塞'}),
    #     Node('symptom', {"name": 'decreased_paO2_at_various_levels', 'chinese_name': 'PaO2不同程度下降'}),
    #     Node('symptom', {"name": 'normal_or_increased_paCO2', 'chinese_name': 'PaCO2正常或增高'}),
    #     Node('symptom', {"name": 'pH_value_correlates_with_disease_severity', 'chinese_name': 'pH值与疾病严重性相关'}),
    #     Node('symptom', {"name": 'metabolic_acidosis', 'chinese_name': '代谢性酸中毒'}),
    #     Node('symptom', {"name": 'type_i_respiratory_failure', 'chinese_name': 'I型呼吸衰竭'}),
    #     Node('symptom', {"name": 'type_ii_respiratory_failure', 'chinese_name': 'II型呼吸衰竭'}),
    #     Node('item', {"name": 'item_bronchiolitis1'}),
    #     Node('item', {"name": 'item_bronchiolitis2'}),
    #     Node('item', {"name": 'item_bronchiolitis3'}),
    #     Node('item', {"name": 'item_bronchiolitis4'}),
    #     Node('item', {"name": 'item_bronchiolitis5'}),
    #     Node('item', {"name": 'item_bronchiolitis6'}),
    #     Node('item', {"name": 'item_bronchiolitis7'}),
    #     Node('item', {"name": 'item_bronchiolitis21'}),
    #     Node('item', {"name": 'item_bronchiolitis31'}),
    # ],
    # [
    #     Node('disease', {"name": 'mycoplasma_pneumonia', 'chinese_name': '支原体肺炎'}),
    #     Node('symptom', {"name": 'child', 'chinese_name': '儿童'}),
    #     Node('symptom', {"name": 'persistent_cough', 'chinese_name': '持久咳嗽'}),
    #     Node('symptom', {"name": 'less_lung_signs', 'chinese_name': '肺部体征少'}),
    #     Node('symptom', {"name": 'early_and_obvious_chest_X-ray_changes', 'chinese_name': '早期明显胸部X线改变'}),
    #     Node('symptom', {"name": 'ineffective_with_penicillin', 'chinese_name': '青霉素无效'}),
    #     Node('symptom', {"name": 'effective_with_macrolides', 'chinese_name': '大环内酯类抗生素治疗效果好'}),
    #     Node('symptom', {"name": 'normal_peripheral_blood_white_cell_count', 'chinese_name': '外周血白细胞数正常'}),
    #     Node('symptom', {"name": 'elevated_peripheral_blood_white_cell_count', 'chinese_name': '外周血白细胞数升高'}),
    #     Node('symptom', {"name": 'positive_with_mycoplasma_pneumonia_IgM_antibody', 'chinese_name': '血清肺炎支原体IgM抗体阳性'}),
    #     Node('symptom', {"name": 'positive_with_cold_agglutination_titer_greater_than_1:32', 'chinese_name': '血清冷凝集滴度＞1:32'}),
    #     Node('symptom', {"name": 'positive_with_pharyngeal_swab_isolation_of_mycoplasma_pneumoniae', 'chinese_name': '咽拭子分离支原体阳性'}),
    #     Node('item', {"name": 'item_mycoplasma_pneumonia1'}),
    #     Node('item', {"name": 'item_mycoplasma_pneumonia2'}),
    # ],
    # [
    #     Node('disease', {"name": 'spontaneous_pneumothorax'}),
    #     Node('symptom', {"name": 'sudden_chest_pain', 'chinese_name': '突发患侧胸痛'}),
    #     Node('symptom', {"name": 'dyspnea', 'chinese_name': '喘憋'}),
    #     Node('symptom', {"name": 'respiratory_distress', 'chinese_name': '呼吸困难'}),
    #     Node('symptom', {"name": 'occasional_dry_cough', 'chinese_name': '偶尔有干咳'}),
    #     Node('symptom', {"name": 'chest_fullness_on_the_affected_side', 'chinese_name': '患侧胸部饱满'}),
    #     Node('symptom', {"name": 'reduced_breathing_movement', 'chinese_name': '呼吸运动减弱'}),
    #     Node('symptom', {"name": 'tympanic_percussion_note', 'chinese_name': '叩诊呈鼓音'}),
    #     Node('symptom', {"name": 'decreased_or_absent_breath_sounds_and_vocal_resonance', 'chinese_name': '语颤和呼吸音均减低或消失'}),
    #     Node('symptom', {"name": 'tracheal_deviation_to_the_contralateral_side', 'chinese_name': '气管向健侧移位'}),
    #     Node('item', {"name": 'item_spontaneous_pneumothorax1'}),
    #     Node('item', {"name": 'item_spontaneous_pneumothorax2'}),
    #     Node('item', {"name": 'item_spontaneous_pneumothorax_2012'}),
    # ],
    # [
    #     Node('disease', {"name": 'noninvasive_thymoma', 'chinese_name': '非侵袭性胸腺瘤'}),
    #     Node('symptom', {"name": 'occupying_lesion_in_the_anterior_superior_mediastinum', 'chinese_name': '经体检CT或者X线检查发现有前上纵膈占位性病变'})
    # ],
    # [
    #     Node('disease', {"name": 'benign_pulmonary_tumor', 'chinese_name': '肺良性肿瘤'}),
    #     Node('symptom', {"name": 'no_symptom', 'chinese_name': '症状较轻或无'}),
    #     Node('symptom', {"name": 'cough', 'chinese_name': '咳嗽'}),
    #     Node('symptom', {"name": 'hemoptysis', 'chinese_name': '咯血'}),
    #     Node('symptom', {"name": 'mild_chest_pain', 'chinese_name': '轻度胸痛'}),
    #     Node('symptom', {"name": 'long-term_stable_condition', 'chinese_name': '病情可长期无变化'}),
    #     Node('symptom', {"name": 'secondary_infection_due_to_tumor_blocking_bronchus', 'chinese_name': '因肿瘤阻塞支气管而继发感染症状'}),
    #     Node('symptom', {"name": 'insignificant_signs_in_early_stage', 'chinese_name': '早期不显著'}),
    # ],
    # [
    #     Node('disease', {"name": 'acute_respiratory_distress_syndrome', 'chinese_name': '急性呼吸窘迫综合征'}),
    #     Node('symptom', {"name": 'onset_within_1_week_of_knowing_clinical_trigger', 'chinese_name': '已知临床诱因后，1周之内或新发或原有呼吸系统症状加重'}),
    #     Node('symptom', {"name": 'bilateral_lung_infiltrates', 'chinese_name': '胸片或CT扫描，可见双肺浸润影'}),
    #     Node('symptom', {"name": 'respiratory_failure_not_explained_by_heart_failure_or_fluid_overload', 'chinese_name': '无法用心功能衰竭或液体负荷过多解释的呼吸衰竭'}),
    #     Node('symptom', {"name": 'mild_hypoxemia', 'chinese_name': '轻度低氧血症：200mmHg<PaO2/FiO2≤300mmHg，PEEP或CPAP≥5cmH2O（轻度ARDS患者可能采用无创通气）'}),
    #     Node('symptom', {"name": 'moderate_hypoxemia', 'chinese_name': '中度低氧血症：100mmHg<PaO2/FiO2≤200mmHg，PEEP≥5cmH2O'}),
    #     Node('symptom', {"name": 'severe_hypoxemia', 'chinese_name': '重度低氧血症：PaO2/FiO2≤100mmHg，PEEP≥5cmH2O'}),
    #     Node('item', {"name": 'item_acute_respiratory_distress_syndrome'}),
    # ],
    # [
    #     Node('disease', {"name": 'acute_upper_respiratory_infection', 'chinese_name': '急性上呼吸道感染'}),
    #     Node('item', {"name": 'common_cold', 'chinese_name': '普通感冒：急性起病，以鼻部卡他症状为主，可伴有发热、喷嚏、鼻塞、咽部不适等症状'}),
    #     Node('item', {"name": 'item_common_cold'}),
    #     Node('item',
    #          {"name": 'pharyngitis', 'chinese_name': '咽炎：一般以咽干不适、咽痛等咽炎症状为主，可伴有或随后出现发热、咳嗽、咳黄痰、咽部脓苔，查血常规示白细胞升高'}),
    #     Node('item',
    #          {"name": 'item_pharyngitis'}),
    #     Node('symptom', {"name": 'nasal_catarrh_symptoms', 'chinese_name': '鼻部卡他症状'}),
    #     Node('symptom', {"name": 'fever', 'chinese_name': '发热'}),
    #     Node('symptom', {"name": 'sneezing', 'chinese_name': '喷嚏'}),
    #     Node('symptom', {"name": 'nasal_congestion', 'chinese_name': '鼻塞'}),
    #     Node('symptom', {"name": 'throat_discomfort', 'chinese_name': '咽部不适'}),
    #     Node('symptom', {"name": 'cough', 'chinese_name': '咳嗽'}),
    #     Node('symptom', {"name": 'yellow_sputum', 'chinese_name': '咳黄痰'}),
    #     Node('symptom', {"name": 'pharyngeal_exudate', 'chinese_name': '咽部脓苔'}),
    #     Node('symptom', {"name": 'elevated_white_blood_cells', 'chinese_name': '白细胞升高'})
    # ],
    # [
    #     Node('disease', {"name": 'acute_bronchitis', 'chinese_name': '急性气管支气管炎'}),
    #     Node('symptom', {"name": 'sudden_onset', 'chinese_name': '起病急'}),
    #     Node('symptom', {"name": 'mild_systemic_symptoms', 'chinese_name': '通常全身症状较轻，可有发热'}),
    #     Node('symptom', {"name": 'dry_cough', 'chinese_name': '初为干咳或少量粘液痰'}),
    #     Node('symptom', {"name": 'increased_sputum_production', 'chinese_name': '随后痰量逐渐增多'}),
    #     Node('symptom', {"name": 'worsening_cough', 'chinese_name': '咳嗽加剧'}),
    #     Node('symptom', {"name": 'hemoptysis', 'chinese_name': '偶伴血痰'}),
    #     Node('symptom', {"name": 'no_obvious_positive_signs', 'chinese_name': '查体可无明显阳性表现'}),
    #     Node('symptom', {"name": 'rales', 'chinese_name': '两肺闻及散在干、湿性啰音，部位不固定，咳嗽后减少或消失'}),
    #     Node('symptom', {"name": 'normal_white_blood_cell_count', 'chinese_name': '白细胞计数可正常'}),
    #     Node('symptom', {"name": 'elevated_neutrophil_percentage', 'chinese_name': '伴有感染者，可伴有中性粒细胞百分比升高'}),
    #     Node('symptom', {"name": 'increased_blood_sedimentation_rate', 'chinese_name': '血沉加快'}),
    #     Node('symptom', {"name": 'normal_chest_x_ray', 'chinese_name': 'X线胸片一般无异常或仅有肺纹理增粗'}),
    #     Node('item', {"name": 'item_acute_bronchitis1'}),
    #     Node('item', {"name": 'item_acute_bronchitis2'}),
    #     Node('item', {"name": 'item_acute_bronchitis3'}),
    #     Node('item', {"name": 'item_acute_bronchitis11'}),
    # ],
    # [
    #     Node('disease', {"name": 'obstructive_sleep_apnea_syndrome', 'chinese_name': '阻塞性睡眠呼吸暂停综合征'}),
    #     Node('symptom', {"name": 'dry_mouth_on_awakening', 'chinese_name': '晨起口干'}),
    #     Node('symptom', {"name": 'loud_snoring', 'chinese_name': '响亮而高低不均的鼾声'}),
    #     Node('symptom', {"name": 'breathing_pause_during_sleep', 'chinese_name': '睡眠中出现呼吸中断现象'}),
    #     Node('symptom', {"name": 'daytime_sleepiness', 'chinese_name': '白天犯困'}),
    #     Node('symptom', {"name": 'breathing_pause_or_hypopnea', 'chinese_name': '全夜7小时的睡眠中发生呼吸暂停和/或低通气达30次以上或每小时超过5次'}),
    #     Node('symptom', {"name": 'AHI_greater_than_5', 'chinese_name': '睡眠呼吸暂停低通气指数（AHI）≥5次/h'}),
    #     Node('symptom', {"name": 'nighttime_snoring', 'chinese_name': '常伴夜间打鼾'}),
    #     Node('item', {"name": 'item_obstructive_sleep_apnea_syndrome1'}),
    #     Node('item', {"name": 'item_obstructive_sleep_apnea_syndrome2'}),
    # ],
]

adding_paths = [
    [
        Edge('HAS_BRANCH_COMBINATION', 'influenza', 'and'),
        Edge('HAS_BRANCH_COMBINATION', 'item_influenza', 'or'),
        Edge('HAS_BRANCH_COMBINATION', 'item_influenza1', 'or'),
        Edge('HAS_BRANCH_COMBINATION', 'item_influenza2', 'and'),
        Edge('HAS_BRANCH', 'influenza', 'item_influenza'),
        Edge('HAS_BRANCH', 'influenza', 'item_influenza1'),
        Edge('HAS_BRANCH', 'item_influenza', 'item_influenza2'),
        Edge('HAS_BRANCH', 'item_influenza', 'original_acute_exacerbation_of_chronic_lung_diseases'),
        Edge('HAS_BRANCH', 'item_influenza2', 'upper_respiratory_tract_symptoms'),
        Edge('HAS_BRANCH', 'item_influenza2', 'fever'),
        Edge('HAS_BRANCH', 'item_influenza1', 'Influenza_virus_nucleic_acid_test_positive'),
        Edge('HAS_BRANCH', 'item_influenza1', 'Influenza_virus_rapid_antigen_test_positive'),
        Edge('HAS_BRANCH', 'item_influenza1', 'Flu_viruses_isolated_culture_positive'),
        Edge('HAS_BRANCH', 'item_influenza1', 'IgG_4_fold_or_more')
    ],
    [
        Edge('HAS_BRANCH_COMBINATION', 'bronchopneumonia', 'and'),
        Edge('HAS_BRANCH_COMBINATION', 'item_bronchopneumonia1', 'or'),
        Edge('HAS_BRANCH_COMBINATION', 'item_bronchopneumonia3', 'or'),
        Edge('HAS_BRANCH_COMBINATION', 'item_bronchopneumonia4', 'or'),
        Edge('HAS_BRANCH_COMBINATION', 'item_bronchopneumonia2', 'or'),
        Edge('HAS_BRANCH', 'bronchopneumonia', 'item_bronchopneumonia1'),
        Edge('HAS_BRANCH', 'bronchopneumonia', 'item_bronchopneumonia2'),
        Edge('HAS_BRANCH', 'item_bronchopneumonia1', 'item_bronchopneumonia3'),
        Edge('HAS_BRANCH', 'item_bronchopneumonia1', 'item_bronchopneumonia4'),
        Edge('HAS_BRANCH', 'item_bronchopneumonia3', 'cough'),
        Edge('HAS_BRANCH', 'item_bronchopneumonia3', 'sputum_production'),
        Edge('HAS_BRANCH', 'item_bronchopneumonia3', 'worsening_of_preexisting_respiratory_symptoms'),
        Edge('HAS_BRANCH', 'item_bronchopneumonia4', 'nasal_flaring'),
        Edge('HAS_BRANCH', 'item_bronchopneumonia4', 'cyanosis_and_triad_of_physiologic_signs'),
        Edge('HAS_BRANCH', 'item_bronchopneumonia1', 'bilateral_fine_creptations_in_lungs'),
        Edge('HAS_BRANCH', 'item_bronchopneumonia2', 'fever'),
        Edge('HAS_BRANCH', 'item_bronchopneumonia2', 'acute_onset'),
        Edge('HAS_BRANCH', 'item_bronchopneumonia2', 'altered_mental_status'),
        Edge('HAS_BRANCH', 'item_bronchopneumonia2', 'diarrhea'),
        Edge('HAS_BRANCH', 'item_bronchopneumonia2', 'vomiting'),
        Edge('HAS_BRANCH', 'item_bronchopneumonia2', 'tachycardia')
    ],
    [
        Edge('HAS_BRANCH_COMBINATION', 'chronic_bronchitis', 'or'),
        Edge('HAS_BRANCH', 'chronic_bronchitis', 'chronic_cough'),
        Edge('HAS_BRANCH', 'chronic_bronchitis', 'recurrent_cough'),
        Edge('HAS_BRANCH', 'chronic_bronchitis', 'sputum_production'),
        Edge('HAS_BRANCH', 'chronic_bronchitis', 'wheezing')
    ],
    # [
    #     Edge('HAS_BRANCH_COMBINATION', 'item_spontaneous_pneumothorax_2017', 'and'),
    #     Edge('HAS_BRANCH', 'item_spontaneous_pneumothorax_2017', 'x_ray_pneumothorax_line'),
    #     Edge('HAS_BRANCH', 'item_spontaneous_pneumothorax_2017', 'x_ray_lung_compression'),
    #     Edge('HAS_BRANCH', 'item_spontaneous_pneumothorax_2017', 'chest_pain'),
    #     Edge('HAS_BRANCH', 'item_spontaneous_pneumothorax_2017', 'shortness_of_breath'),
    #     Edge('HAS_BRANCH', 'item_spontaneous_pneumothorax_2017', 'cough'),
    #     Edge('HAS_BRANCH', 'item_spontaneous_pneumothorax_2017', 'decreased_breath_sounds'),
    #     Edge('HAS_BRANCH', 'item_spontaneous_pneumothorax_2017', 'hyperresonance_or_dullness_on_percussion'),
    #     Edge('HAS_BRANCH', 'item_spontaneous_pneumothorax_2017', 'tracheal_shift')
    # ],
    [
        Edge('HAS_BRANCH_COMBINATION', 'benign_chest_wall_tumor', 'and'),
        Edge('HAS_BRANCH_COMBINATION', 'item_benign_chest_wall_tumor', 'or'),
        Edge('HAS_BRANCH', 'benign_chest_wall_tumor', 'palpable_mass'),
        Edge('HAS_BRANCH', 'benign_chest_wall_tumor', 'item_benign_chest_wall_tumor'),
        Edge('HAS_BRANCH', 'item_benign_chest_wall_tumor', 'local_compression_symptoms'),
        Edge('HAS_BRANCH', 'item_benign_chest_wall_tumor', 'no_symptom'),
        Edge('HAS_BRANCH', 'item_benign_chest_wall_tumor', 'local_tenderness')
    ],
    [
        Edge('HAS_BRANCH_COMBINATION', 'bronchogenic_carcinoma', 'or'),
        Edge('HAS_BRANCH_COMBINATION', 'item_bronchogenic_carcinoma', 'and'),
        Edge('HAS_BRANCH', 'bronchogenic_carcinoma', 'item_bronchogenic_carcinoma'),
        Edge('HAS_BRANCH', 'bronchogenic_carcinoma', 'smoking_history'),
        Edge('HAS_BRANCH', 'bronchogenic_carcinoma', 'old'),
        Edge('HAS_BRANCH', 'item_bronchogenic_carcinoma', 'cough'),
        Edge('HAS_BRANCH', 'item_bronchogenic_carcinoma', 'hemoptysis'),
        Edge('HAS_BRANCH', 'item_bronchogenic_carcinoma', 'chest_pain'),
    ],
    [
        Edge('HAS_BRANCH_COMBINATION', 'bronchiectasis', 'or'),
        Edge('HAS_BRANCH_COMBINATION', 'item_bronchiectasis', 'and'),
        Edge('HAS_BRANCH_COMBINATION', 'item_bronchiectasis1', 'or'),
        Edge('HAS_BRANCH', 'bronchiectasis', 'item_bronchiectasis'),
        Edge('HAS_BRANCH', 'bronchiectasis', 'wheezing'),
        Edge('HAS_BRANCH', 'bronchiectasis', 'rhonchi'),
        Edge('HAS_BRANCH', 'bronchiectasis', 'dyspnea'),
        Edge('HAS_BRANCH', 'bronchiectasis', 'cyanosis'),
        Edge('HAS_BRANCH', 'bronchiectasis', 'clubbing'),
        Edge('HAS_BRANCH', 'abnormal_bronchiectasis_changes', 'clubbing'),
        Edge('HAS_BRANCH', 'item_bronchiectasis', 'recurrent_cough'),
        Edge('HAS_BRANCH', 'item_bronchiectasis', 'productive_cough'),
        Edge('HAS_BRANCH', 'item_bronchiectasis', 'hemoptysis'),
        Edge('HAS_BRANCH', 'item_bronchiectasis', 'item_bronchiectasis1'),
        Edge('HAS_BRANCH', 'item_bronchiectasis1', 'chronic_infection'),
        Edge('HAS_BRANCH', 'item_bronchiectasis1', 'toxic'),
    ],
    [
        Edge('HAS_BRANCH_COMBINATION', 'bronchiolitis', 'and'),
        Edge('HAS_BRANCH_COMBINATION', 'item_bronchiolitis1', 'or'),
        Edge('HAS_BRANCH_COMBINATION', 'item_bronchiolitis2', 'or'),
        Edge('HAS_BRANCH_COMBINATION', 'item_bronchiolitis3', 'or'),
        Edge('HAS_BRANCH_COMBINATION', 'item_bronchiolitis4', 'or'),
        Edge('HAS_BRANCH_COMBINATION', 'item_bronchiolitis5', 'or'),
        Edge('HAS_BRANCH_COMBINATION', 'item_bronchiolitis6', 'or'),
        Edge('HAS_BRANCH_COMBINATION', 'item_bronchiolitis7', 'and'),
        Edge('HAS_BRANCH_COMBINATION', 'item_bronchiolitis21', 'and'),
        Edge('HAS_BRANCH_COMBINATION', 'item_bronchiolitis31', 'and'),
        Edge('HAS_BRANCH', 'bronchiolitis', 'item_bronchiolitis1'),
        Edge('HAS_BRANCH', 'bronchiolitis', 'item_bronchiolitis2'),
        Edge('HAS_BRANCH', 'bronchiolitis', 'item_bronchiolitis3'),
        Edge('HAS_BRANCH', 'bronchiolitis', 'item_bronchiolitis4'),
        Edge('HAS_BRANCH', 'bronchiolitis', 'item_bronchiolitis5'),
        Edge('HAS_BRANCH', 'bronchiolitis', 'item_bronchiolitis6'),
        Edge('HAS_BRANCH', 'bronchiolitis', 'item_bronchiolitis7'),
        Edge('HAS_BRANCH', 'item_bronchiolitis1', 'young_age'),
        Edge('HAS_BRANCH', 'item_bronchiolitis21', 'low_grade_fever'),
        Edge('HAS_BRANCH', 'item_bronchiolitis21', 'runny_nose'),
        Edge('HAS_BRANCH', 'item_bronchiolitis21', 'nasal_congestion'),
        Edge('HAS_BRANCH', 'item_bronchiolitis21', 'cough'),
        Edge('HAS_BRANCH', 'item_bronchiolitis21', 'high_fever'),
        Edge('HAS_BRANCH', 'item_bronchiolitis21', 'malaise'),
        Edge('HAS_BRANCH', 'item_bronchiolitis21', 'loss_of_appetite'),
        Edge('HAS_BRANCH', 'item_bronchiolitis2', 'lower_respiratory_tract_symptoms'),
        Edge('HAS_BRANCH', 'item_bronchiolitis2', 'aggravated_cough'),
        Edge('HAS_BRANCH', 'item_bronchiolitis2', 'wheezing'),
        Edge('HAS_BRANCH', 'item_bronchiolitis2', 'respiratory_distress'),
        Edge('HAS_BRANCH', 'item_bronchiolitis2', 'item_bronchiolitis21'),
        Edge('HAS_BRANCH', 'item_bronchiolitis2', 'significant_dyspnea'),
        Edge('HAS_BRANCH', 'item_bronchiolitis2', 'cyanosis'),
        Edge('HAS_BRANCH', 'item_bronchiolitis31', 'fever'),
        Edge('HAS_BRANCH', 'item_bronchiolitis31', 'respiratory_distress'),
        Edge('HAS_BRANCH', 'item_bronchiolitis31', 'tachypnea'),
        Edge('HAS_BRANCH', 'item_bronchiolitis31', 'prolonged_expiration'),
        Edge('HAS_BRANCH', 'item_bronchiolitis31', 'expiratory_wheezing'),
        Edge('HAS_BRANCH', 'item_bronchiolitis31', 'full_chest'),
        Edge('HAS_BRANCH', 'item_bronchiolitis31', 'hyperresonance'),
        Edge('HAS_BRANCH', 'item_bronchiolitis3', 'item_bronchiolitis31'),
        Edge('HAS_BRANCH', 'item_bronchiolitis3', 'dyspnea'),
        Edge('HAS_BRANCH', 'item_bronchiolitis3', 'restlessness'),
        Edge('HAS_BRANCH', 'item_bronchiolitis3', 'flaring_nostrils'),
        Edge('HAS_BRANCH', 'item_bronchiolitis3', 'triangular_nasal_flaring'),
        Edge('HAS_BRANCH', 'item_bronchiolitis3', 'cyanotic_lips'),
        Edge('HAS_BRANCH', 'item_bronchiolitis4', 'leukopenia_white_blood_cell_count'),
        Edge('HAS_BRANCH', 'item_bronchiolitis5', 'obstructive_emphysema_of_varying_degree_in_all_lungs'),
        Edge('HAS_BRANCH', 'item_bronchiolitis5', 'thickening_of_lung_markings'),
        Edge('HAS_BRANCH', 'item_bronchiolitis5', 'small_patches_of_shadows'),
        Edge('HAS_BRANCH', 'item_bronchiolitis5', 'lung_atelectasis'),
        Edge('HAS_BRANCH', 'item_bronchiolitis6', 'obstructive_airway_disease_in_acute_phase'),
        Edge('HAS_BRANCH', 'item_bronchiolitis7', 'decreased_paO2_at_various_levels'),
        Edge('HAS_BRANCH', 'item_bronchiolitis7', 'normal_or_increased_paCO2'),
        Edge('HAS_BRANCH', 'item_bronchiolitis7', 'pH_value_correlates_with_disease_severity'),
        Edge('HAS_BRANCH', 'item_bronchiolitis7', 'metabolic_acidosis'),
        Edge('HAS_BRANCH', 'item_bronchiolitis7', 'type_ii_respiratory_failure'),
        Edge('HAS_BRANCH', 'item_bronchiolitis7', 'type_i_respiratory_failure')
    ],
    [
        Edge('HAS_BRANCH_COMBINATION', 'mycoplasma_pneumonia', 'and'),
        Edge('HAS_BRANCH_COMBINATION', 'item_mycoplasma_pneumonia1', 'or'),
        Edge('HAS_BRANCH_COMBINATION', 'item_mycoplasma_pneumonia2', 'or'),
        Edge('HAS_BRANCH', 'mycoplasma_pneumonia', 'item_mycoplasma_pneumonia1'),
        Edge('HAS_BRANCH', 'mycoplasma_pneumonia', 'item_mycoplasma_pneumonia2'),
        Edge('HAS_BRANCH', 'mycoplasma_pneumonia', 'child'),
        Edge('HAS_BRANCH', 'mycoplasma_pneumonia', 'persistent_cough'),
        Edge('HAS_BRANCH', 'mycoplasma_pneumonia', 'less_lung_signs'),
        Edge('HAS_BRANCH', 'mycoplasma_pneumonia', 'early_and_obvious_chest_X-ray_changes'),
        Edge('HAS_BRANCH', 'mycoplasma_pneumonia', 'ineffective_with_penicillin'),
        Edge('HAS_BRANCH', 'mycoplasma_pneumonia', 'effective_with_macrolides'),
        Edge('HAS_BRANCH', 'item_mycoplasma_pneumonia1', 'normal_peripheral_blood_white_cell_count'),
        Edge('HAS_BRANCH', 'item_mycoplasma_pneumonia1', 'elevated_peripheral_blood_white_cell_count'),
        Edge('HAS_BRANCH', 'item_mycoplasma_pneumonia2', 'positive_with_mycoplasma_pneumonia_IgM_antibody'),
        Edge('HAS_BRANCH', 'item_mycoplasma_pneumonia2', 'positive_with_cold_agglutination_titer_greater_than_1:32'),
        Edge('HAS_BRANCH', 'item_mycoplasma_pneumonia2', 'positive_with_pharyngeal_swab_isolation_of_mycoplasma_pneumoniae')
    ],
    # [
    #     Edge('HAS_BRANCH_COMBINATION', 'spontaneous_pneumothorax', 'or'),
    #     Edge('HAS_BRANCH', 'spontaneous_pneumothorax', 'item_spontaneous_pneumothorax_2012'),
    #     Edge('HAS_BRANCH', 'spontaneous_pneumothorax', 'item_spontaneous_pneumothorax_2017'),
    #     Edge('HAS_BRANCH_COMBINATION', 'item_spontaneous_pneumothorax_2012', 'and'),
    #     Edge('HAS_BRANCH_COMBINATION', 'item_spontaneous_pneumothorax1', 'and'),
    #     Edge('HAS_BRANCH_COMBINATION', 'item_spontaneous_pneumothorax2', 'or'),
    #     Edge('HAS_BRANCH', 'item_spontaneous_pneumothorax_2012', 'item_spontaneous_pneumothorax1'),
    #     Edge('HAS_BRANCH', 'item_spontaneous_pneumothorax_2012', 'item_spontaneous_pneumothorax2'),
    #     Edge('HAS_BRANCH', 'item_spontaneous_pneumothorax1', 'sudden_chest_pain'),
    #     Edge('HAS_BRANCH', 'item_spontaneous_pneumothorax1', 'dyspnea'),
    #     Edge('HAS_BRANCH', 'item_spontaneous_pneumothorax1', 'respiratory_distress'),
    #     Edge('HAS_BRANCH', 'item_spontaneous_pneumothorax1', 'occasional_dry_cough'),
    #     Edge('HAS_BRANCH', 'item_spontaneous_pneumothorax_2012', 'item_spontaneous_pneumothorax2'),
    #     Edge('HAS_BRANCH', 'item_spontaneous_pneumothorax2', 'chest_fullness_on_the_affected_side'),
    #     Edge('HAS_BRANCH', 'item_spontaneous_pneumothorax2', 'reduced_breathing_movement'),
    #     Edge('HAS_BRANCH', 'item_spontaneous_pneumothorax2', 'tympanic_percussion_note'),
    #     Edge('HAS_BRANCH', 'item_spontaneous_pneumothorax2', 'decreased_or_absent_breath_sounds_and_vocal_resonance'),
    #     Edge('HAS_BRANCH', 'item_spontaneous_pneumothorax2', 'tracheal_deviation_to_the_contralateral_side'),
    #     Edge('HAS_BRANCH', 'item_spontaneous_pneumothorax2', 'no_symptom'),
    # ],
    [
        Edge('HAS_BRANCH_COMBINATION', 'noninvasive_thymoma', 'and'),
        Edge('HAS_BRANCH', 'noninvasive_thymoma', 'occupying_lesion_in_the_anterior_superior_mediastinum'),
    ],
    [
        Edge('HAS_BRANCH_COMBINATION', 'benign_pulmonary_tumor', 'or'),
        Edge('HAS_BRANCH', 'benign_pulmonary_tumor', 'no_symptom'),
        Edge('HAS_BRANCH', 'benign_pulmonary_tumor', 'cough'),
        Edge('HAS_BRANCH', 'benign_pulmonary_tumor', 'hemoptysis'),
        Edge('HAS_BRANCH', 'benign_pulmonary_tumor', 'mild_chest_pain'),
        Edge('HAS_BRANCH', 'benign_pulmonary_tumor', 'long-term_stable_condition'),
        Edge('HAS_BRANCH', 'benign_pulmonary_tumor', 'secondary_infection_due_to_tumor_blocking_bronchus'),
        Edge('HAS_BRANCH', 'benign_pulmonary_tumor', 'insignificant_signs_in_early_stage')
    ],
    [
        Edge('HAS_BRANCH_COMBINATION', 'acute_respiratory_distress_syndrome', 'and'),
        Edge('HAS_BRANCH_COMBINATION', 'item_acute_respiratory_distress_syndrome', 'or'),
        Edge('HAS_BRANCH', 'acute_respiratory_distress_syndrome', 'onset_within_1_week_of_knowing_clinical_trigger'),
        Edge('HAS_BRANCH', 'acute_respiratory_distress_syndrome', 'bilateral_lung_infiltrates'),
        Edge('HAS_BRANCH', 'acute_respiratory_distress_syndrome',
             'respiratory_failure_not_explained_by_heart_failure_or_fluid_overload'),
        Edge('HAS_BRANCH', 'acute_respiratory_distress_syndrome', 'item_acute_respiratory_distress_syndrome'),
        Edge('HAS_BRANCH', 'item_acute_respiratory_distress_syndrome', 'mild_hypoxemia'),
        Edge('HAS_BRANCH', 'item_acute_respiratory_distress_syndrome', 'moderate_hypoxemia'),
        Edge('HAS_BRANCH', 'item_acute_respiratory_distress_syndrome', 'severe_hypoxemia')
    ],
    [
        Edge('HAS_BRANCH_COMBINATION', 'acute_upper_respiratory_infection', 'or'),
        Edge('HAS_BRANCH_COMBINATION', 'common_cold', 'and'),
        Edge('HAS_BRANCH_COMBINATION', 'pharyngitis', 'and'),
        Edge('HAS_BRANCH_COMBINATION', 'item_common_cold', 'or'),
        Edge('HAS_BRANCH_COMBINATION', 'item_pharyngitis', 'or'),
        Edge('HAS_BRANCH', 'acute_upper_respiratory_infection', 'common_cold'),
        Edge('HAS_BRANCH', 'acute_upper_respiratory_infection', 'pharyngitis'),
        Edge('HAS_BRANCH', 'common_cold', 'item_common_cold'),
        Edge('HAS_BRANCH', 'common_cold', 'nasal_catarrh_symptoms'),
        Edge('HAS_BRANCH', 'item_common_cold', 'fever'),
        Edge('HAS_BRANCH', 'item_common_cold', 'sneezing'),
        Edge('HAS_BRANCH', 'item_common_cold', 'nasal_congestion'),
        Edge('HAS_BRANCH', 'item_common_cold', 'throat_discomfort'),
        Edge('HAS_BRANCH', 'pharyngitis', 'item_pharyngitis'),
        Edge('HAS_BRANCH', 'pharyngitis', 'throat_discomfort'),
        Edge('HAS_BRANCH', 'item_pharyngitis', 'cough'),
        Edge('HAS_BRANCH', 'item_pharyngitis', 'yellow_sputum'),
        Edge('HAS_BRANCH', 'item_pharyngitis', 'pharyngeal_exudate'),
        Edge('HAS_BRANCH', 'item_pharyngitis', 'elevated_white_blood_cells'),
        Edge('HAS_BRANCH', 'item_pharyngitis', 'fever')
    ],
    [
        Edge('HAS_BRANCH_COMBINATION', 'acute_bronchitis', 'and'),
        Edge('HAS_BRANCH_COMBINATION', 'item_acute_bronchitis1', 'and'),
        Edge('HAS_BRANCH_COMBINATION', 'item_acute_bronchitis2', 'or'),
        Edge('HAS_BRANCH_COMBINATION', 'item_acute_bronchitis3', 'or'),
        Edge('HAS_BRANCH_COMBINATION', 'item_acute_bronchitis11', 'or'),
        Edge('HAS_BRANCH', 'acute_bronchitis', 'item_acute_bronchitis1'),
        Edge('HAS_BRANCH', 'acute_bronchitis', 'item_acute_bronchitis2'),
        Edge('HAS_BRANCH', 'acute_bronchitis', 'item_acute_bronchitis3'),
        Edge('HAS_BRANCH', 'item_acute_bronchitis1', 'mild_systemic_symptoms'),
        Edge('HAS_BRANCH', 'item_acute_bronchitis1', 'item_acute_bronchitis11'),
        Edge('HAS_BRANCH', 'item_acute_bronchitis11', 'dry_cough'),
        Edge('HAS_BRANCH', 'item_acute_bronchitis11', 'increased_sputum_production'),
        Edge('HAS_BRANCH', 'item_acute_bronchitis11', 'worsening_cough'),
        Edge('HAS_BRANCH', 'item_acute_bronchitis11', 'hemoptysis'),
        Edge('HAS_BRANCH', 'item_acute_bronchitis11', 'fever'),
        Edge('HAS_BRANCH', 'item_acute_bronchitis2', 'no_obvious_positive_signs'),
        Edge('HAS_BRANCH', 'item_acute_bronchitis2', 'rales'),
        Edge('HAS_BRANCH', 'item_acute_bronchitis3', 'normal_white_blood_cell_count'),
        Edge('HAS_BRANCH', 'item_acute_bronchitis3', 'elevated_neutrophil_percentage'),
        Edge('HAS_BRANCH', 'item_acute_bronchitis3', 'increased_blood_sedimentation_rate'),
        Edge('HAS_BRANCH', 'item_acute_bronchitis3', 'normal_chest_x_ray')
    ],
    # [
    #     Edge('HAS_BRANCH_COMBINATION', 'obstructive_sleep_apnea_syndrome', 'and'),
    #     Edge('HAS_BRANCH_COMBINATION', 'item_obstructive_sleep_apnea_syndrome1', 'or'),
    #     Edge('HAS_BRANCH_COMBINATION', 'item_obstructive_sleep_apnea_syndrome2', 'or'),
    #     Edge('HAS_BRANCH', 'obstructive_sleep_apnea_syndrome', 'item_obstructive_sleep_apnea_syndrome1'),
    #     Edge('HAS_BRANCH', 'obstructive_sleep_apnea_syndrome', 'item_obstructive_sleep_apnea_syndrome2'),
    #     Edge('HAS_BRANCH', 'item_obstructive_sleep_apnea_syndrome1', 'dry_mouth_on_awakening'),
    #     Edge('HAS_BRANCH', 'item_obstructive_sleep_apnea_syndrome1', 'loud_snoring'),
    #     Edge('HAS_BRANCH', 'item_obstructive_sleep_apnea_syndrome1', 'breathing_pause_during_sleep'),
    #     Edge('HAS_BRANCH', 'item_obstructive_sleep_apnea_syndrome1', 'daytime_sleepiness'),
    #     Edge('HAS_BRANCH', 'item_obstructive_sleep_apnea_syndrome2', 'daytime_sleepiness'),
    #     Edge('HAS_BRANCH', 'item_obstructive_sleep_apnea_syndrome2', 'breathing_pause_or_hypopnea'),
    #     Edge('HAS_BRANCH', 'item_obstructive_sleep_apnea_syndrome2', 'AHI_greater_than_5'),
    #     Edge('HAS_BRANCH', 'item_obstructive_sleep_apnea_syndrome2', 'nighttime_snoring')
    # ],
]


def add_nodes_to_db(node_list):
    db = DB()
    driver = db.get_driver()

    with driver.session(database="disease") as session:
        for obj in node_list:
            label = obj.getType()
            properties = obj.attrs
            name = obj.getAttr('name')
            if name is not None:
                existing_node = session.execute_read(db._get_node_by_name, name)
                # existing_node = db.get_node_by_name(name)
                if existing_node is not None:
                    continue
            session.execute_write(db._create_node, label, properties)
    db.close()


def add_edges_to_db(edge_list):
    db = DB()
    driver = db.get_driver()

    with driver.session(database="disease") as session:
        for obj in edge_list:
            rel_type = obj.type
            start_node_name = obj.start_id
            end_node_name = obj.end_id

            query = f"""
            MATCH (s {{name:'{start_node_name}'}})-[r:{rel_type}]->(e {{name:'{end_node_name}'}})
            RETURN COUNT(r) > 0 as exists
            """
            result = session.run(query).single().value()
            if result:
                continue

            start_node = session.execute_read(db._get_node_by_name, start_node_name)
            if start_node is None:
                continue
            start_label = list(start_node.labels)[0]
            if rel_type == 'HAS_BRANCH_COMBINATION':
                query = f"MATCH (start:{start_label} {{name: $start_name}}) CREATE (a:Logic {{name: $logic_name}}), (start)-[:{rel_type}]->(a)"
                session.run(query, start_name=start_node_name, logic_name=end_node_name)
            else:
                end_node = session.execute_read(db._get_node_by_name, end_node_name)
                if end_node is None:
                    continue
                end_label = list(end_node.labels)[0]
                query = f"MATCH (start:{start_label} {{name: $start_name}}), (end:{end_label} {{name: $end_name}}) CREATE (start)-[:{rel_type}]->(end)"
                session.run(query, start_name=start_node_name, end_name=end_node_name)
    db.close()


def add_knowledge_to_db(obj):
    db = DB()
    driver = db.get_driver()

    with driver.session(database="knowledge") as session:
        label = obj.getType()
        properties = obj.attrs
        name = obj.getAttr('name')
        if name is not None:
            existing_node = session.execute_read(db._get_node_by_name, name)
            # existing_node = db.get_node_by_name(name)
            if existing_node is None:
                session.execute_write(db._create_node, label, properties)
    db.close()

for node in adding_nodes:
    add_nodes_to_db(node)
for edge in adding_paths:
    add_edges_to_db(edge)
for knowlege in knowledges:
    add_knowledge_to_db(knowlege)
# for node in nodes:
#     node_type = node.getType()
#     attr_dict = node.attrs
#     attr_str = "{" + ", ".join([f"{k}: '{v}'" for k, v in attr_dict.items()]) + "}"
#     query = f"CREATE (n:{node_type} {attr_str})"
#     print(query)
#
# for edge in edges:
#     edge_type = edge.getType()
#     start_id = edge.getStartId()
#     end_ids = edge.getEndId()
#     end_id_str = "[" + ", ".join([f"'{id}'" for id in end_ids]) + "]"
#     query = f"MATCH (start {{id: '{start_id}'}}), (end {{id: '{end_ids[0]}'}}) CREATE (start)-[:{edge_type}]->(end:{end_ids[1]} {end_id_str})"
#     print(query)


# def add_edges_to_db(edge_list):
#     db = DB()
#     driver = db.get_driver()
#
#     with driver.session(database="disease") as session:
#         for obj in edge_list:
#             rel_type = obj.type
#             start_node_name = obj.start_id
#             end_node_name = obj.end_id
#
#             query = f"""
#             MATCH (s {{name:'{start_node_name}'}})-[r:{rel_type}]->(e {{name:'{end_node_name}'}})
#             RETURN COUNT(r) > 0 as exists
#             """
#             result = session.run(query).single().value()
#             if result:
#                 continue
#
#             start_node = session.execute_read(db._get_node_by_name, start_node_name)
#             if start_node is None:
#                 continue
#             if rel_type == 'HAS_BRANCH_COMBINATION':
#                 query = f"MATCH (start:{start_node.labels.pop()} {{name: $start_name}}) CREATE (a:Logic {{name: 'and'}}), (start)-[:{rel_type}]->(a)"
#                 session.run(query, start_name=start_node_name, end_name=end_node_name)
#             else:
#                 end_node = session.execute_read(db._get_node_by_name, end_node_name)
#                 if end_node is None:
#                     continue
#                 query = f"MATCH (start:{start_node.labels.pop()} {{name: $start_name}}), (end:{end_node.labels.pop()} {{name: $end_name}}) CREATE (start)-[:{rel_type}]->(end)"
#                 session.run(query, start_name=start_node_name, end_name=end_node_name)
#     db.close()

