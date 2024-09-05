from unityparser import UnityDocument


def run():
    project_settings_file_path = 'ProjectSettings/ProjectSettings.asset'
    unity_document = UnityDocument.load_yaml(project_settings_file_path)
    projectsettings_monobehaviour_document = unity_document.entry

    try:
        bundle_version = projectsettings_monobehaviour_document.bundleVersion
        bundle_code = projectsettings_monobehaviour_document.AndroidBundleVersionCode
    except AttributeError:
        print("Failed to find bundleVersion in ProjectSettings.asset")
        return

    print("bundle_version: " + str(bundle_version))
    print("bundle_code: " + str(bundle_code))

    print(f"::set-output name=bundle-version::{str(bundle_version)}")
    print(f"::set-output name=bundle-code::{str(bundle_code)}")

    return


run()
