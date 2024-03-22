import pandas as pd
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
tables = ['MD_PRD', 'MD_PRD_AUTH_FRM', 'MD_PRD_ORPH_DSG', 'MD_PRD_IND_TXT', 'HD_PRD_CLS', 'HD_PRD_NM', 'ND_PRD_NM_PRT', 'MD_PRD_MSTR_FL', 'MD_PRD_PHCO_ENQ']
report_df = pd.DataFrame(columns=['PLND_TABLE_NAME', 'TOTAL_REC_CNT_IN_PLND', 'LND_TABLE_NAME', 'TOTAL_REC_CNT_IN_LND', 'RECORD_COUNT_VALIDATION', 'COL_NAME_VALIDATION'])

for tab in tables:
    cnt_status = ""
    v_status = ""
    plnd_count = ""
    lnd_count = ""
    col_status = ""
    cmt = ""
    plnd_db_tab = f"C_BO_{tab}_bview"
    lnd_db_tab = f"C_S_AD_{tab}_stview"
    
    try:
        plnd_cols = [col for col in spark.read.table(plnd_db_tab).columns if '_fk' not in col]
        lnd_cols = [col for col in spark.read.table(lnd_db_tab).columns if '_fk' not in col]
        
        plnd_cols_str = ', '.join(plnd_cols)
        lnd_cols_str = ', '.join(lnd_cols)
        
        plnd_df = spark.sql(f"SELECT {plnd_cols_str} FROM {plnd_db_tab}")
        lnd_df = spark.sql(f"SELECT {lnd_cols_str} FROM {lnd_db_tab}")
        
        plnd_count = plnd_df.count()
        lnd_count = lnd_df.count()
        
        if plnd_count == lnd_count:
            cnt_status = "Pass"
            if len(plnd_cols) == len(lnd_cols) and len(set(plnd_cols) - set(lnd_cols)) == 0:
                col_status = "Pass"
            else:
                col_status = "Fail"
        
            a_b_issues = plnd_df.exceptAll(lnd_df)  # A-B
            b_a_issues = lnd_df.exceptAll(plnd_df)  # B-A
            in_plnd_nt_lnd_cnt = a_b_issues.count()  # A-B_cnt
            in_lnd_nt_plnd_cnt = b_a_issues.count()  # B-A_cnt
            
            if in_plnd_nt_lnd_cnt == 0 and in_lnd_nt_plnd_cnt == 0:
                v_status = "Pass"
                cmt = "No mismatches!!"
        else:
            v_status = "Fail"
            cmt = "Mismatches Found!!"
        
        report_df = pd.concat([report_df, pd.DataFrame({'PLND_TABLE_NAME': [plnd_db_tab],
                                                        'TOTAL_REC_CNT_IN_PLND': [plnd_count],
                                                        'LND_TABLE_NAME': [lnd_db_tab],
                                                        'TOTAL_REC_CNT_IN_LND': [lnd_count],
                                                        'RECORD_COUNT_VALIDATION': [cnt_status],
                                                        'COL_NAME_VALIDATION': [col_status],
                                                        'REC_CNT_IN_PLND_NOT_IN_LND': [in_plnd_nt_lnd_cnt],
                                                        'REC_CNT_IN_LND_NOT_IN_PLND': [in_lnd_nt_plnd_cnt],
                                                        'DATA_VALIDATION': [v_status],
                                                        'COMMENTS': [cmt]})], ignore_index=True)
    except Exception as e:
        print(f"Error processing table {tab}: {str(e)}")

df = spark.createDataFrame(report_df)
df.show()
