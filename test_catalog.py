import unittest
from catalog import CatalogPanel, filter_catalog


class CatalogTests(unittest.TestCase):
    def test_first_page_of_accessories(self):
        self.assertEqual([row["name"] for row in filter_catalog("配件", 1)],
                         ["多口 USB 集线器", "视频采集卡"])

    def test_all_items_keep_pagination(self):
        self.assertEqual(len(filter_catalog("全部", 3)), 1)


if __name__ == "__main__":
    unittest.main()

