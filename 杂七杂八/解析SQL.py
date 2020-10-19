import sqlparse
from sqlparse.sql import IdentifierList, Identifier, Where
from sqlparse.tokens import Keyword, DML

sql_str = """
CREATE TABLE `hdp_ads_dw.dim_ad_channel`(
  `ad_channel_id`          BIGINT COMMENT '广告位渠道ID', 
  `ad_channel_name`        STRING COMMENT '广告位渠道名称', 
  `business_line_code`     STRING COMMENT '商业化产品线编码[BL_001=搜索推广|BL_002=PC展示|BL_003=移动展示]', 
  `business_line_name`     STRING COMMENT '商业化产品线名称[BL_001=搜索推广|BL_002=PC展示|BL_003=移动展示]', 
  `business_platform_code` STRING COMMENT '商业化平台[BP_001=点睛|BP_002=布尔|BP_003=聚效]', 
  `business_platform_name` STRING COMMENT '商业化平台[BP_001:点睛|BP_002:布尔|BP_003:聚效]', 
  `business_product_code`  STRING COMMENT '商业产品线产品编码', 
  `business_product_name`  STRING COMMENT '商业产品线产品名称', 
  `business_terminal_code` STRING COMMENT '投放终端[BT_001=PC|BT_002=移动]', 
  `business_terminal_name` STRING COMMENT '投放终端[BT_001=PC|BT_002=移动]', 
  `ba_channel_id`          STRING COMMENT '平台_渠道', 
  `is_valid`               TINYINT COMMENT '是否有效[0=无效|1=有效]', 
  `included_ad_pv`         TINYINT COMMENT '是否计入请求[0=不计入|1=计入]', 
  `included_ad_deal`       TINYINT COMMENT '是否计入处理[0=不计入|1=计入]', 
  `included_ad_view`       TINYINT COMMENT '是否计入展示[0=不计入|1=计入]', 
  `included_ad_click`      TINYINT COMMENT '是否计入点击[0=不计入|1=计入]', 
  `included_ad_cost`       TINYINT COMMENT '是否计入消费[0=不计入|1=计入]',
  `ad_channel_display`       STRING COMMENT '渠道显示名称',
  `ad_channel_classify_code` STRING COMMENT '渠道分类代码',
  `ad_channel_classify_name` STRING COMMENT '渠道分类名称',
  `source_type_code`         STRING COMMENT '媒体来源代码[internal=站内|external=站外]',
  `source_type_name`         STRING COMMENT '媒体来源名称[internal=站内|external=站外]',
  `flow_type_code`           STRING COMMENT '流量类型[standard=标准|non-standard=非标]',
  `flow_type_name`           STRING COMMENT '流量类型[standard=标准|non-standard=非标]',
  `kpi_income_classify_code` STRING COMMENT 'kpi渠道分类代码',
  `kpi_income_classify_name` STRING COMMENT 'kpi渠道分类名称'
) COMMENT '渠道信息维表'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
STORED AS TEXTFILE
LOCATION '/home/hdp-ads-dw/hive/warehouse/hdp_ads_dw.db/dim/dim_ad_channel';
"""

statement = sqlparse.parse(sql_str)[0]

for item in statement:
    if isinstance(item, IdentifierList):
        for identifier in item.get_identifiers():
            print(item.get_name())
    elif isinstance(item, Identifier):
        print(item.get_name())
    elif item.ttype is Keyword:
        print(item.value)

def is_subselect(parsed):
    if not parsed.is_group:
        return False
    for item in parsed.tokens:
        if item.ttype is DML and item.value.upper() == 'SELECT':
            return True
    return False


def extract_from_part(parsed):
    from_seen = False
    for item in parsed.tokens:
        if from_seen:
            if is_subselect(item):
                yield from extract_from_part(item)
            elif item.ttype is Keyword:
                return
            else:
                yield item
        elif item.ttype is Keyword and item.value.upper() == 'FROM':
            from_seen = True


def extract_table_identifiers(token_stream):
    for item in token_stream:
        if isinstance(item, IdentifierList):
            for identifier in item.get_identifiers():
                yield identifier.get_name()
        elif isinstance(item, Identifier):
            yield item.get_name()
        # It's a bug to check for Keyword here, but in the example
        # above some tables names are identified as keywords...
        elif item.ttype is Keyword:
            yield item.value


def extract_tables(sql):
    stream = extract_from_part(sqlparse.parse(sql)[0])
    return list(extract_table_identifiers(stream))


if __name__ == '__main__':
    sql = """
    select K.a,K.b from (select H.b from (select G.c from (select F.d from
    (select E.e from A, B, C, D, E), F), G), H), I, J, K order by 1,2;
    """

    tables = ', '.join(extract_tables(sql))
    print('Tables: {}'.format(tables))
