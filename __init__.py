import unittest
import test_000create_doc
import test_002edit_doc
import test_001look_doc_by_mod
import test_003tuijiandaomuban
import test_101delete_doc
import test_004bjcz_yanshi
import test_005bjcz_xiazai
import test_006fenbianlv
import test_100rename_mod


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(test_000create_doc.CreateDoc))
suite.addTest(unittest.makeSuite(test_002edit_doc.EditButton))
suite.addTest(unittest.makeSuite(test_001look_doc_by_mod.LookDoc))
suite.addTest(unittest.makeSuite(test_003tuijiandaomuban.TuiJian))
suite.addTest(unittest.makeSuite(test_005bjcz_xiazai.XiaZai))
suite.addTest(unittest.makeSuite(test_004bjcz_yanshi.Yanshi))
suite.addTest(unittest.makeSuite(test_006fenbianlv.FenBianLv))
suite.addTest(unittest.makeSuite(test_100rename_mod.RenameDoc))
suite.addTest(unittest.makeSuite(test_101delete_doc.DeleteDoc))