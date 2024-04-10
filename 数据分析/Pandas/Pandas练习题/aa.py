# distutils: language=3
# cython: language_level=3
# -*- coding: utf-8 -*-
# @Time    : 2024/2/2 14:48
# @Author  : zhuzhiwei-jk
# @Description:
import datetime
import json

import pandas as pd


# kd = pd.read_csv('20240202_1444_mongo_argus_antifraud_db_event_info_last7d_Doris_BJMD.csv')
# print(kd)
# kd.sort_values(by="phone_count", inplace=False, ascending=True)
# now = datetime.datetime.now()
# current_date = datetime.datetime(now.year, now.month, now.day)
# print(current_date).strftime('%Y-%m-%d %H:%M:%S')
# base_sql = "SELECT distinct(history.customerManagerId) \
#                 FROM mongo_argus_antifraud_db_event_info_history history \
#                 WHERE history.customerManagerId is NOT null \
#                         AND history.customerManagerId != '' AND history.eventCode ='{}' \
#                     UNION ALL \
#                 SELECT distinct(last.customerManagerId) \
#                 FROM mongo_argus_antifraud_db_event_info_last7d last7d \
#                 WHERE last7d.customerManagerId is NOT null \
#                         AND last7d.customerManagerId != '' AND last7d.eventCode ='{}';"
# manager_sql_credit = base_sql.format('CREDIT', 'CREDIT')
# print(manager_sql_credit)

# kd = pd.read_csv('20240202_1714_mongo_argus_antifraud_db_event_info_last7d_Doris_BJMD.csv')
# for index, row in kd.iterrows():
#     rr = row.to_dict()['ruleResult']
#     json.loads(row['ruleResult'])
#     print(json.loads(rr)['creditResultInfo']['intRuleList'][0]['intRuleNum'])

def extract_value(json_str, rule_list):
    try:
        json_dict = json.loads(json_str)
        int_rule_list = json_dict.get('creditResultInfo', {}).get('intRuleList', [])
        if len(int_rule_list) == 0:
            return False, []
        else:
            int_rule_list = [j.get('intRuleNum', '') for j in int_rule_list]
            rule_set = set(rule_list)
            has_intersection = any(rule in rule_set for rule in int_rule_list)
            return has_intersection, int_rule_list
    except json.JSONDecodeError:
        return False, []


anti_fraud_rejection_rules = ['FRA_CREDIT_BH06_002', 'FRA_CREDIT_BH06_003', 'FRR_CREDIT_AD01_001',
                              'FRR_CREDIT_AD02_001', 'FRR_CREDIT_BH08_001']

kd = pd.read_csv('20240204_1442_mongo_argus_antifraud_db_event_info_history_Doris_BJMD.csv')
result = kd['ruleResult'].apply(lambda x: extract_value(x, anti_fraud_rejection_rules))
kd['rule_mark'], kd['intRuleList'] = result.str[0], result.str[1]
kd = kd[kd['rule_mark'] == True]
print(kd)
for i in kd['mobileNo'].unique().tolist():
    print(i)
