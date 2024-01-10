# CASE用法
# 示例：当前逾期标记
# select
#   case
#     rpy_flag
#     when rpy_flag = "OD" then 'True'
#     else 'False'
#   end currentOverMark
# from
#   tenant_db_zbank.cloudbank_lcsx_db_ln_plan