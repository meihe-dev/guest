from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import

# 使用库suds_jurko: https://bitbucket.org/jurko/suds
# Web Services查询：http://www.webxml.com.cn/zh_cn/web_services.aspx

# 天气查询
# url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx?wsdl'
url = 'http://ws.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl'

imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
imp.filter.add('http://WebXml.com.cn/')

client = Client(url, plugins=[ImportDoctor(imp)])

# print(client)

'''
Suds ( https://fedorahosted.org/suds/ )  version: 0.6

Service ( WeatherWebService ) tns="http://WebXml.com.cn/"
   Prefixes (1)
      ns0 = "http://WebXml.com.cn/"
   Ports (2):
      (WeatherWebServiceSoap)
         Methods (5):
            getSupportCity(xs:string byProvinceName)
            getSupportDataSet()
            getSupportProvince()
            getWeatherbyCityName(xs:string theCityName)
            getWeatherbyCityNamePro(xs:string theCityName, xs:string theUserID)
         Types (91):
            ArrayOfString
            xs:ENTITIES
            xs:ENTITY
            xs:ID
            xs:IDREF
            xs:IDREFS
            xs:NCName
            xs:NMTOKEN
            xs:NMTOKENS
            xs:NOTATION
            xs:Name
            xs:QName
            xs:all
            xs:allNNI
            xs:annotated
            xs:anyType
            xs:anyURI
            xs:attribute
            xs:attributeGroup
            xs:attributeGroupRef
            xs:base64Binary
            xs:blockSet
            xs:boolean
            xs:byte
            xs:complexRestrictionType
            xs:complexType
            xs:date
            xs:dateTime
            xs:decimal
            xs:derivationControl
            xs:derivationSet
            xs:double
            xs:duration
            xs:element
            xs:explicitGroup
            xs:extensionType
            xs:facet
            xs:float
            xs:formChoice
            xs:fullDerivationSet
            xs:gDay
            xs:gMonth
            xs:gMonthDay
            xs:gYear
            xs:gYearMonth
            xs:group
            xs:groupRef
            xs:hexBinary
            xs:int
            xs:integer
            xs:keybase
            xs:language
            xs:localComplexType
            xs:localElement
            xs:localSimpleType
            xs:long
            xs:namedAttributeGroup
            xs:namedGroup
            xs:namespaceList
            xs:narrowMaxMin
            xs:negativeInteger
            xs:noFixedFacet
            xs:nonNegativeInteger
            xs:nonPositiveInteger
            xs:normalizedString
            xs:numFacet
            xs:openAttrs
            xs:positiveInteger
            xs:public
            xs:realGroup
            xs:reducedDerivationControl
            xs:restrictionType
            xs:short
            xs:simpleDerivationSet
            xs:simpleExplicitGroup
            xs:simpleExtensionType
            xs:simpleRestrictionType
            xs:simpleType
            xs:string
            xs:time
            xs:token
            xs:topLevelAttribute
            xs:topLevelComplexType
            xs:topLevelElement
            xs:topLevelSimpleType
            xs:typeDerivationControl
            xs:unsignedByte
            xs:unsignedInt
            xs:unsignedLong
            xs:unsignedShort
            xs:wildcard
      (WeatherWebServiceSoap12)
         Methods (5):
            getSupportCity(xs:string byProvinceName)
            getSupportDataSet()
            getSupportProvince()
            getWeatherbyCityName(xs:string theCityName)
            getWeatherbyCityNamePro(xs:string theCityName, xs:string theUserID)
         Types (91):
            ArrayOfString
            xs:ENTITIES
            xs:ENTITY
            xs:ID
            xs:IDREF
            xs:IDREFS
            xs:NCName
            xs:NMTOKEN
            xs:NMTOKENS
            xs:NOTATION
            xs:Name
            xs:QName
            xs:all
            xs:allNNI
            xs:annotated
            xs:anyType
            xs:anyURI
            xs:attribute
            xs:attributeGroup
            xs:attributeGroupRef
            xs:base64Binary
            xs:blockSet
            xs:boolean
            xs:byte
            xs:complexRestrictionType
            xs:complexType
            xs:date
            xs:dateTime
            xs:decimal
            xs:derivationControl
            xs:derivationSet
            xs:double
            xs:duration
            xs:element
            xs:explicitGroup
            xs:extensionType
            xs:facet
            xs:float
            xs:formChoice
            xs:fullDerivationSet
            xs:gDay
            xs:gMonth
            xs:gMonthDay
            xs:gYear
            xs:gYearMonth
            xs:group
            xs:groupRef
            xs:hexBinary
            xs:int
            xs:integer
            xs:keybase
            xs:language
            xs:localComplexType
            xs:localElement
            xs:localSimpleType
            xs:long
            xs:namedAttributeGroup
            xs:namedGroup
            xs:namespaceList
            xs:narrowMaxMin
            xs:negativeInteger
            xs:noFixedFacet
            xs:nonNegativeInteger
            xs:nonPositiveInteger
            xs:normalizedString
            xs:numFacet
            xs:openAttrs
            xs:positiveInteger
            xs:public
            xs:realGroup
            xs:reducedDerivationControl
            xs:restrictionType
            xs:short
            xs:simpleDerivationSet
            xs:simpleExplicitGroup
            xs:simpleExtensionType
            xs:simpleRestrictionType
            xs:simpleType
            xs:string
            xs:time
            xs:token
            xs:topLevelAttribute
            xs:topLevelComplexType
            xs:topLevelElement
            xs:topLevelSimpleType
            xs:typeDerivationControl
            xs:unsignedByte
            xs:unsignedInt
            xs:unsignedLong
            xs:unsignedShort
            xs:wildcard
'''

result = client.service.getWeatherbyCityName('石首')
print(result)