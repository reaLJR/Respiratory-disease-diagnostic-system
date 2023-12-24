class MR:
    def __init__(self, patient_id, mr_type, attributes):
        self.patient_id = patient_id
        self.mr_type = mr_type
        self.attributes = attributes

    def getType(self):
        return self.mr_type

    def getAttribute(self, name):
        return self.attributes.get(name)

def generate_MRs_rule(MRs):
    # 定义基础类型列表
    basics = ['Symptom', 'Nature', 'Position', 'Severity', 'AttackTime', 'Duration', 'Frequency',
              'Feature', 'Aura', 'Mitigation', 'Incentive', 'Family', 'History', 'Auxiliary', 'Medical', 'Prodrome']

    MRs_rule = []

    for mr in MRs:
        mr_rule = []
        mr_rule.append(mr.getType())

        # 获取当前证据项类型的全部属性类型集合
        attributes = []
        if mr.getType() == 'Symptom':
            attributes = ['name', 'credibility']
        elif mr.getType() == 'Nature':
            attributes = ['name', 'certainty']
        elif mr.getType() == 'Position':
            attributes = ['name', 'position', 'side', 'certainty']
        elif mr.getType() == 'Severity':
            attributes = ['level', 'certainty']
        elif mr.getType() == 'AttackTime':
            attributes = ['hour', 'certainty']
        elif mr.getType() == 'Duration':
            attributes = ['start_time', 'end_time', 'certainty']
        elif mr.getType() == 'Frequency':
            attributes = ['times', 'duration', 'unit', 'certainty']

        # 将所有属性值加入到mr_rule中，如果属性值不存在，则加入空值
        for attribute in attributes:
            name = attribute
            if name in mr.attributes.keys():
                mr_rule.append(mr.attributes[name])
            else:
                mr_rule.append('')

        MRs_rule.append(mr_rule)

    return MRs_rule

def print_MRs(MRs):
    MRs_rule = generate_MRs_rule(MRs)

    # 输出MRs_rule的ASP表示
    for mr_rule in MRs_rule:
        asp_str = mr_rule[0] + '(' + '"' + MRs[MRs_rule.index(mr_rule)].patient_id + '"' + ','
        asp_str += ','.join(['"' + x + '"' for x in mr_rule[1:]]) + ').'
        print(asp_str)


test_MRs = [MR("病人1", "mr_Nature", {"patient_id": "病人1", "symptom": "胀痛", "certainty": "c"}),
       MR("病人1", "mr_Position", {"patient_id": "病人1", "location": "双侧", "side": "顶部", "part": "c"}),
       MR("病人1", "mr_Severity", {"patient_id": "病人1", "level": "中度"}),
       MR("病人1", "mr_AttackTime", {"patient_id": "病人1", "hour": 10, "certainty": "c"}),
       MR("病人1", "mr_Duration", {"patient_id": "病人1", "start_time": 360, "end_time": 360, "certainty": "c"}),
       MR("病人1", "mr_Frequency", {"patient_id": "病人1", "times": 1, "duration": 14, "unit": "月", "certainty": "c"})]

# print_MRs(MRs)


def get_has_symptom(symptoms):
    has_symptoms = set()
    for symptom in symptoms:
        has_symptom = 'has_symptom(' + symptom + ').'
        has_symptoms.add(has_symptom)
#     has_symptom = '''
# has_symptom(fever).
# has_symptom(cough).
# has_symptom(sore_throat).
#     '''
    return '\n'.join(has_symptoms)