"""Module for config related tasks"""

import json


data_config = {
    "data": {
        "name": "data_loader",
        "type": ["list", "csv"],
        "batch_size": 0
    },
}
permitted_steps = {
    "steps": {
        "normalize_text": {
            "type": [
                "lowercase",
                "remove_digits",
                "remove_punctuation",
                "remove_stopwords",
                "remove_whitespace",
                "expand_contractions",
                "remove_html",
                "porter_stemmer",
                "lemmatizer"
            ]
        }
    }
}
# If you use the key it must run before the value
step_order = {
    "remove_html": [
        "remove_punctuation",
        "porter_stemmer",
        "lemmatizer"
    ],
}
required_pre_steps = {
    "remove_stopwords": ["lowercase"]
}


def validate_config(config, log_level):
    """
    Validate config passed. If there is not a log level
    for a step use the level passed into this method. Some
    steps rely on others steps, checks are put in place to
    raise errors for such case. For example the stopword
    steps require the lowercase step.

    Args:
        config (obj): config object
        log_level (str): log level for each step
    Returns:
        obj if no errors returns config
    """

    # Confirm Required Steps
    for key, val in data_config.items():
        if not config.get(key):
            raise KeyError(
                "The {} section is missing from config!".format(key)
            )
        for sub_key, sub_val in val.items():
            if not config[key].get(sub_key):
                raise KeyError(
                    "{} is missing from the {} section!".format(sub_key, key)
                )
            if sub_key == "batch_size":
                if not isinstance(config[key].get(sub_key), int):
                    raise TypeError("batch_size must be type int!")
            elif config[key].get(sub_key) not in sub_val:
                raise ValueError(
                    "{} is not a valid option!".format(
                        config[key].get(sub_key))
                )
            elif config[key].get(sub_key) == "csv":
                if not config[key].get("file_path"):
                    raise ValueError(
                        "Csv data loaders require the file_path key!"
                    )
                if not config[key].get("columns"):
                    raise ValueError(
                        "Please add the columns key, with a dictionary "
                        " containing the id and data columns. For "
                        "example {'id': 'id', 'data': 'text_column'}"
                    )

        # Set the log level
        if not config[key].get("log_level"):
            config[key]["log_level"] = log_level

    steps_validated = []
    if config.get("steps"):
        # Check the steps are a list
        if not isinstance(config["steps"], list):
            raise TypeError("The config steps must be a list.")

        for step in config["steps"]:
            step_name = step.get("name")
            step_type = step.get("type")
            if not step.get("log_level"):
                step["log_level"] = log_level

            # Check for key errors
            if not step_name or not step_type:
                raise KeyError("Please use the keys name or type.")

            # Check if the step is valid
            if not permitted_steps["steps"].get(step_name):
                raise KeyError(
                    "{} is not a valid step!".format(step_name)
                )

            # Check if the type is valid
            permitted_type = permitted_steps["steps"][step_name]["type"]
            if step_type not in permitted_type:
                raise ValueError(
                    "{} is not a valid option in {}!".format(
                        step_type,
                        step_name
                    )
                )

            # Remove stopwords can accept options - default is short_list
            if step_type == "remove_stopwords":
                options = step.get("options", "short_list")
                if options not in ["short_list", "long_list", "custom"]:
                    raise ValueError(
                        "The remove stopwords options can only accept "
                        "short_list or long_list!"
                    )
                if options == "custom" and not step.get("custom_list"):
                    raise KeyError(
                        "Please add the custom list to your config with the "
                        "custom_list key!"
                    )
                step["options"] = options

            # Check to see if order matters with other steps
            steps_validated.append(step_type)
            if step_order.get(step_type):
                for check in step_order.get(step_type):
                    if check in steps_validated:
                        raise KeyError(
                            "The {} step can not run before the {}"
                            " step!".format(
                                check,
                                step_type
                            )
                        )
            # Check for steps that require other steps
            if required_pre_steps.get(step_type):
                for check in required_pre_steps.get(step_type):
                    if check not in steps_validated:
                        raise KeyError(
                            "The {} step requires the {}"
                            " as a previous step!".format(
                                step_type,
                                check
                            )
                        )

    else:
        raise KeyError("Please add steps to your config!")

    return config
