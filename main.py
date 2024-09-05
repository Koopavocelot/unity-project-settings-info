from unityparser import UnityDocument


def run():
    project_settings_file_path = 'ProjectSettings/ProjectSettings.asset'
    unity_document = UnityDocument.load_yaml(project_settings_file_path)
    projectsettings_monobehaviour_document = unity_document.entry

    bundle_version = ""
    bundle_code = 0
    try:
        bundle_version = projectsettings_monobehaviour_document.bundleVersion
        bundle_code = projectsettings_monobehaviour_document.AndroidBundleVersionCode
    except AttributeError:
        print("Failed to find bundleVersion in ProjectSettings.asset")
        return

    print("bundle_version: " + str(bundle_version))
    print("bundle_code: " + str(bundle_code))

    # see https://docs.github.com/en/actions/reference/workflow-commands-for-github-actions#setting-an-output-parameter
    print(f"::set-output name=bundle-version::{bundle_version}")
    print(f"::set-output name=bundle-code::{bundle_code}")

    return


run()
