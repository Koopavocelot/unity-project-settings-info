from unityparser import UnityDocument


def run():
    project_settings_file_path = 'ProjectSettings/ProjectSettings.asset'
    unity_document = UnityDocument.load_yaml(project_settings_file_path)
    projectsettings_monobehaviour_document = unity_document.entry

    bundle_code = 0
    try:
        bundle_code = projectsettings_monobehaviour_document.AndroidBundleVersionCode
    except AttributeError:
        print("Failed to find bundleVersion in ProjectSettings.asset")
        return

    print("bundle_code: " + str(bundle_code))

    print(f"::set-output name=bundle-code::{bundle_code}")

    return


run()
