curriculum_schema = {
    "type": "object",
    "properties": {
        "rules": {
            "type": "object",
            "properties": {
                "minimum_credits": {"type": "integer"},
                "minimum_national_voluntary_credits": {"type": "integer"},
                "minimum_special_task_credits": {"type": "integer"},
                "maximum_excluded_credits_special_task": {"type": "integer"},
                "group_subjects": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "subjects": {
                                "type": "array",
                                "items": {"type": "string"},
                                "minItems": 1}
                        },
                        "required": ["name", "subjects"],
                        "additionalProperties": False
                    }
                },
                "basket_subjects": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "subjects": {
                                "type": "array",
                                "items": {"type": "string"},
                                "minItems": 1},
                            "minimum_compulsory_total": {"type": "integer"},
                            "minimum_compulsory_per_subject": {"type": "integer"},
                        },
                        "required": [
                            "name",
                            "subjects",
                            "minimum_compulsory_total",
                            "minimum_compulsory_per_subject"],
                        "additionalProperties": False
                    }
                },
                "national_mandatory_subjects": {"type": "array", "items": {"type": "string"}},
                "national_voluntary_subjects": {"type": "array", "items": {"type": "string"}},
                "special_task_code": {"type": "string"},
                "own_courses_codes": {"type": "array", "items": {"type": "string"}}
            },
            "required": [
                "minimum_credits",
                "minimum_national_voluntary_credits",
                "minimum_special_task_credits",
                "maximum_excluded_credits_special_task",
                "group_subjects",
                "basket_subjects",
                "national_mandatory_subjects",
                "national_voluntary_subjects"],
            "additionalProperties": False
        },
        "subjects": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "courses": {
                        "types": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "credits": {"type": "integer"},
                                "mandatory": {"type": "boolean"},
                                "national": {"type": "boolean"}
                            }
                        }}
                }}},
    },
    "required": ["rules", "subjects"],
    "additionalProperties": False
}
