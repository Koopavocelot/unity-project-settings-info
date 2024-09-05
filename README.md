# Unity Project Settings Info
Github action that retrieves ProjectSettings info for Unity project and outputs it via github actions output.
This fork contains additional outputs from ProjectSettings, not included in the original.


## Outputs
* `bundle-version` - The current bundle version found in the ProjectSettings.
* `bundle-code` - The current Android bundle code found in the ProjectSettings.

## Example Usage

```yaml
name: Project Settings Info

on: workflow_dispatch

jobs:
  get-project-info:
    runs-on: ubuntu-latest
    name: "A job to test unity-project-settings-info"
    steps:
      - name: "Checkout"
        uses: actions/checkout@v2
        with:
          fetch-depth: 0
      - name: "Unity Project Settings Info"
        id: unity-project-settings-info
        uses: Breakstep-Studios/unity-project-settings-info@v1.0.0
      - name: "Output Bundle Version and Bundle Code"
        run: |
          echo bundleVersion: ${{ steps.unity-project-settings-info.outputs.bundle-version }}
          echo bundleCode: ${{ steps.unity-project-settings-info.outputs.bundle-code }}
```

## TODO

### Short Term
* Outputting of commonly used ProjectSettings fields. Create issue / pr for modifications.

### Long Term
* Dynamic retrieval of various ProjectSettings values based on some input query?
