class ComfyUIGroupBypasser:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            # Creates a boolean widget/input (True/False toggle)
                "my_bool": ("BOOLEAN", {"default": False, "force_input": False}),
        }}

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ()
    FUNCTION = "noop"
    CATEGORY = "utils"

    def noop(self, my_bool):
        return (my_bool,)


NODE_CLASS_MAPPINGS = {
    "ComfyUI-Group-Bypasser": ComfyUIGroupBypasser,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI-Group-Bypasser": "Group Bypasser",
}
