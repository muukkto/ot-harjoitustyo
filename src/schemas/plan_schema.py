plan_schema = {
    "type": "object",
    "properties": {
        "config": {
            "type": "object",
            "properties": {
                "special_task": {"type": "boolean"},
                "meb_language": {"type": "string"},
                "graduation_period": {"type": "string"}
            },
            "required": ["config", "courses"],
            "additionalProperties": False
        },
        "courses": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "on_cur": {"type": "boolean"},
                    "code": {"type": "string"},
                    "subject": {"type": "string"},
                    "name": {"type": "string"},
                    "ects": {"type": "integer"}
                },
                "required": ["on_cur", "code", "subject", "name", "ects"],
                "additionalProperties": False
            }
        },
        "meb_plan": {
            "type": "object",
            "properties": {
                "1": {"type": "array", "items": {"type": "string"}},
                "2": {"type": "array", "items": {"type": "string"}},
                "3": {"type": "array", "items": {"type": "string"}}
            }
        }
    },
    "required": ["config", "courses", "meb_plan"],
    "additionalProperties": False
}
