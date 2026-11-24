"""Small offline catalog used by the XichuGeek tutorial."""
ITEMS = (
    {"name": "多口 USB 集线器", "group": "配件"},
    {"name": "键盘收纳盒", "group": "收纳"},
    {"name": "视频采集卡", "group": "配件"},
    {"name": "橡胶理线夹", "group": "收纳"},
    {"name": "桌面音箱", "group": "音频"},
)


def filter_catalog(group, page, page_size=2):
    if page < 1 or page_size < 1:
        raise ValueError("page and page_size must be positive")
    selected = [item for item in ITEMS if group == "全部" or item["group"] == group]
    start = (page - 1) * page_size
    return selected[start:start + page_size]


class CatalogPanel:
    def __init__(self):
        self.group = "全部"
        self.page = 1

    def select_group(self, group):
        self.group = group
        self.page = 1

    def visible(self):
        return filter_catalog(self.group, self.page)

