import unittest
from catalog import CatalogPanel, filter_catalog


class CatalogTests(unittest.TestCase):
    def test_first_page_of_accessories(self):
        self.assertEqual([row["name"] for row in filter_catalog("配件", 1)],
                         ["多口 USB 集线器", "视频采集卡"])

    def test_all_items_keep_pagination(self):
        self.assertEqual(len(filter_catalog("全部", 3)), 1)


    def test_switching_filter_resets_page_and_shows_accessories(self):
        panel = CatalogPanel()
        panel.page = 3
        panel.select_group("配件")
        self.assertEqual(panel.page, 1)
        self.assertEqual([row["name"] for row in panel.visible()],
                         ["多口 USB 集线器", "视频采集卡"])

if __name__ == "__main__":
    unittest.main()

