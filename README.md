# fm-face-finder

A tool to assist Football Manager players by automating the search for footballer images, cropping them to the required size for the game.

---

## Input Required

- Place an `.xlsx` file in the `/input/` folder.
- The file must have columns: `Name`, `Club`, and `UID`.
- You can retrieve this data from the Football Manager game's `.html` export.

---

## Setup

1. **Set up the Docker container** with this repository.
2. After setup, run these commands inside the container:
    ```sh
    sh .devcontainer/initialize.sh
    sh .devcontainer/python_env.sh
    ```

3. **Modify installed package methods:**
    - In `proj/modules/crop_image.py`, update the `HeadDetector` class as follows:
      ```python
      def _read_model(self, model: str) -> torch.jit.ScriptModule:
          model_path = hf_hub_download(REPO_ID, f"{model}.trcd")
          loaded_model = torch.jit.load(model_path, map_location=self._device)
      ```
    - In `proj/modules/download_image_bing.py`, for the `Better_Bing_Image_Downloader`'s `Downloader` class, remove the code that requests the image source.

4. **Reload the window** after making these modifications to ensure changes take effect.

---

## Running the Program

- Configure settings (such as which `.xlsx` file to use and desired season) in `config.py`.
- Run the main program:
  ```sh
  python main.py
  ```
- To clear output images:
  ```sh
  python clear_output_image.py
  ```
- To zip output images:
  ```sh
  python zip_output_image.py
- **Copy the `.zip` file from the container to your local machine** (run this in a terminal on your local computer, not inside the dev container):
    ```sh
    docker cp <container-id>:/workspaces/fm-face-finder/final_images.zip C:\Users\<username>\Downloads
    ```

---

## After Getting the Output Images

1. Place the `.zip` file in the `/graphics/` folder and extract it.
2. Use **fmXML** software to generate a config file for Football Manager.

---


