import json
import Connectors
import Transformations
import AutoML
try:
    Adnan_DBFS = Connectors.DBFSConnector.fetch([], {}, "5e9703ae2f478682d5f01d90", spark,
                                                "{'url': '', 'file_type': 'Delimeted', 'dbfs_token': '', 'dbfs_domain': '', 'delimiter': ',', 'is_header': 'Use Header Line'}")

except Exception as ex:
    print(ex)
try:
    Adnan_AutoFE = Transformations.TransformationMain.run(["5e9703ae2f478682d5f01d90"], {
                                                          "5e9703ae2f478682d5f01d90": Adnan_DBFS}, "5e9703ae2f478682d5f01d91", spark, json.dumps({"FE": []}))

except Exception as ex:
    print(ex)
try:
    AutoML.functionRegression(Adnan_AutoFE, [], "")

except Exception as ex:
    print(ex)
