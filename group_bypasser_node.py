class ComfyUIGroupBypasser:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                # Dummy hidden input to trigger UI re-renders on the backend side if needed
                "toggle_feature": ("BOOLEAN", {"default": False, "label_on": "Enabled", "label_off": "Disabled"}),
            }
        }

    RETURN_TYPES = ()
    RETURN_NAMES = ()
    FUNCTION = "noop"
    CATEGORY = "utils"

    def noop(self, toggle_feature):
       # Process the boolean state dynamically in your backend logic
        if toggle_feature:
            result = f"Feature active! Processing"
        else:
            result = "Feature inactive."
        return (result,)


NODE_CLASS_MAPPINGS = {
    "ComfyUI-Group-Bypasser": ComfyUIGroupBypasser,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI-Group-Bypasser": "Group Bypasser",
}
