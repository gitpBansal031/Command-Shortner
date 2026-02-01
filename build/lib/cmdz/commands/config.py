import os
import json

CONFIG_DIR = os.path.expanduser("~/.cmdz")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")


def _ensure_dir():
    os.makedirs(CONFIG_DIR, exist_ok=True)


def _load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE) as f:
        return json.load(f)


def _save_config(config: dict):
    _ensure_dir()
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)


def set_namespace(namespace: str):
    config = _load_config()
    config["namespace"] = namespace
    _save_config(config)
    print(f"Namespace set to: {namespace}")


def get_namespace():
    config = _load_config()
    ns = config.get("namespace")
    if not ns:
        print("Namespace not set. Run: cmdz setns <namespace>")
    else:
        print("Namespace:",ns)


def set_env(env: str):
    if env not in ("dev", "stg"):
        print("Env can be either dev or stg")
        return

    config = _load_config()
    config["env"] = env
    _save_config(config)
    print("Env set to:",env)


def get_env():
    config = _load_config()
    env = config.get("env")
    if not env:
        print("Env not set. Run: cmdz setenv <env>")
    else:
        print("Env:",env)