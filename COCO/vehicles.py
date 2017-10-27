# This is the 'sloth' config file I use to visualize and edit the
# converted (COCO -> sloth) json file.
#
# Usage:
# sloth -c vehicles.py /data/COCO-2017-vehicle/train.json

LABELS = (
    {"attributes": {"type": "rect", "class": "bicycle"},
     "item":     "sloth.items.RectItem",
     "inserter": "sloth.items.RectItemInserter",
     "text":     "bicycle"
    },

    {"attributes": {"type": "rect", "class": "car"},
     "item":     "sloth.items.RectItem",
     "inserter": "sloth.items.RectItemInserter",
     "text":     "car"
    },

    {"attributes": {"type": "rect", "class": "motorcycle"},
     "item":     "sloth.items.RectItem",
     "inserter": "sloth.items.RectItemInserter",
     "text":     "motorcycle"
    },

    {"attributes": {"type": "rect", "class": "bus"},
     "item":     "sloth.items.RectItem",
     "inserter": "sloth.items.RectItemInserter",
     "text":     "bus"
    },

    {"attributes": {"type": "rect", "class": "train"},
     "item":     "sloth.items.RectItem",
     "inserter": "sloth.items.RectItemInserter",
     "text":     "train"
    },

    {"attributes": {"type": "rect", "class": "truck"},
     "item":     "sloth.items.RectItem",
     "inserter": "sloth.items.RectItemInserter",
     "text":     "truck"
    },

    {"attributes": {"type": "rect", "class": "boat"},
     "item":     "sloth.items.RectItem",
     "inserter": "sloth.items.RectItemInserter",
     "text":     "boat"
    },
)
