from suds.client import Client

# 使用库suds_jurko: https://bitbucket.org/jurko/suds
# Web Services查询：http://www.webxml.com.cn/zh_cn/web_services.aspx

# 电话号码归属地查询
url = 'http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
client = Client(url)
# print(client)
'''
Suds ( https://fedorahosted.org/suds/ )  version: 0.6

Service ( MobileCodeWS ) tns="http://WebXml.com.cn/"
   Prefixes (1)
      ns0 = "http://WebXml.com.cn/"
   Ports (2):
      (MobileCodeWSSoap)
         Methods (2):
            getDatabaseInfo()
            getMobileCodeInfo(xs:string mobileCode, xs:string userID)
         Types (1):
            ArrayOfString
      (MobileCodeWSSoap12)
         Methods (2):
            getDatabaseInfo()
            getMobileCodeInfo(xs:string mobileCode, xs:string userID)
         Types (1):
            ArrayOfString
'''

result = client.service.getMobileCodeInfo('1XXXXX')
print(result)