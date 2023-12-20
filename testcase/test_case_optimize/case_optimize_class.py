import allure
import pytest
import requests

from api.api import mobile_query
from utils.read import base_data

url = base_data.read_ini()['host']['api_sit_url']


@allure.epic("数据进制项目epic")
@allure.feature("手机号模块feature")
class TestMobile:
    @allure.story("北京的手机号story")
    @allure.title("测试手机号归属地title")
    @allure.testcase("https://www.yjwujian.cn/", name="接口地址testcase")
    @allure.issue("https://www.baidu.com", name="缺陷地址issue")
    @allure.link("https://www.yjwujian.cn/", name="链接地址link")
    @allure.description("当前手机号是13456755448，归属地是北京的description")
    @allure.step("先进行归属地的操作step")
    @allure.severity("minor")  # 五个等级：blocker critical normal minor trivial
    def test_mobile(self):
        params = base_data.read_data()['mobile_belong']
        print("测试手机归属地get请求")
        result = mobile_query(params)
        assert result.success is True
        assert result.body['status'] == 0
        assert result.body['msg'] == "ok"
        # assert result['result']["shouji"] == "13456755448"
        assert result.body['result']["province"] == "北京"
        assert result.body['result']["company"] == "中国移动"
        assert result.body['result']["areacode"] == "0571"

    @allure.story("北京的手机号story")
    @allure.title("测试手机号归属地title")
    @allure.testcase("https://www.yjwujian.cn/", name="接口地址testcase")
    @allure.issue("https://www.baidu.com", name="缺陷地址issue")
    @allure.link("https://www.yjwujian.cn/", name="链接地址link")
    @allure.description("当前手机号是13456755448，归属地是北京的description")
    @allure.step("先进行归属地的操作step")
    @allure.severity("minor")  # 五个等级：blocker critical normal minor trivial
    def test_mobile_dynamic(self):
        params = base_data.read_data()['mobile_belong_dynamic']["params"]
        title = base_data.read_data()['mobile_belong_dynamic']["title"]
        story = base_data.read_data()['mobile_belong_dynamic']["story"]
        allure.dynamic.story(story)
        allure.dynamic.title(title)
        print("测试手机归属地get请求")
        result = mobile_query(params)
        assert result.success is True
        assert result.body['status'] == 0
        assert result.body['msg'] == "ok"
        # assert result['result']["shouji"] == "13456755448"
        assert result.body['result']["province"] == "北京"
        assert result.body['result']["company"] == "中国移动"
        assert result.body['result']["areacode"] == "0571"


if __name__ == '__main__':
    pytest.main()
