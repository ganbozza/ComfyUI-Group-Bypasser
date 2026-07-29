class ComfyUIGroupBypasser:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # We use an internal string config to save state
                "toggle_config": ("STRING", {"default": "{}"}), 
            },
            "optional": {
                # Dummy hidden input to trigger UI re-renders on the backend side if needed
                "refresh_trigger": ("INT", {"default": 0, "min": 0, "max": 999999, "step": 1}),
            }
            }

    RETURN_TYPES = ("BOOLEAN", "STRING")
    RETURN_NAMES = ("is_active", "active_toggles_list")
    FUNCTION = "noop"
    CATEGORY = "utils"

    def noop(self, toggle_config, refresh_trigger=0, **kwargs):
        # kwargs catches any dynamically added Python inputs or mapped subgraph bindings
        try:
            config = json.loads(toggle_config)
        except Exception:
            config = {}

        # Merge configuration and kwargs to get accurate boolean values
        active_toggles = []
        for key, val in kwargs.items():
            if val is True:
                active_toggles.append(key)
        
        # If evaluation maps directly to config keys:
        for key, val in config.items():
            if val is True and key not in active_toggles:
                active_toggles.append(key)

        is_active = len(active_toggles) > 0
        return (is_active, ", ".join(active_toggles))


NODE_CLASS_MAPPINGS = {
    "ComfyUI-Group-Bypasser": ComfyUIGroupBypasser,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI-Group-Bypasser": "Group Bypasser",
}
