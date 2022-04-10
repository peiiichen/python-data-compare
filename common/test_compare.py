import pytest
from common.db_operation import DbOperations
import pandas as pd
import time
import logging
log = logging.getLogger(__name__)


@pytest.fixture(params=DbOperations().get_db_result())
def compare_data(request):
    return request.param


# now = time.strftime('%Y-%m-%d_%H-%M-%S')
# file_path = "../result/result_"+now+".xlsx"
# pd.DataFrame().to_excel(file_path,index=False,header=False)
# writer = pd.ExcelWriter(file_path, mode="a", engine="openpyxl", if_sheet_exists='overlay' )


def test_data_compare(compare_data):
    case_name = compare_data[0]
    log.info("==================开始对比case_name:%s==================" % case_name)
    origin_result = pd.DataFrame(compare_data[1])
    log.info(origin_result)
    current_result = pd.DataFrame(compare_data[2])

    compare_result = origin_result.compare(current_result)
    log.info(compare_result)

    # compare_result.to_excel(excel_writer=writer, sheet_name=case_name, index=True,header=True)
    # writer.save()

    assert compare_result.empty is True
    log.info("测试结束")

