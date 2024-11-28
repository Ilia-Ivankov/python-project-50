expectation1 = """[
    {
        "key": "common",
        "status": "nested",
        "children": [
            {
                "key": "follow",
                "status": "added",
                "value": false
            },
            {
                "key": "setting1",
                "status": "unchanged",
                "value": "Value 1"
            },
            {
                "key": "setting2",
                "status": "removed",
                "value": 200
            },
            {
                "key": "setting3",
                "status": "updated",
                "old_value": true,
                "new_value": null
            },
            {
                "key": "setting4",
                "status": "added",
                "value": "blah blah"
            },
            {
                "key": "setting5",
                "status": "added",
                "value": {
                    "key5": "value5"
                }
            },
            {
                "key": "setting6",
                "status": "nested",
                "children": [
                    {
                        "key": "doge",
                        "status": "nested",
                        "children": [
                            {
                                "key": "wow",
                                "status": "updated",
                                "old_value": "",
                                "new_value": "so much"
                            }
                        ]
                    },
                    {
                        "key": "key",
                        "status": "unchanged",
                        "value": "value"
                    },
                    {
                        "key": "ops",
                        "status": "added",
                        "value": "vops"
                    }
                ]
            }
        ]
    },
    {
        "key": "group1",
        "status": "nested",
        "children": [
            {
                "key": "baz",
                "status": "updated",
                "old_value": "bas",
                "new_value": "bars"
            },
            {
                "key": "foo",
                "status": "unchanged",
                "value": "bar"
            },
            {
                "key": "nest",
                "status": "updated",
                "old_value": {
                    "key": "value"
                },
                "new_value": "str"
            }
        ]
    },
    {
        "key": "group2",
        "status": "removed",
        "value": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    },
    {
        "key": "group3",
        "status": "added",
        "value": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
]"""
